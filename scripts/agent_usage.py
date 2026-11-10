r"""Token use of past Curio Class agents, by kind (docs/agents/TOKEN-PLAN.md).

    python scripts/agent_usage.py [project-folder-name]

Reads the local Claude Code agent logs (~/.claude/projects/<name>/*/subagents), keeps agents whose first prompt names
Curio Class, and prints medians for the newest 40 of each kind: turns, new input, cache writes, cache reads, output.
"""
import json,glob,os,re,collections,sys
root=os.path.join(os.path.expanduser('~'),'.claude','projects',sys.argv[1] if len(sys.argv)>1 else 'S--')
kinds=[('lens-teaching',r'`?Teaching`? lens'),('lens-play',r'`?Play`? lens'),('lens-craft',r'`?Craft`? lens'),('exit',r'exit check for ONE'),('final',r'Final look agent'),('plan',r'plan agent for ONE'),('spec',r'spec agent for ONE'),('sens',r'sensitivity'),('build',r'build agent for ONE'),('merge',r'[Mm]erge')]
rows=collections.defaultdict(list)
for f in glob.glob(os.path.join(root,'*','subagents','agent-*.jsonl')):
    try:
        first=None;turns=0;inp=cr=cc=out=0;tools=collections.Counter();model=None;seen=set();img=0;maxctx=0
        with open(f,encoding='utf-8',errors='ignore') as fh:
            for line in fh:
                try:d=json.loads(line)
                except: continue
                m=d.get('message') or {}
                if first is None and d.get('type')=='user':
                    c=m.get('content'); first=c if isinstance(c,str) else json.dumps(c)[:3000]
                if d.get('type')=='user' and isinstance(m.get('content'),list):
                    for b in m['content']:
                        if isinstance(b,dict) and b.get('type')=='tool_result' and isinstance(b.get('content'),list):
                            img+=sum(1 for x in b['content'] if isinstance(x,dict) and x.get('type')=='image')
                if d.get('type')=='assistant':
                    mid=m.get('id')
                    for b in m.get('content',[]):
                        if b.get('type')=='tool_use': tools[b['name']]+=1
                    if mid in seen: continue
                    seen.add(mid); u=m.get('usage') or {}; model=m.get('model') or model
                    turns+=1; inp+=u.get('input_tokens',0); cr+=u.get('cache_read_input_tokens',0); cc+=u.get('cache_creation_input_tokens',0); out+=u.get('output_tokens',0)
                    maxctx=max(maxctx,u.get('input_tokens',0)+u.get('cache_read_input_tokens',0)+u.get('cache_creation_input_tokens',0))
        if not first or 'Curio' not in first: continue
        k=next((n for n,p in kinds if re.search(p,first[:1500])),None)
        if not k: continue
        rows[k].append(dict(turns=turns,inp=inp,cr=cr,cc=cc,out=out,tools=tools,model=model,img=img,maxctx=maxctx,mt=os.path.getmtime(f)))
    except Exception as e: pass
import statistics as s
print('kind n | turns | fresh-in | cache-write | cache-read | out | final ctx | images | models')
for k,v in rows.items():
    v=sorted(v,key=lambda r:-r['mt'])[:40]
    md=lambda key:int(s.median([r[key] for r in v]))
    tl=collections.Counter()
    for r in v: tl.update(r['tools'])
    n=len(v)
    print(k,n,'|',md('turns'),'|',md('inp'),'|',md('cc'),'|',md('cr'),'|',md('out'),'|',md('maxctx'),'|',md('img'),'|',collections.Counter(r['model'] for r in v).most_common(3))
    print('   tools/agent:',{a:round(b/n,1) for a,b in tl.most_common(6)})

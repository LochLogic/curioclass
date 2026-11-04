import csv,sys
f,us=sys.argv[1],sys.argv[2].split(',')
for x in csv.DictReader(open(f+'.csv',encoding='utf-8')):
    if x['unit'] in us:
        if x['status']=='open': print(x['n'],'O',x['type'],'|',x['module'][:28],'|',x['title'],'|',x['students'])
        else: print(x['n'],x['status'][0].upper(),x['type'],'|',x['module'][:28],'|',x['title'])

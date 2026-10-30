# Super tool model checks

The Python each super-tool spec agent ran to check its model, goals and worst cases (docs/agents/SUPER.md). The
builder re-runs these to match the tool's numbers to the spec's Sources. Run from the tool's folder here, for example
`cd docs/agents/super-checks/living-pond && python suite.py`.

- pocket-universe: pu.py is the model (N-body leapfrog, merges); t3 to t27 are the goal and combination checks
  (t1 and t2 were overwritten by another agent's scratch files and are lost; their results are in the spec).
- living-pond: pond.py is the model; suite.py, goals.py, tracer.py, rescue.py and final.py the checks.
- molecule-forge: check1.py (bonding rules on every book molecule), legal_enum.py, crystal.py, salt2.py, push.py,
  with the PubChem data they read (pubchem.json, pc3d.json).
- span-and-spire: the truss stiffness solver, tower modal and shake checks.
- cipher-vault: round trips for all six rooms (Enigma checked against the AAAAA to BDZGO test vector), the
  substitution solver by length, Kasiski and the column splitter, the bombe search and the one-time-pad decoys.

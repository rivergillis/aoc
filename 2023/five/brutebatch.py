import subprocess

procs = []
# 10 seed source ranges
for i in range(10):
  procs.append(subprocess.Popen(["python", "brute2.py", f'{i}']))

for i,proc in enumerate(procs):
  print(f'waiting on proc {i}')
  proc.wait()
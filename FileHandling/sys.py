import sys
f = open("file.txt")
L1 = f.readline()
L2 = f.readline()
sys.stdout.write(L1)
sys.stdout.write(L2)
sys.stderr.write('No errors.')
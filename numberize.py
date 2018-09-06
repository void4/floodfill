import os
from sys import argv

if len(argv)<2:
	raise Exception("Missing <path>")

input("WARNING! THIS FILL RENAME ALL FILES IN THIS DIRECTORY!\nAre you sure: %s?" % argv[1])

start = 0

if len(argv)>=3:
	start = int(argv[2])

print("Starting at %i" % start)

for i,f in enumerate(sorted(os.listdir(argv[1]))):
	ending = "."+f.split(".")[-1]
	fname = ("/%i" % (start+i))+ending
	print("%s => %s" % (f,fname))
	os.rename(argv[1]+"/"+f,argv[1]+fname)

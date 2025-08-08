
fname=input("enter the file name:  ")

f = open(fname, "r")
data = f.read()
f.close()
symbols = "!@#$%^&*()_+{}:<>?[],./;'\|"

for s in symbols:
    data = data.replace(s, "")
words = data.split()

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

for w in counts:
    print(w, ":", counts[w])

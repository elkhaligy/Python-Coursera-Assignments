name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
dct = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith("From") and not(line.startswith("From:")):
        hour = line.split()[-2].split(":")[0]
        dct[hour] = dct.get(hour, 0)+1

lst = list()
for k, v in dct.items():
    lst.append((k, v))
res = sorted(lst)
for h, c in res:
    print(h, c)

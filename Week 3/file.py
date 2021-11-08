# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
handler = open(fname)
average = 0
count = 0
for line in handler:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    x = line.find(":")
    a = slice(x+1, len(line)-1, 1)
    average = average+float(line[a])
average = average/count
print("Average spam confidence: ", average,sep="")

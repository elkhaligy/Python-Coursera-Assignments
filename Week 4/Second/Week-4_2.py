file_handle = open('mbox-short.txt')
cnt = 0
for line in file_handle:
    line = line.rstrip()
    if line.startswith('From:'):
        lst = line.split()
        cnt = cnt+1
        print(lst[1])
    else:
        continue
print(f"There were {cnt} lines in the file with From as the first word")

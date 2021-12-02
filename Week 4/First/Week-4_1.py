file_handle = open('romeo.txt')
list = list()
for line in file_handle:
    print(line.rstrip())
    for i in line.split():
        if i not in list:
            list.append(i)
list.sort()
print(list)

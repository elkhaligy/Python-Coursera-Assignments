name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts=dict()
for line in fh:
        if line.startswith('From:'):
            words = line.split()
            counts[words[1]] = counts.get(words[1], 0)+1


most_word=None
most_word_count=None
for word,count in counts.items():
    if most_word_count==None or most_word_count<count:
        most_word=word
        most_word_count=count
print(most_word,most_word_count)

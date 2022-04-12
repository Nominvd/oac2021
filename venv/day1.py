handle = open('voorbeeld1dag1.txt')
count=0
prev = None
for line in handle:
    iline = int(line)
    if prev is not None and iline > prev:
        count = count + 1
    prev = iline
print(count)

handle = open('dag1.txt')
count=0
prev1 = None
prev2 = None
prev3 = None
for line in handle:
    iline = int(line)

    if prev1 is not None and prev2 is not None and prev3 is not None:
        if (prev1 + prev2 + prev3) < (prev2 + prev3 + iline):
            count = count + 1
    prev1 = prev2
    prev2 = prev3
    prev3 = iline
print(count)

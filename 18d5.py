with open("18d5_2.txt") as f:
    a= f.read().strip("\n")
a = list(a)
pos = 0
while pos < len(a):
    if pos + 1 < len(a) and a[pos].isupper() and a[pos + 1].islower() and \
    a[pos].upper() == a[pos+1].upper():
        a.pop(pos+1)
        a.pop(pos)
        pos -= 1
        pos = max(pos, 0)
    elif pos + 1 < len(a) and a[pos].islower() and a[pos + 1].isupper() and \
    a[pos].upper() == a[pos+1].upper():
        a.pop(pos+1)
        a.pop(pos)
        pos -= 1
        pos = max(pos, 0)
    else:
        pos += 1

print(a)
print(len(a))
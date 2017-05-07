a = "1 11 2 22 3 33 4 44 5 55"
print("a = ", a)

b = a.split()
print("b = ", b)

c = b[1::2]
print("c = ", c)

int_d = [int(x) for x in b]
d = [str(max(int_d)), str(min(int_d))]
print("d = ", d)

numbers = set()
for elem in a:
    if elem != ' ':
        numbers.add(int(elem))

e = str(sum(numbers))
print("e = ", e)

f = d
f.insert(1, e)
print("f = ", f)

g = ", ".join(f)
print("g = ", g)

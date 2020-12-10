fp = open("d8input.txt", "r")
txt = fp.read()
lines = txt.split("\n")
print("lines len: ", len(lines))
index_order = []

#llop through all lines and get an index order
i = 0
last_i = 100
while len(lines) > i:
    last_i = i
    print(i)
    x = lines[i]
    if x not in index_order:
        index_order.append(x)
    else:
        break
    if "jmp" in x:
        xs = x.split(" ")
        print(xs)
        if "+" in xs[1]:
            xss = xs[1].split("+")
            print(xss)
            i += int(xss[1])-1
        elif "-" in xs[1]:
            xss = xs[1].split("-")
            i -= int(xss[1])+1
    else:
        i += 1
    if last_i == i:
        break

print(index_order)
score = 0
for p in index_order:
    ps = p.split(" ")
    if "jmp" not in ps[0]:
        if "+" in ps[1]:
            xss = ps[1].split("+")
            print(xss)
            score += int(xss[1])
        elif "-" in ps[1]:
            xss = ps[1].split("-")
            score -= int(xss[1])

print("score is:", score)

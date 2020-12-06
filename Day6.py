fp = open("d6input.txt", "r")
count = 0
counts = []
group =  []
count_two = 0

def read_lines(txt):
    global group
    while True:
        buffer = txt.readline()
        if buffer != "\n":
            group.append(buffer.strip())
        if buffer == "\n":
            #check_count()
            check_count_part2()
            group = [] # wipe for the next group
        if buffer == "":
            #check_count()
            check_count_part2()
            break

def check_count():
    global count
    global group
    used = []
    for l in group:
        ll = l.lower()
        for char in ll:
            if char not in used:
                used.append(char)
    count += len(used)

def check_count_part2():
    global group
    global count_two
    print(group)
    gnum = len(group)
    letters = dict()
    if gnum == 1:
        # only 1 member in group so all count
        count_two += len(group[0])
        print('Gorup 0 with question length ', len(group[0]), group)
    else:
        # more then 1 in the group so work through them
        for l in group:
            if l == "":
                gnum -= 1
            for char in l:
                if char in letters :
                    letters[char] += 1
                else:
                    letters[char] = 1
        for k in letters.keys():
            if letters[k] == gnum:
                count_two += 1
# missed the last 2 off
#part 2 spare characters at the end of last group
#check_count()
read_lines(fp)
print(count)
print("Count 2 ", count_two)

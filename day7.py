import re
fp = open("d7input.txt", "r")

def read_lines(txt):
    global lines
    while True:
        line = txt.readline()
        make_bag_list(line)
        if line == "" or line == "\n":
            break

names = []
class bag:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains
        self.shiny_gold = False
        self.gold_trail = False
        self.gold_trail_trail = False
        self.gold_trail_trail_trail = False
        self.gold_trail_trail_trail_trail = False
        self.value = 0
        self.base = False

    def showParams(self):
        return self.name, self.contains

    def write_params(self):
        string = "name {},\n contains {}\n".format(self.name, self.contains)
        return string

    def can_hold_shiny_gold(self):
        for x in self.contains:
            if "shiny gold" in x:
                self.shiny_gold = True

    def trails(self):
        for n in names:
            for x in self.contains:
                if n in x:
                    self.gold_trail = True
    def trails_trails(self):
        for n in names:
            for x in self.contains:
                if n in x:
                    self.gold_trail_trail = True
    def trails_trails_trails(self):
        for n in names:
            for x in self.contains:
                if n in x:
                    self.gold_trail_trail_trail = True
    def trails_trails_trails_trails(self):
        for n in names:
            for x in self.contains:
                if n in x:
                    self.gold_trail_trail_trail_trail = True
    def is_base(self):
        for x in self.contains:
            if x.strip() == "no other":
                self.value = 1
                self.base = True

bag_list =[]
base_bags = []
def make_bag_list(l):
    global bag_list
    ls = l.split("contain")
    name = ls[0].split("bags")[0]
    contains = []
    if len(ls) > 1:
        lsc = ls[1].split(",")
        for b in lsc:
            contains.append(b.split('bag')[0])
    bag_list.append(bag(name, contains))

read_lines(fp)
for bag in bag_list:
    bag.can_hold_shiny_gold()
    if bag.shiny_gold:
        if bag.name not in names:
            names.append(bag.name)

for bag in bag_list:
    bag.trails()
    if bag.gold_trail:
        if bag.name not in names:
            names.append(bag.name)

for bag in bag_list:
    bag.trails_trails()
    if bag.gold_trail_trail:
        if bag.name not in names:
            names.append(bag.name)

for bag in bag_list:
    bag.trails_trails_trails()
    if bag.gold_trail_trail_trail:
        if bag.name not in names:
            names.append(bag.name)

for bag in bag_list:
    bag.trails_trails_trails_trails()
    if bag.gold_trail_trail_trail_trail:
        if bag.name not in names:
            names.append(bag.name)

# part 2
for bag in bag_list:
    bag.is_base()
    if bag.base:
        base_bags.append(bag)
shiny_level = []
level_1 = []
sums = 0
l = []
for bag in bag_list:
    if "shiny gold" in bag.name:
        shiny_level.append(bag)
        print(bag.showParams())
        for x in bag.contains:
            xr = re.sub(r'[^a-zA-Z ]+', '', x)
            l.append(xr.strip())
            xd = re.sub(r'[^0-9 ]+', '', x)
            sums += int(xd)
            print(xd)
            for bag2 in bag_list:
                if xr in bag.name:
                    level_1.append(bag2)
print(shiny_level)
print(level_1)
l2 = []
print(l)
for bag in bag_list:
    for ls in l:
        if ls in bag.name:
            for x in bag.contains:
                xr = re.sub(r'[^a-zA-Z ]+', '', x)
                l2.append(xr.strip())
                xd = re.sub(r'[^0-9 ]+', '', x)
                sums += int(xd)
                print(xd)
print("sums count", sums)
l3 = []
for bag in bag_list:
    for ls in l2:
        if ls in bag.name:
            for x in bag.contains:
                print(x)
                xr = re.sub(r'[^a-zA-Z ]+', '', x)
                l3.append(xr.strip())
                xd = re.sub(r'[^0-9 ]+', '', x)
                print(xd)
                if xr.strip() != "no other":
                    sums += int(xd)

l4 = []
for bag in bag_list:
    for ls in l3:
        if ls in bag.name:
            for x in bag.contains:
                xr = re.sub(r'[^a-zA-Z ]+', '', x)
                l4.append(xr.strip())
                xd = re.sub(r'[^0-9 ]+', '', x)
                if xr.strip() != "no other":
                    sums += int(xd)
# 4, 2 , 4 , 2 , 2, 3 , 2, 4, 2, 3, 5
print("Names Count ", len(names))
print("sums count", sums)
# 136 # 177

def write_to_file(name):
    f = open("day7part.txt", "a+")
    for bag in bag_list:
        if name in bag.name:
            params = bag.write_params()
            f.writelines(params)

write_to_file("dim plum")

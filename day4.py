import re

fp = open("d4input.txt", "r")

# read through each line untill we get to a blank line which is a new passport
# go through each line and check for required fields
# update counter.
# cid = False #optional so we don''t need to check it
def checkbyr(l):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if "byr" in l:
        x = l.split("byr:")
        y = x[1].split(" ")
        if len(y[0]) == 4 and 1920 <= int(y[0]) <= 2002:
            return True
    return False


def checkiyr(l):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if "iyr" in l:
        x = l.split("iyr:")
        y = x[1].split(" ")
        if len(y[0]) == 4 and 2010 <= int(y[0]) <= 2020:
            return True
    return False


def checkeyr(l):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if "eyr" in l:
        x = l.split("eyr:")
        y = x[1].split(" ")
        if len(y[0]) == 4 and 2020 <= int(y[0]) <= 2030:
            return True
    return False


def checkhgt(l):
    # hgt (Height) - a number followed by either cm or in:
    if "hgt" in l:
        x = l.split("hgt:")
        y = x[1].split(" ")
        if "cm" in y[0]:
            # If cm, the number must be at least 150 and at most 193.
            z = y[0].split("cm")
            if 150 <= int(z[0]) <= 193:
                return True
        if "in" in y[0]:
            # If in, the number must be at least 59 and at most 76.
            z = y[0].split("in")
            if 59 <= int(z[0]) <= 76:
                return True
    return False


def checkhcl(l):  # might need to check this
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if "hcl" in l:
        x = l.split("hcl:")
        y = x[1].split(" ")
        yy = y[0]
        z = re.sub('[^a-f0-9#]', '', yy)
        if len(z) == 7 and z[0] == "#":
            return True
    return False


def checkecl(l):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    el = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if "ecl" in l:
        x = l.split("ecl:")
        y = x[1].split(" ")
        z = y[0]
        if z in el:
            return True
    return False


def checkpid(l):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if "pid" in l:
        x = l.split("pid:")
        y = x[1].split(" ")
        z = y[0]
        if len(z) == 9:
            return True
    return False


valid = 0
passport = []


# read through each line add it to the passport lis until we get to blank line then check then pause to check the passport

def checkPassport():
    global valid
    global passport
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for l in passport:
        if not byr:
            byr = checkbyr(l)
        if not iyr:
            iyr = checkiyr(l)
        if not eyr:
            eyr = checkeyr(l)
        if not hgt:
            hgt = checkhgt(l)
        if not hcl:
            hcl = checkhcl(l)
        if not ecl:
            ecl = checkecl(l)
        if not pid:
            pid = checkpid(l)
    # print(byr,iyr,eyr, hgt, hcl, ecl, pid)
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1
    passport = []


def readLines(text):
    global passport
    while True:
        buffer = text.readline()
        if buffer != "\n":
            passport.append(buffer)
        if buffer == "\n":
            checkPassport()
        if buffer == "":
            checkPassport()
            break


# checkPassport()
readLines(fp)
print(valid)
print(passport)

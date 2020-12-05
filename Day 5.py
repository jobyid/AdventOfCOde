# lets start from the end
# part result is max seat id

id_list = [0]
fp = open("d5input.txt", "r")

def read_lines(txt):
    while True:
        buffer = txt.readline()
        find_row(buffer)
        if buffer == "":
            break

def find_row(ref):
    # F means to take the lower half
    # B means to take the upper half
    colref = ""
    row = 0
    range = 128
    max_row = 127
    min_row = 0
    for char in ref:
        i = ref.index(char)
        if i < 7:
            range /= 2
            if char == "F":
                max_row = min_row + range - 1

            else:
                min_row = max_row - range + 1

            if min_row == max_row:
                row = min_row
        else:
            colref += char
    find_col(colref, row)

def find_col(colref, row):
    # R means to take the upper half
    # L means to take the lower half
    min_col = 0
    max_col = 7
    range = 8
    col = 0
    for char in colref:
        range /= 2
        if char == "R":
            min_col = max_col - range + 1
        else:
            max_col = min_col + range - 1

        if min_col == max_col:
            col = min_col
    seat_id(row, col)

def seat_id(row,col):
    # seat ID: multiply the row by 8, then add the column
    global id_list
    id = row * 8 + col
    #if id > max(id_list):
    id_list.append(id)

def find_my_seat():
    id_list_sorted = sorted(id_list)
    # print(id_list_sorted)
    idl = []
    for id in id_list_sorted:
        i = id_list_sorted.index(id) + 1
        if i < len(id_list_sorted) -1:
            if id_list_sorted[i] != (id + 1):
                idl.append(id + 1)
    print("idl",idl, "my Seat", max(idl))



read_lines(fp)
#print(id_list, "max", max(id_list))
find_my_seat()

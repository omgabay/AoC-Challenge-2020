def parseEncodingToBinary(encoding,replace_dict):
    for old_char, new_char in replace_dict.items():
        #print(old_char, new_char)        
        encoding = encoding.replace(old_char,new_char)

    encoding = encoding[::-1]  # flip string
    num = 0 
    for i in range(len(encoding)):
        digit = int(encoding[i])
        num += digit * 2 ** i 
  
    return num 



'''
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
'''

with open("day5_input.txt", 'r',  encoding="utf-8") as file:
    row_dict = {"F": "0", "B": "1"}
    seat_dict = {"L": "0", "R": "1"}
    sample = ["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"] 
    max_seat = 0 
    seat_id_lst = [] 
    for line in file.readlines():
        line = line.strip()
        row_code = line[:7]
        seat_code = line[7:]
    
        row = parseEncodingToBinary(row_code, row_dict)
        seat = parseEncodingToBinary(seat_code, seat_dict)
        seat_id = 8*row + seat 

        seat_id_lst.append(seat_id)
        # if seat_id > max_seat: 
        #     max_seat = seat_id  
        #     print(f'row {row} seat {seat} seat id {seat_id}')


    seat_id_lst.sort()
    prev = -100 
    for i, id in enumerate(seat_id_lst):
        if id == prev +2:
            print(seat_id_lst[i-1],id-1,id) 
        prev = id     




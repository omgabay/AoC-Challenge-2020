history = set()
accumulator = 0 
loop = [0,1,2,3,8,9,427,428,429,430,431,306,307,371,372,373,374,375,466,331,332,333,310,311,312,313,314,250,251,252,253,381,382,383,384,238,239,591,592,593,594,595,165,275,276,181,338,339,340,259,260,261,262,263,550,551,552,553,554,572,573,574,575,576,436,437,438,473,474,475,476,477,366,367,368,369,292,293,294,295,545,546,285,190,78,79,80,81,498,499,500,501,132,530,468,469,425,326,327,105,106,107,108,458,582,193,194,195,196,152,153,154,411,208,209,509,168,169,170,171,172,360,361,362,363,201,202,203,204,534,535,536,537,483,484,485,486,487,215,216,217,377,378,379,449,450,451,452,219,220,221,316,317,318,319,320,539,540,541,542,566,68,69,70,71,120,121,122,123,117,118,184,185,186,187,398,505,522,281,83,84,85,86,87,50,51,52,53,349,350,39,40,41,42,559,560,561,562,563,416,417,418,419,306]

with open("./day8/day8_input.txt", 'r',  encoding="utf-8") as file:
    code = file.readlines()
    for line in loop:
        command = code[line].strip()
        opcode, value = command.split()
        if opcode == "acc":
            print(f'line {line} was skipped- {opcode} {value}')
            continue
        accumulator = 0 
        history.clear()
        i = 0 
        while i < len(code):
            command = code[i].strip()
            opcode, value = command.split()  
            value = int(value)
            history.add(i)
            if i == line: 
                opcode = 'jmp' if opcode == 'nop' else 'nop'
                print(f'replacement occured on line {i}/{len(code)}')
            if opcode == 'jmp':
                i += value             
                if i in history: 
                    break                 
            elif opcode == 'acc': 
                accumulator += value
                i += 1   
            else: 
                i += 1    

        if i == len(code): 
            print(line, code[line].strip())
            print(f'accumulator value {accumulator}')
            print(f'finished execution on line {i}/{len(code)}')    
            break
       






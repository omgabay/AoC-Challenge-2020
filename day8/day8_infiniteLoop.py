history = set()
accumulator = 0 
with open("./day8/day8_input.txt", 'r',  encoding="utf-8") as file:
    code = file.readlines()
    line = 0 
    print('hello world')
    while line < len(code): 
        command = code[line].strip()
        opcode, value = command.split()        
        value = int(value)
        history.add(line)
        if opcode == 'jmp':
            line += value             
            if line in history: 
                print(f'{line}')
                break 
            continue
        elif opcode == 'acc': 
            accumulator += value     

        line += 1   
        print(line, sep='==>')




print(f'final value of accumulator - {accumulator}')    

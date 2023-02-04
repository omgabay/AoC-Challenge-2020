history = set()
accumulator = 0 
with open("./day8/day8_input.txt", 'r',  encoding="utf-8") as file:
    code = file.readlines()
    line = 0 
    while line < len(code): 
        if line in history:
            print(f'{line}')
            break 
        else:
            print(line, end=",")
        command = code[line].strip()
        opcode, value = command.split()        
        value = int(value)
        history.add(line)
        if opcode == 'jmp':
            line += value 
        else:
            line += 1               
           
        if opcode == 'acc': 
            accumulator += value


      
    




print(f'final value of accumulator - {accumulator}')    

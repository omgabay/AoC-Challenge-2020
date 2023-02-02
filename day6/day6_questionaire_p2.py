import string 
total_answers = 0 
answers = list(string.ascii_lowercase)
with open("./day6/day6_input.txt", 'r',  encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        # check if line is empty 
        if len(line) == 0: 
            total_answers += len(answers)
            print(answers)
            answers = list(string.ascii_lowercase)
            continue
        
        answers = [ans for ans in answers if ans in line]
            

    print(f'total = {total_answers}')        

        

        
        

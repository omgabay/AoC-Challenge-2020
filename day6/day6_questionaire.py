total_answers = 0 
answers = set() 
with open("./day6/day6_input.txt", 'r',  encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        # check if line is empty 
        if len(line) == 0: 
            total_answers += len(answers)
            print(answers)
            answers.clear()
            continue
        response = line 
        for selection in response: 
            if selection.isalpha():
                answers.add(selection)
    print(f'total = {total_answers}')        

        

        
        

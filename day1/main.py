expenses = set()
two_sums = {}
with open("expenses.txt", 'r', encoding="utf-8") as file:
    for line in file.readlines():
        c = int(line.strip())
        if c < 2020 and c not in expenses:
            complement = 2020 - c 
            if complement in two_sums:
                a,b = two_sums[complement]
                print(f'{a}*{b}*{c} = {a*b*c}')
                break
            for expense in expenses: 
                two_sum = expense + c 
                if two_sum not in two_sums and two_sum <= 2020:
                    two_sums[two_sum] = [expense, c]     
            expenses.add(c) 


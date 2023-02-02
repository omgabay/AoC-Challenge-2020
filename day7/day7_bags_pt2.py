from collections import namedtuple
Bag = namedtuple('Bag', 'name count')
bags = {}

def countBags(bags, bag_name):
    bag_count = 1
    for bag in bags[bag_name]: 
        bag_count += bag.count*countBags(bags, bag.name)
    return bag_count         


with open("./day7/day7_input.txt", 'r',  encoding="utf-8") as file:
    for i,line in enumerate(file.readlines()):
        # read line and remove period at eol 
        line = line.strip().strip(".")   
        # get bag's name and what it contains 
        bag_name,match,inside = line.partition("contain")
        if len(match) == 0:
            continue
        bag_name = " ".join([word for word in bag_name.split() if word not in "bags"] + ["bag"])
        
        if bag_name not in bags: 
            bags[bag_name] = [] 

        # if the bag must not contain any other bag, continue      
        if inside.strip() == "no other bags":
            continue
        for allowed_bag in inside.split(","):  
            bag_count = int(allowed_bag.split()[0])         
            bag_inside = " ".join([word for word in allowed_bag.split() if word not in "bags" and not word.isnumeric()] + ["bag"])
            bags[bag_name].append(Bag(bag_inside, bag_count))



print(f'shiny gold bag must contain {countBags(bags, "shiny gold bag")-1} bags')





bags = {}
def depthFirstSearch(tree, curr_node,to_find):    
    if curr_node == to_find: 
        return True 
    if curr_node not in tree: 
        return False     
    for node in tree[curr_node]:   
        if depthFirstSearch(tree,node,to_find):
            return True
    return False 


with open("./day7/day7_input.txt", 'r',  encoding="utf-8") as file:
    for i,line in enumerate(file.readlines()):
        line = line.strip().strip(".")    
        bag_name,match,inside_bag = line.partition("contain")
        bag_name = " ".join([word for word in bag_name.split() if word not in "bags"] + ["bag"])
        if len(match) == 0:
            continue
        if bag_name not in bags: 
            bags[bag_name] = [] 
        
        for allowed_bag in inside_bag.split(","):            
            bag_inside = " ".join([word for word in allowed_bag.split() if word not in "bags" and not word.isnumeric()] + ["bag"])
            bags[bag_name].append(bag_inside)
count = 1 
with open("./day7/day7_input.txt", 'r',  encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip().strip(".")  
        bag_name,match,_ = line.partition("contain")
        if len(match) == 0:
            continue
        bag_name = " ".join([word for word in bag_name.split() if word not in "bags"] + ["bag"])
        if bag_name == "shiny gold bag":
            continue
        if depthFirstSearch(bags,bag_name,"shiny gold bag"):
            print(f'{count}){bag_name}: {bags[bag_name]}')
            count += 1 




       
            

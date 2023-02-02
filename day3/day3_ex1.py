LINE_LENGTH = 31 
#LINE_LENGTH = 66
#output = open("day3_output.txt", "w", encoding="utf-8")


def count_trees(delta_x: int, delta_y: int):
    lines_to_skip = 0
    trees = 0
    with open("ski_map.txt", 'r',  encoding="utf-8") as file:
        x_position = 0
        for line in file.readlines():
            if lines_to_skip == 0:
                if line[x_position] == '#':
                    trees += 1
                # calculate the next position    
                x_position = (x_position + delta_x) % LINE_LENGTH     
                lines_to_skip = delta_y
            lines_to_skip -= 1  

    return trees          
            #output.write(f"{line[:x_position]}X{line[x_position+1:]}")
            # else: 
            #     output.write(f"{line[:x_position]}O{line[x_position+1:]}")
         
                

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
total_trees = 1
for delta_x,delta_y in slopes: 
    total_trees *= count_trees(delta_x, delta_y)
    print(count_trees(delta_x, delta_y))



print('number of trees in our path:',total_trees)   


def scanner(file_path):
    result = 0
    
    # read the file
    with open(file_path, 'r') as file:

        lines = file.readlines()
    
   
    # get a full number

    # get the index to be checked

    get_number_data(lines)

    # check if there is any adjacent symbol 

    # if yes, sum up


    return result


# returns the number found and the index to be checked if there is a symbol
def get_number_data(lines):
    number_index_list = []
    row = 0
    column = 0

    # look for a number
    for line in lines:
        while(column<len(line)-1):
            char = line[column]

            # get a full number
            if char.isnumeric():
                number = ""
                index = []
                while(char.isnumeric()):
                    number = number + char
                    index.append([column, row])
                    column = column + 1
                    char = line[column]

                number_index_list.append([number, index])
                
            print("a")
            column = column + 1

    
    print(number_index_list)
    
        
# get all the adjacent indices
def get_adjacent_index(index):
    movement_list = [[-1,0], [1,0], [-1,-1], [-1, 1], [0,-1], [0,1], [1,1], [1,-1]]
    adjacent_indices = []
    for movement in movement_list:
        adjacent_indices.append(movement + index)

    print(adjacent_indices)
    return adjacent_indices







if __name__ == "__main__":

    file_name = "test.txt"

    result = scanner(file_name)
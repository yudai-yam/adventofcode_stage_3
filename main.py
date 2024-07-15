def scanner(file_path):
    result = 0
    
    # read the file
    with open(file_path, 'r') as file:

        lines = file.readlines()
    

####################### part 1 ##################################
   
    # get a full number and its index
    #number_index_list = get_number_data(lines)
    #number_adj_index_list = []

    ## get its adjacent index
    #for number_index in number_index_list:
        #index_list = number_index[1]
        #adjacent_index_list = []
        #for index in index_list:
            #adjacent_index_list.append(get_adjacent_index(index))

        #number_adj_index_list.append([number_index[0], adjacent_index_list])

    

    #result = 0

    ## check if there is a simbol in the adjacent index
    #for num_adj_ind in number_adj_index_list:
        ## if there is at least one simbol -> preserve the number -> use it for the last calculation
        #symbol_exists = False
        #for adj_ind in num_adj_ind[1]:
            #for adj_ind_each in adj_ind:
                #col, row = adj_ind_each[1], adj_ind_each[0]
                #if 0< col < len(lines[0]) - 1 and 0 < row < len(lines) - 1:
                    #if isSimbol(lines[col][row]):
                        #symbol_exists = True
            
        #if symbol_exists:
            #result = result + int(num_adj_ind[0])   

############# part 2 ############################################
    # get star and its index
    star_index_list = get_star_index(lines)

    # check if there are two adjacent numbers

    star_adj_index_list = []
    for star_index in star_index_list:
       star_adj_index_list.append(get_adjacent_index(star_index)) 
    
    print(star_adj_index_list)
    number_index_list = get_number_data(lines)
    result = 0

    for each in star_adj_index_list:
        number_count = 0 # if 2, multiply
        temp_numbers = []
        for star_adj_index in each:
            
            # check if there is a number
            for number_data in number_index_list:
                if star_adj_index in number_data[1] and number_data[0] not in temp_numbers:
                    number_count = number_count + 1 
                    temp_numbers.append(number_data[0])
                    print(temp_numbers)
        print(number_count)
        if number_count == 2:
            temp = int(temp_numbers[0]) * int(temp_numbers[1])
            result = result + temp

    return result


def isSimbol(char):
    if char != '.' and not char.isnumeric():
        return True
    else:
        return False


def isStar(char):
    if char == '*':
        return True
    else:
        return False




# returns the number found and the index to be checked if there is a symbol
def get_number_data(lines):
    number_index_list = []
    row = 0
    # look for a number
    for line in lines:
        column = 0
        while(column<len(line)-1):
            char = line[column] 


            # get a full number and its index
            if char.isnumeric():
                number = ""
                index = []
                while(char.isnumeric()):
                    number = number + char
                    index.append([column, row])
                    column = column + 1
                    char = line[column]

                number_index_list.append([number, index])

            column = column + 1
        row = row + 1

    return number_index_list


    
        
# get all the adjacent indices
def get_adjacent_index(index):

    movement_list = [[-1,0], [1,0], [-1,-1], [-1, 1], [0,-1], [0,1], [1,1], [1,-1]]
    adjacent_indices = []
    for movement in movement_list:
        adjacent_indices.append([index[0] + movement[0], index[1] + movement[1]])
   
    return adjacent_indices



def get_star_index(lines):
    star_index_list = []
    row = 0
    # look for a number
    for line in lines:
        column = 0
        for char in line:
            if isStar(char):
                star_index_list.append([column, row])
            
            column = column + 1
        
        row = row + 1
    
    print(star_index_list)

    return star_index_list







if __name__ == "__main__":

    file_name = "input.txt"

    result = scanner(file_name)

    print(result)
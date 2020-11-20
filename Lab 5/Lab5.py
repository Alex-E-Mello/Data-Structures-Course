def sum(num):
    #base case
    if num == 1:
        print("Base case: returns 1")
        return 1
    #0 input
    if num == 0:
        return 0
    #negative input
    if num < 0:
        return "Only calculates the sum of positive integers"
    
    #recursive call
    if num > 0:
        returned_value = sum(num-1) + num

        #print step
        print("sum(" + str(num - 1) + ") + " + str(num))

        #return value
        return returned_value


def fibonacci(number):
    #base case
    if number == 0:
        return 0
    #base case
    if number == 1:
        return 1
    
    #recursive call
    if number > 1:
        return fibonacci(number - 1) + fibonacci(number-2)
        


def largest(data):
    #base case
    if len(data) == 1:
        print("Base case: returns first number (" + str(data[0]) + ")")
        return data[0]
    
    #recursive call
    else:
        #end index
        end = len(data)-1
        
        #creates spliced list
        next_list = data[0:end]
        
        #recursive call on spliced list
        #saves the return value as returned_value
        returned_value = largest(next_list)

        #print step
        print("Compares " + str(returned_value) + " and " + str(data[end]))

        #if list is larger than 1 item
        #compares the previous largest item to the next item in list
        if data[end] >= returned_value:
            return data[end]
        else:
            return returned_value
            

def countCannonballs(height):
    #base case
    if height == 1:
        print("Base case: returns 1")
        return 1
    #incorrect input
    if height < 1:
        return "The height must be positive"
    #recursive call
    if height > 1:
        returned_value = countCannonballs(height-1) + (height * height)

        #value to print
        print_value = returned_value - (height * height)
        print("Adds " + str(print_value) + " and " + str(height*height) + " (" + str(height)+ "*" + str(height) + ")")

        #return value
        return returned_value




import sys, traceback

####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
###
###
### Type your name here: Alex Mello
###
##
## Look at the function main below to see how these functions are used
##
##
## Complete the functions below as directed in the docstring comments
##
##
## I will test your code by running the main function defined below.
##
##Obviously, as you write each function, you can test it individually
##using the Python shell
##
##


#complete

def initialize_portfolio(filename): #20 points
    """
    read the data contained in the named file
    and return a *list of tuples* representing the data
    For example: [('DD', 1085),('DIS', 1213), ('GE', 1781), ('GS',1913),......]
    """

    #opens file
    #makes empty list for tuples
    
    file = open(filename, "r")
    list_tuples = []

    #each line in file
    #strips end of line
    #splits line by comma
    #makes tuples from the split list
    #appends tuple to the list
    
    for line in file:
        line = line.strip()
        line = line.split(",")
        tuples = (line[0],line[1])
        list_tuples.append(tuples)

    #returns list of tuples
        
    return list_tuples



##EXTRA FUNCTION
#makes a list of lists instead of list of tuples

def initialize_portfolio_lists(filename):
    """
    read the data contained in the named file
    and return a *list of lists* representing the data
    """

    #opens file
    #makes empty list for lists
    
    file = open(filename, "r")
    list_lists = []

    #each line in file
    #strips end of line
    #splits line by comma
    #makes lists from the split list
    #appends lists to the list
    
    for line in file:
        line = line.strip()
        line = line.split(",")
        lists = [line[0],line[1]]
        list_lists.append(lists)

    #returns list of lists
        
    return list_lists
    

#complete

def print_portfolio(portfolio):  #20 points
    """
    Print the contents of the portfolio in a two-column format as shown below
    The first line is a header
    All the other lines show a stock symbol, and the number of shares
    held of that stock, with a tab "\t" character separating the two,
    like this:
    Symbol    Amount
    DIS       1213
    GE        1781
    GS        1913
    .....
    This function does not return anything
    """

    #prints symbol and amount
    #has tab in own quotations to fix spacing
    
    print("Symbol","\t","Amount")

    #runs initialize_portfolio
    #saves the list_tuples from function to list_tuples
    #starts index
    
    list_tuples = initialize_portfolio("holdings.txt")
    index = 0

    #for each tuple in tuple list
    #if index is less than length of list
    #prints list[index][0] tab list[index][1]
    #increases index
    
    for tuples in list_tuples:
        if index < len(list_tuples):
            print(list_tuples[index][0],"\t",list_tuples[index][1])
            index = index + 1
    
    pass


#complete

def total_shares(portfolio): #20 points
    """
    return the total number of shares owned (across all stocks) in the portfolio
    """

    #runs initialize_portfolio
    #saves the list_tuples from function to list_tuples
    #starts index
    #starts total
    
    list_tuples = initialize_portfolio("holdings.txt")
    index = 0
    total = 0

    #for each tuple in tuple list
    #if index is less than length of list
    #total is increased by list[index][1]
    #increases index
    
    for tuples in list_tuples:
        if index < len(list_tuples):
            total = total + int(list_tuples[index][1])
            index = index + 1

    #returns total
    
    return total


#complete

def find_amount(portfolio, stock_symbol): #20 points
    """
    return the number of shares of the specified stock in the portfolio
    for example, find_amount(portfolio, "DIS") returns 1213
    """

    #runs initialize_portfolio
    #saves the list_tuples from function to list_tuples
    #starts index
    #starts amount
    
    list_tuples = initialize_portfolio("holdings.txt")
    index = 0
    amount = 0

    #for each tuple in tuple list
    #if index is less than length of list
    #checks if list[index][0] == stock symbol
    #if it is changes amount to list[index][1]
    #increases index whether it matches or not
    
    for tuples in list_tuples:
        if index < len(list_tuples):
            if list_tuples[index][0] == stock_symbol:
                amount = list_tuples[index][1]

                #return amount inside if
                #if it finds amount it doesnt continue
                return amount
            
            index = index + 1

    #returns amount
    #returns 0 if it cannot find amount
    
    return amount


def update_portfolio(portfolio, filename): # 20 points
    """
    Open the specified file, read the transactions in it,
    and update the portfolio accordingly
    Return the updated portfolio
    """
    
    file = open(filename, "r")
    trades = []

    for line in file:
        line = line.strip()
        line = line.split(",")
        lists = [line[0],line[1],line[2]]
        trades.append(lists)

    #runs initialize_portfolio_lists
    #saves the list_lists from function to datalist
    #starts index1 and index2

    datalist = initialize_portfolio_lists("holdings.txt")

    #goes through numbers for range of len trades
    #goes through numbers for range of len datalist
    for trade in range(len(trades)):            
        for data in range(len(datalist)):

            #if datalist[0-?][0] equals trades[0-?][1]
            #checks if it's buy or sell
            #adds or subtracts accordingly
            if datalist[data][0] == trades[trade][1]:
                if trades[trade][0] == "Buy":
                    datalist[data][1] = int(datalist[data][1]) - int(trades[trade][2])

                if trades[trade][0] == "Sell":
                    datalist[data][1] = int(datalist[data][1]) + int(trades[trade][2])

    #returns a list of the datalist
    return datalist



#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
def main():
    try:
        portfolio = initialize_portfolio("holdings.txt")
    except:
        print(">>>>>>>> initialize_portfolio has errors")
        traceback.print_exc()

    print("\nHere is your portfolio before any trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
        traceback.print_exc()
        
    try:
        print("\nThe total number of shares in the portfolio is ", total_shares(portfolio))
    except:
        print(">>>>>>>> total_shares has errors")
        traceback.print_exc()
        
    symbol = input("\nEnter a stock symbol(like IBM): ")

    try:
        print("\nBefore any trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>> find_amount has errors")
        traceback.print_exc()

    try:
        portfolio = update_portfolio(portfolio, "trades.txt")
    except:
        print(">>>>>>>> update_portfolio has errors")
        traceback.print_exc()
        
    print("\nHere is your portfolio after trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
        traceback.print_exc()
    
    symbol = input("\nEnter a stock symbol(like IBM): ")
    
    try:
        print("\nAfter trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>>> find_amount has errors")
        traceback.print_exc()


#Run the main function     
main()

#Alex Mello
#9/11/2019

#ALGORITHM

#print welcome

#find input name and output names
#open the input file
#find the placeholders
#get input to change the placeholders
#replace placeholders with input
#write the result to the output file

#setup a system for asking to repeat
#ask to repeat after madlib is complete

#sources
#used to clear the output file
#https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python

#used to remove "-" from the placeholders
#https://www.programiz.com/python-programming/methods/built-in/slice
#https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string-in-python


#most of the program in this function
def body():
    """Contains the main instructions for the program"""
    
    #initializes True
    #makes list for list of lines
    #makes list for the result lines
    again = True
    lines = []
    result_lines = []
    
    

    #while again is True
    while again == True:

        #saves variable for  file name
        filename = input("Input file name: ")

        #tries to open file
        try:
            file = open(filename, "r")
            
        #asks for file name if it doesn't open
        #tries to open again
        except:
            filename = input("File not found. Try again: ")
            file = open(filename, "r")
            
        #gets name for output file
        #prints empty line
        result_file = input("Output file name: ")
        print("")

        #strips end of lines
        #splits line by spaces
        #appends list of each line to the lines list
        file.seek(0)
        for line in file:
            line = line.strip()
            line = line.split()
            lines.append(line)

        #goes through each line
        #resets the temp words
        for line in lines:
            temp_words = ""

            #goes through each word
            for word in line:

                #if word isnt a placeholder
                #adds to temp words
                if word[0] != "<":
                    temp_words = temp_words + word + " "

                #if word could be a placeholder
                else:
                    if word[len(word)-1] == ">":
                                                
                        #if the word starts with <
                        #splits word of < and >
                        #starts counter
                        if word[0] == "<":
                            word = word.strip("<")
                            word = word.strip(">")
                            counter = 0

                            #changes - to a space
                            for char in word:
                                if word[counter] == "-":
                                    word = word[:counter] + " " + word[counter+1:]
                                    counter = counter + 1
                                else:
                                    counter = counter + 1
                                

                            #if word_type starts with a vowel
                            #uses an
                            if word[0] == "a" or word[0] =="e" or word[0] =="i" or word[0] =="o" or word[0] =="u" or word[0] =="A" or word[0] =="E" \
                               or word[0] =="I" or word[0] =="O" or word[0] =="U":
                                
                                replacement = input("Please type an " + word + ": ")
                                temp_words = temp_words + replacement + " "

                            #else
                            #uses a
                            else:
                                replacement = input("Please type a " + word + ": ")
                                temp_words = temp_words + replacement + " "

                                
            #adds result words to result list     
            result_lines.append(temp_words)

        #opens file
        #creats file if it doesn't exist
        output = open(result_file, "w+")

        #goes to start of file
        #clears the file
        output.seek(0)
        output.truncate()

        #for each line in file
        result_counter = 0
        for each in result_lines:
            output.write(result_lines[result_counter] + '\n')
            result_counter = result_counter + 1

        #closes file
        output.close()
        
        print("\nYour MadLib story has been created.")

        #finds out whether to print or not
        #prints or not based on input
        should_print = input("\nDo you want to see the resulting story? (Y|N) ")
        if should_print == "Y" or  should_print == "y":
            result_print = ""
            for each in result_lines:
                result_print = result_print + each
            print("")
            print(result_print)
            print("")
                        
        #asks to repeat or not
        again = repeat()

        #try to reset function
        file.close()
        result_lines = []
        lines = []
        line = ""
        filename = ""
        result_file = ""

        #worked :)


#prints welcome
def welcome():
    """Prints the welcome"""
    
    print("Welcome to the game of Mad Libs.")
    print("I will ask you to provide several words and phrases to fill in a mad lib story.The result will be written to an output file.\n")

#asks to repeat or not
#returns value
def repeat():
    """Finds out whether to repeat or not. Returns True or False relating to continue or not."""
    
    value = input("Do you want to process another Mad Lib? (Y|N) ")
    print("")

    if value == "N" or value == "n":
        again = False

    if value == "Y" or value == "y":
        again = True

    return again

#prints welcome
#runs body function function
def main():
    """Calls the welcome and body functions."""
    welcome()
    body()

#calls main function
main()


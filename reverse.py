#takes an input of a string
def reverse(words):
    #turns the input into a list
    words = list(words)
    #sets the output to a reverse of the string itself using slicing
    output = list(words[::-1])
    #prints the output
    print (output)
#srts up the program for command line arguments
if __name__ == "__main__":
    # imports system for commandline
    import sys
    #program is call usuing arguments that stop when the user stops entering infor but starts at index 1
    reverse(sys.argv[1:])

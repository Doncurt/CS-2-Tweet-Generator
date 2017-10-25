import random #imports the random class
#list object that stores quotes, separated by commas
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")
#rand_index variable used to randomly select a place in the tuple and based on index, print out the line
def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]
#this makes sire that the file can be stored in a module that can access just the parts that are needed
#otherwise the entre script runs any time its called
if __name__ == '__main__':
    quote = random_python_quote()
    print (quote)
# you can use the import fucntion later in another program to have access to all of the information

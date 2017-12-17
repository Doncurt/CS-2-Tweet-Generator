from dictogram import Dictogram
import stochsample
from random import randint



def dictogram_markov(text_string):

    data = text_string.split()
    dictogram = {}

    for position in range(len(data) - 1):
        word = data[position]
        next_word = data[position + 1]

        if word in dictogram:
            dictogram[word].add_count(next_word)
        else:
            dictogram[word] = Dictogram([next_word])

    return(dictogram)



def markov_sample(dictogram):
    return stochsample.weight_sampling(dictogram)


def markov_chain(dictogram):
    #updated to handle the 2nd order markov chain correctly now that Im settled into a new apartment

    #gets a list of keys from the corpus by way of the dictogram class
    keys = [k for k, v in dictogram.items()]
    #takes a random word based on its position in the keys and sets it as the word that starts the chain
    output = [keys[randint(0, len(keys) - 1)]]
    #
    for position in range(10):
        word= dictogram[output[position]]
        next_word = markov_sample(word)
        output.append(next_word)

    return ' '.join(output)

def nth_order_markov_dictograms(text_string, nth_order):
    data = text_string.split()
    dictogram = {}

    for position in range(len(data) - nth_order):

        current_tuple = tuple((data[index]) for index in range(position, position + nth_order))
        next_word = data[position + nth_order]

        if current_tuple in dictogram:
            dictogram[current_tuple].add_count(next_word)
        else:
            dictogram[current_tuple] = Dictogram([next_word])

    return(dictogram)
def nth_order_markov(dictogram):
    # this class was the bane of my existance
    keys = [k for k, v in dictogram.items()]
    output = list(keys[randint(0, len(keys) - 1)])

    nth_order_stop = len(output)

    for position in range(15):
        #finds the key tuple based on the length
        key_tuple = tuple((output[index]) for index in range(position, position + nth_order_stop))
        # if the tuple is in the dictogram it adds it to the output
        if key_tuple in dictogram:
            word = dictogram[key_tuple]
            next_word = markov_sample(word)
            output.append(next_word)
            #if it isnt, jsut top the entore function from running at this point
        else:
            break

    return ' '.join(output)

if __name__ == "__main__":
    test = 'one fish two fish red fish blue fish'
    markov_test = dictogram_markov(test)
    #print(markov_test)
    print(markov_chain(markov_test))

    

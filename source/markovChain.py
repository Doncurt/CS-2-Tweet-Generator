from dictogram import Dictogram
import sample
from random import randint



def dictogram_markov(text_string):
    #was running into issues
    data = text_string
    #splits data into a string
    data = data.split()

    #initiallized empty dictogram
    dictogram = {}
    #based on the position of the word it scans through the text given and sets the word that is the focus of that part of the markov chain and assigns the next value
    for position in range(len(data) - 1):
        word = data[position]
        next_word = data[position + 1]

        #if the word is in the dictogram then nextword is incremented in the next interation
        if word in dictogram:
            dictogram[word].add_count(next_word)
        else:
            dictogram[word] = Dictogram([next_word])

    return(dictogram)


def markov_sample(dictogram):
    return sample.weighted_dict_sampling(dictogram)


def markov_chain(dictogram_):

    output = ['red']
    for word_pos in range(15):
        next_word = markov_sample(dictogram[output[word_pos]])
        output.append(next_word)


    #text_string
    #print(' '.join(output))
    #accurate and works as of nove 13th
    return ' '.join(output)


if __name__ == "__main__":
    test = 'one fish two fish red fish blue fish'
    fish_markov = markov_dictograms(fish_text)
    print(markov_chain(fish_markov_dictionary))

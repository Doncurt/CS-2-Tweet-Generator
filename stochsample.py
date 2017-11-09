import histogram
import random

'''
Sampling the dictionary based on the relative frequency of the word in the text( which was transfered into a dictionary and will be imported at the top)

'''
def weight_sampling(histogram):
    words_sample_list = [word for word in histogram]
    #testing for words
    print(words_sample_list)
    token_count = 0
    for sample in words_sample_list:
        token_count += histogram[sample]

    randval = random.randint(0, token_count - 1)

    for k, v in histogram.items():
        frequency = v

        while frequency >= 0:
            if randval > 0:
                randval -= 1
                frequency -= 1
            else:
                return k

if __name__== "__main__":
    import sys
    

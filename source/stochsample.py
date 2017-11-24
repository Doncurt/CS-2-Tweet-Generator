import histogram
import random

'''
Sampling the dictionary based on the relative frequency of the word in the text( which was transfered into a dictionary and will be imported at the top)

'''

def weight_sampling(histogram):
    #testing for words
    #print(words_sample_list)
    token_count = 0
    for word, freq in histogram.items():
        token_count += freq

    randval = random.randint(0, token_count - 1)

    for k, v in histogram.items():
        frequency = v

        while frequency > 0:
            if randval > 0:
                randval -= 1
                frequency -= 1
            else:
                return k
'''
runs the test for the stocastic sampling and returns both the expected values as well as the frequency in which they should occur
after testing it prints all of the expected values and therefore can handle hiigher numbers of text files being fed to it
'''

def test_weight_sampling():
    red_count=0
    two_count=0
    one_count=0
    blue_count=0
    fish_count=0
    for i in range(10000):
        sample = weight_sampling(histogram.histo)

        if sample =="one":
            one_count+=1

        if sample =="two":
            two_count+=1

        if sample =="blue":
            blue_count+=1

        if sample =="red":
            red_count+=1

        if sample =="fish":
            fish_count+=1

    print(one_count, ' ', two_count, ' ', red_count, ' ', blue_count , ' ', fish_count )
if __name__ == "__main__":
    import sys

    test_weight_sampling();
    print(weight_sampling(histogram.histo))

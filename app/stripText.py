from string import punctuation

class Clean():
    '''Will clean the text of all whitespace, punctuation, as well as tabs, indents and the like'''



    def __init__(self):
        '''only needed to actually make the class run as needed'''
        pass

    def strip(self, text_file):
        ''' Removes all punctuation, and escapt cahrs from the text in question'''
        with open(text_file, 'r') as olafText:
            data = olafText.read()
        word_output = ''.join(data)
        word_output = ''.join(word for word in word_output if word not in punctuation)
        return word_output

    def listify(self, word_output):
        """ Seperate string into word list """
        word_list = word_output.split()
        return word_list

    def cleaner(self, file):
        word_output = self.strip(text_file)
        word_list = self.listify(word_output)
        return word_list

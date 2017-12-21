'''from string import punctuation

class Cleaner():
    """Will clean the text of all whitespace, punctuation, as well as tabs, indents and the like"""



    def __init__(self):
        """only needed to actually make the class run as needed"""
        pass

    def strip(self, text_file):
        """ Removes all punctuation, and escapt cahrs from the text in question"""
        with open(text_file, 'r') as olafText:
            data = olafText.read()
        word_output = ''.join(data)
        word_output = ''.join(word for word in word_output if word not in punctuation)
        return word_output

    def listify(self, word_output):
        """ Seperate string into word list """
        word_list = word_output.split()
        return word_list

    def clean(self, text_file):
        word_output = self.strip(text_file)
        word_list = self.listify(word_output)
        return word_list
'''
from string import punctuation

class Clean():
    """ Returns a list of single words """

    def __init__(self):
        pass

    def _remove_punctuation(self, file_name):
        """ Remove all punctuation from text file """
        with open(file_name, 'r') as myfile:
            dialouge_list = myfile.read()
        long_string = ''.join(dialouge_list)
        long_string = ''.join(c for c in long_string if c not in punctuation)
        return long_string

    def _single_words(self, long_string):
        """ Seperate string into word list """
        word_list = long_string.split()
        return word_list

    def clean_text(self, file_name):
        long_string = self._remove_punctuation(file_name)
        word_list = self._single_words(long_string)
        return word_list

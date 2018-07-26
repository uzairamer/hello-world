import re
from collections import defaultdict


class WordAnalysis(object):
    """WordAnalysis consists of static methods that helps in word analysis
    like checking frequency of each word in a file etc
    """

    def __pretty_print_word_frequency(input_dict):
        """Private Method: Prints the word and its count in a pretty format

        Arguments:
            input_dict(dict): input dictionary with key as word and value as count

        Returns:
            VOID
        """
        print("Word\t\t\tFrequency")
        print("{:-^{}}".format('', 28))
        for key in input_dict.keys():
            print("{:<{}}{}".format(key, 16, input_dict[key]))

    @classmethod
    def word_frequency_from_file(cls, filename, monocase = False, pretty_print=False):
        """Reads a txt file and does frequency calculation for each word

        Arguments:
            filename(str): Name of the candidate file for analysis, accepts any file that has raw text in it
            pretty_print(bool): Set this to true if you want to see a frequency report on console
            monocase(bool): If true then all words would be considered lowercase and similar words would merge

        Returns:
            result(dict): key is the word and value is the frequency
        """

        # variable declarations
        all_words = []  # holds all the words
        word_pattern = r'[a-zA-Z]+'

        # file reading and regex logic
        with open(file=filename) as f:
            for line in f:  # reading one line at a time
                match = re.findall(word_pattern, line)
                if match:  # bingo
                    if monocase:
                        all_words += [x.lower() for x in match]  # converting all to lowercase and appending to list
                    else:
                        all_words += match

        # converting all_words list to frequencies
        result = defaultdict(int)
        for word in all_words:
            result[word] += 1

        # del all_words
        del all_words

        if pretty_print:
            WordAnalysis.__pretty_print_word_frequency(result)
        return result

from WordAnalysisKit import WordAnalysis

if __name__ == "__main__":
    WordAnalysis.word_frequency_from_file("words.txt", monocase=True, pretty_print=True)
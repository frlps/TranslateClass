import nltk
import nltk.tokenize as tkz
from sqlalchemy import null

nltk.download('punkt')

from nltk.corpus import stopwords
import nltk.tag as tagger

nltk.download('averaged_perceptron_tagger')

from nltk.stem import RegexpStemmer

import pickle
with open('Tagger_Brill.pkl', 'rb') as pk_file:
    brill_tag = pickle.load(pk_file)

from nltk.corpus import mac_morpho
nltk.download('mac_morpho')
tagged_sents = mac_morpho.tagged_sents()

from nltk.tag.sequential import UnigramTagger
unigram_tag = nltk.tag.UnigramTagger(tagged_sents)


class Translate:
    """
        Classe translate version 1.0 03/08/2022
    """

    def __init__(self, sentence_to_translate=None, unigram_tagger=unigram_tag, brill_tagger=brill_tag):
        self.unigram_tagger = unigram_tagger
        self.brill_tagger = brill_tagger
        if sentence_to_translate == None:
            inp = input('Qual a sentença que voê quer traduzir?? : ')
            self.stt = inp
        else:
            self.stt = sentence_to_translate

    def test_taggers(self):
        print('Unigram nltk tagger')
        print(self.unigram_tagger.tag(tkz.word_tokenize(self.stt)))
        print('Brill tagger')
        print(self.brill_tagger.tag(tkz.word_tokenize(self.stt)))
         

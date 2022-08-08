import pickle
import nltk
import nltk.tag as tagger

nltk.download('averaged_perceptron_tagger')

from nltk.corpus import mac_morpho
nltk.download('mac_morpho')
tagged_sents = mac_morpho.tagged_sents()

from nltk.tag.sequential import UnigramTagger
unigram_tag = tagger.UnigramTagger(tagged_sents)

with open('Tagger_Unigram_NLTK.pkl', 'wb') as handle:
    pickle.dump(unigram_tag, handle, protocol=pickle.HIGHEST_PROTOCOL)
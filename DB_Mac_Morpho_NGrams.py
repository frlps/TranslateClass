import nltk
from nltk.corpus import mac_morpho
nltk.download('mac_morpho')

DB_Tokens_MM = mac_morpho.words()

from nltk import bigrams,trigrams

bigr = bigrams(DB_Tokens_MM)
trigr = trigrams(DB_Tokens_MM)

print(DB_Tokens_MM[:20])
#print(list(bigr)[:20])
#print(list(trigr)[:20])

from nltk.lm.preprocessing import padded_everygram_pipeline
train, vocab = padded_everygram_pipeline(2, DB_Tokens_MM)

from nltk.lm import MLE

lm = MLE(2)
lm.fit(train, vocab)
print(len(lm.vocab))
print(lm.vocab.lookup(DB_Tokens_MM[:2]))

print(lm.score('atinge','média'))

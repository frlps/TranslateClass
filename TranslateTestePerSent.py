from Translate2 import Translate

trans = Translate('Eu passei pela maçã, gostar muito de maçã')

#print(trans.tagged_sentence)

#print(trans.PROPESS_search())
#print(trans.NPROP_search())
#print(trans.NOUN_search())

#print(trans.VERB_REDUCT_lemmatizer())
#print(trans.sent_split())

#print(trans.tagged_sentence)
#print(trans.SUBJECT_APROX_search())

trans.PRONOUNS_MINOR_corrections()

print(trans.tagged_sentence)
#print(trans.VERB_search())
#print(trans.SUBJECT_search())
print(trans.REGULAR_VERB_flexion())
print(trans.tagged_sentence)

#print(trans.temp_sentence())
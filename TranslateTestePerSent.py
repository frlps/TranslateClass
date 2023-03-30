from Translate2 import Translate

trans = Translate('Benjamim e Aline comer maça ontem gostar muito de maça', xml_use=False)

#'eu você comer pastel e tomar suco ontem'
#print(trans.tagged_sentence)

#print(trans.PROPESS_search())
#print(trans.NPROP_search())
#print(trans.NOUN_search())

#print(trans.VERB_REDUCT_lemmatizer())
#print(trans.sent_split())

#print(trans.tagged_sentence)

trans.PRONOUNS_MINOR_corrections()

trans.PROPESS_INCLUD_sentence()
print(trans.REGULAR_VERB_flexion())
print(trans.tagged_sentence)

# trans.PROPESS_INCLUD_sentence()
# print(trans.tagged_sentence)
# print(trans.REGULAR_VERB_flexion())

#print(trans.temp_sentence())
from Translate2 import Translate

trans1 = Translate('Eu e Aline comer maçã ontem, gostar muito de maçã')
trans2 = Translate('Eu comer maçã, gostar muito de maçã')

trans1.show_test_tagger()


# print(trans1.VERB_search())


# print(trans1.PROPESS_search())
# print(trans1.NOUN_search())
# print(trans1.NPROP_search())

print(trans1.tagged_sentence)
print(trans1.ADV_search())
print(trans1.temp_sentence())
print('------------------------------------------------------------------------------')
print(trans2.tagged_sentence)
print(trans2.ADV_search())
print(trans2.temp_sentence())

from Translate2 import Translate

trans1 = Translate('Eu e Aline comer maçã ontem, gostar muito de maçã')
trans2 = Translate('Eu comer maçã, gostar muito de maçã')
trans3 = Translate('A tartaruga precisar mudar senha cartão')
trans4 = Translate('Minha experiência em conversa para qualquer atendimento on-line hoje')
trans5 = Translate('Quero emprestimo dinheiro hoje')

#trans1.show_test_tagger()


# print(trans1.PROPESS_search())
# print(trans1.NOUN_search())
# print(trans1.NPROP_search())

print(trans5.tagged_sentence)
print(trans5.VERB_search())
print(trans5.ADV_search())
print(trans5.temp_sentence())
print(trans5.PROPESS_INCLUD_sentence())
print(trans5.tagged_sentence)

#print('------------------------------------------------------------------------------')
#print(trans2.tagged_sentence)
#print(trans2.ADV_search())
#print(trans2.temp_sentence())

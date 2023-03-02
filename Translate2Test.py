from Translate2 import Translate
import nltk

trans1 = Translate('Eu e Aline comer maçã ontem, gostar muito de maçã')
trans2 = Translate('Eu comer maçã, gostar muito de maçã')
trans3 = Translate('A tartaruga precisar mudar senha cartão')
trans4 = Translate('Minha experiência em conversa para qualquer atendimento on-line hoje')
trans5 = Translate('A Minha experiência dia-a-dia é maior finança hoje.')
trans6 = Translate('Eu já mudar senha internet.')
#trans1.show_test_tagger()


# print(trans1.PROPESS_search())
# print(trans1.NOUN_search())
# print(trans1.NPROP_search())

print(trans6.tagged_sentence)
print(trans6.VERB_search())
print(trans6.ADV_search())
print(trans6.temp_sentence())
trans6.PROPESS_INCLUD_sentence()
print(trans6.tagged_sentence)
print(trans6.is_trasnsitive())

print(trans6.tokens)
bigram = nltk.bigrams(trans6.tokens)
tk_freq = nltk.FreqDist(bigram)
for tk in tk_freq.keys():
    print(tk,tk_freq[tk])
#bigrams = nltk.bigrams(nltk.tokenize(trans5.stt))
#print(bigrams)

#print('------------------------------------------------------------------------------')
#print(trans2.tagged_sentence)
#print(trans2.ADV_search())
#print(trans2.temp_sentence())


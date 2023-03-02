from Translate2 import Translate
import nltk

trans1 = Translate('Eu e Aline comer maçã ontem, gostar muito de maçã')
trans2 = Translate('Eu comer maçã, gostar muito de maçã')
#trans3 = Translate('A menina precisou modificar a senha cartão')
trans3 = Translate('Já mudar senha internet.')
trans4 = Translate('Minha experiência em conversa para qualquer atendimento on-line hoje')
trans5 = Translate('A Minha experiência dia-a-dia é maior finança hoje.')
trans6 = Translate('Eu já mudar senha internet.')
#trans1.show_test_tagger()


print(trans3.PROPESS_search())
print(trans3.NOUN_search())
print(trans3.NPROP_search())

print(trans3.tagged_sentence)
print(trans3.VERB_search())
print(trans3.ADV_search())
print(trans3.temp_sentence())
trans3.PROPESS_INCLUD_sentence()
trans3.TAGGER_MINOR_corrections()
trans3.ARTICLES_MINOR_corrections()
trans3.PREPOSITIONS_MINOR_corrections()
#print(trans5.tagged_sentence)

#print(trans5.tokens)
#bigram = nltk.bigrams(trans5.tokens)
#tk_freq = nltk.FreqDist(bigram)
#for tk in tk_freq.keys():
#    print(tk,tk_freq[tk])

print(trans3.tagged_sentence)
print(trans3.tokens)
print(trans3.VERB_REDUCT_lemmatizer())

print(trans3.AN_MORF_SUBJECT_search())

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


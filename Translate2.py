import pickle
import simplemma
import nltk 
nltk.download('punkt')
import re

#Importanto o POS Tagger Brill já treinado
with open('Tagger_Brill.pkl', 'rb') as handle1:
    brill_tag = pickle.load(handle1)

#Importanto o POS Tagger Ungram do pacote NLTK já treinado
with open('Tagger_Unigram_NLTK.pkl', 'rb') as handle2:
    unigram_tag = pickle.load(handle2)

import nltk.tokenize as tknz


class Translate:
    """
        Classe translate version 1.1 03/08/2022
    """

    def __init__(self, sentence_to_translate=None, unigram_tagger=unigram_tag, brill_tagger=brill_tag):
        """Construtor"""
        self.unigram_tagger = unigram_tagger
        self.brill_tagger = brill_tagger

        if sentence_to_translate == None:
            inp = input('Qual a sentença que você quer traduzir?? : ')
            self.stt = inp.lower()
        else:
            self.stt = sentence_to_translate.lower()

        self.tokens = tknz.word_tokenize(self.stt)

        self.tagged_sentence = self.tagger_choose()

    def test_taggers(self):
        """Metodo de teste dos etiquetadores"""
        tagged_unigram= self.unigram_tagger.tag(tknz.word_tokenize(self.stt))
        tagged_brill = self.brill_tagger.tag(tknz.word_tokenize(self.stt))
        brill_none_counter = 0
        unigram_none_counter = 0

        for pos in tagged_brill:
            if pos[1] == None:
               brill_none_counter += 1

        for pos in tagged_unigram:
            if pos[1] == None:
               unigram_none_counter += 1

        return (tagged_brill, brill_none_counter, tagged_unigram, unigram_none_counter)


    def show_test_tagger(self):
        """Metodo vizualização do teste dos etiquetadores"""
        brill, b_counter, unigram, u_counter = self.test_taggers()
        print('Unigram nltk tagger')
        print(unigram)
        print('Número tokens não identificados em Unigram: ')
        print(u_counter)
        print('Brill tagger')
        print(brill)
        print('Número tokens não identificados em Brill: ')
        print(b_counter)

    """-----------------------------melhor sentença etiquetada-----------------------------"""

    def tagger_choose(self):
        """Metodo escolha da melhor sentença etiquetada"""
        brill, b_counter, unigram, u_counter = self.test_taggers()
    
        if b_counter <= u_counter:
            tagger = brill
        else:
            tagger = unigram
        
        return tagger
        
    """-----------------------------correções menores do etiquetamento, pontuação-----------------------------"""

    def TAGGER_MINOR_corrections(self):
        """Metodo para correção de tagueamento de pontuação"""
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][0] == '.':
                self.tagged_sentence[i] = ('.','.')
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][0] == ',':
                self.tagged_sentence[i] = (',',',')

    """-----------------------------correções menores do etiquetamento, artigos-----------------------------"""

    def ARTICLES_MINOR_corrections(self):
        """Metodo para correção de tagueamento de ARTIGOS"""

        articles_list = ['a','o','as','os','um','uma','uns','umas']

        for i in range(0,len(self.tagged_sentence)):
            art = self.tagged_sentence[i][0]
            if art in articles_list:
                self.tagged_sentence[i] = (art,'ART')

    """-----------------------------correções menores do etiquetamento, preposições-----------------------------"""

    def PREPOSITIONS_MINOR_corrections(self):
        """Metodo para correção de tagueamento de PREPOSIÇÕES essenciais e contrações"""

        prepositions_list = ['à','ao','às','aos','ante', 'após', 'até', 'com', 'contra', 'de', 'da', 'do', 'das', 'dos', 'desde', 
        'em', 'na', 'no', 'nas', 'nos', 'entre', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás', 'num', 'numa']

        for i in range(0,len(self.tagged_sentence)):
            prep = self.tagged_sentence[i][0]
            if prep in prepositions_list:
                self.tagged_sentence[i] = (prep,'PREP')

    """-----------------------------correções menores do etiquetamento, pronomes pessoais e de tratamento-----------------------------"""

    def PRONOUNS_MINOR_corrections(self):
        """Metodo para correção de tagueamento de pronomes pessoais e de tratamento"""

        propess_list = ['eu','tu','ele','ela','nós', 'vós','eles','elas']
        protrat_list = ['você','vocês']

        for i in range(0,len(self.tagged_sentence)):
            pro = self.tagged_sentence[i][0]
            if pro in propess_list:
                self.tagged_sentence[i] = (pro,'PROPESS')
            elif pro in protrat_list:
                self.tagged_sentence[i] = (pro,'PROTRAT')


    """-----------------------------buscas de elementos morfológicos-----------------------------"""

    def VERB_search(self):
        """Metodo para encontrar verbos na sentença etiquetada"""
        verb_indx =[]
        verbs=[]
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][1] == "V":
                verb_indx.append(i)
                verbs.append(self.tagged_sentence[i][0])
        return (verb_indx, verbs)

    def ADV_search(self):
        """Metodo para encontrar advérbios na sentença etiquetada"""
        adv_indx =[]
        advs=[]
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][1] == "ADV":
                adv_indx.append(i)
                advs.append(self.tagged_sentence[i][0])
        return (adv_indx, advs)

    def NOUN_search(self):
        """Metodo para encontrar substantivoss na sentença etiquetada"""
        noun_indx =[]
        nouns=[]
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][1] == "N":
                noun_indx.append(i)
                nouns.append(self.tagged_sentence[i][0])
        return (noun_indx, nouns)

    def NPROP_search(self):
        """Metodo para encontrar nomes próprios na sentença etiquetada"""
        nprop_indx =[]
        nprops=[]
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][1] == "NPROP":
                nprop_indx.append(i)
                nprops.append(self.tagged_sentence[i][0])
        return (nprop_indx, nprops)

    def PROPESS_search(self):
        """Metodo para encontrar nomes próprios na sentença etiquetada"""
        propess_indx =[]
        propesss=[]
        for i in range(0,len(self.tagged_sentence)):
            if self.tagged_sentence[i][1] == "PROPESS":
                propess_indx.append(i)
                propesss.append(self.tagged_sentence[i][0])
        return (propess_indx, propesss)
    
    """-----------------------------Separador de sentença inicial-----------------------------"""

    def sent_split(self):
        """Metodo para separar sentença inicial etiquetada"""

        tagged_sentence = self.tagged_sentence

        first_sentence = []
        types_for_check = []
        index_output = 0

        for i in range(len(tagged_sentence)):
            if tagged_sentence[i][1] != "V" or tagged_sentence[i][1] == "V" and i == 0:
                first_sentence.append(tagged_sentence[i])
                types_for_check.append(tagged_sentence[i][1])
                index_output += 1
            else:
                if 'V' in types_for_check:
                    break
                else:
                    first_sentence.append(tagged_sentence[i])
                    index_output += 1
                    break

        other_sentences = tagged_sentence[index_output:]

        return(first_sentence, other_sentences)


    """-----------------------------tempo da sentença-----------------------------"""

    def temp_sentence(self):
        """Metodo para encontrar o tempo verbal na sentença etiquetada"""

        adv_temp = [('antes','passado'), ('agora','presente'), ('depois','futuro'), 
        ('já','passado'), ('ontem','passado'), ('já','passado'),('hoje','presente'), ('amanhã','futuro')]

        advt_sent=[]

        _, advs = self.ADV_search()

        for advt in adv_temp:
            if advt[0] in advs:
                advt_sent.append(advt)

        if len(advt_sent) == 0:
            temp = input('Quando: Presente, passado ou futuro ?? \n')
            temp = temp.lower()
            return temp
        return advt_sent[0][1]  

    """"-----------------------------sujeito da sentença-----------------------------"""

    def PROPESS_INCLUD_sentence(self):
        """Metodo para incluir EU oculto na sentença etiquetada"""

        sentence = []

        verbs_indx, _ = self.VERB_search()
        adv_indx,_ = self.ADV_search()

        if verbs_indx[0] == 0:
            sentence.append(('eu','PROPESS'))
        elif verbs_indx[0] == 1 and adv_indx[0] == 0:
            sentence.append(('eu','PROPESS'))

        for pos in self.tagged_sentence:
            sentence.append(pos)

        self.tagged_sentence = sentence

    """"-----------------------------Redução de Verbo por lematização-----------------------------"""

    def VERB_REDUCT_lemmatizer(self):
        """
        Método para reduzir o verbo ao infinitivo com lematizador Simplemma.
        """
        infinit_verbs = []

        tagged = self.VERB_search()
        for verb in tagged[1]:
            infinit_verbs.append(simplemma.lemmatize(verb,lang='pt'))

        return infinit_verbs


    """"-----------------------------Seção de flexão verbal-----------------------------"""
    """"-----------------------------INCOMPLETO-----------------------------"""

    def SUBJECT_search(self):
        """Metodo para encontrar possíveis sujeitos (singular ou plural)"""

        singular = ['eu','tu','ele/ela','você']
        plural = ['nós', 'vós','eles/elas','vocês']
        verbal_agreement = None
        propess_equivalence = None

        tag_list = []
        word_list = []

        propess_count = 0
        protrat_count = 0
        nprop_count = 0
        noun_count = 0
        subject_count = 0 

        temp_first_sent,_ = self.sent_split()

        for tk in temp_first_sent:
            tag_list.append(tk[1])
            if tk[1] == 'PROPESS':
                propess_count += 1
            if tk[1] == 'NPROP':
                nprop_count += 1
            if tk[1] == 'N':
                noun_count += 1
            if tk[1] == 'PROTRAT':
                protrat_count +=1
            word_list.append(tk[0])

        subject_count = propess_count + nprop_count + noun_count + protrat_count

        if subject_count == 0:
            verbal_agreement = 'error'
            propess_equivalence = 'error'
        elif subject_count == 1:
            if 'PROPESS' in tag_list:
                if 'eu' in word_list:
                    propess_equivalence = 'eu'
                    verbal_agreement = 'singular'
                elif 'tu' in word_list:
                    propess_equivalence = 'tu'
                    verbal_agreement = 'singular'
                elif 'ele' in word_list or 'ela' in word_list:
                    propess_equivalence = 'ele/ela'
                    verbal_agreement = 'singular'
                elif 'nós' in word_list:
                    propess_equivalence = 'nós'
                    verbal_agreement = 'plural'
                elif 'vós' in word_list:
                    propess_equivalence = 'vós'
                    verbal_agreement = 'plural'
                elif 'eles' in word_list or 'elas' in word_list:
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'
            elif 'PROTRAT' in tag_list:
                if 'você' in word_list:
                    propess_equivalence = 'ele/ela'
                    verbal_agreement = 'singular'
                elif 'vocês' in word_list:
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'
            elif 'NPROP' in tag_list:
                propess_equivalence = 'ele/ela'
                verbal_agreement = 'singular'
            elif 'N' in tag_list:
                word = ''
                for tk in temp_first_sent:
                    if tk[1] == 'N':
                        word = tk[0]
                if word[-1] == 's':
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'
                else:
                    propess_equivalence = 'ele/ela'
                    verbal_agreement = 'singular'
        else:
            if 'PROPESS' in tag_list:
                if 'eu' in word_list:
                    propess_equivalence = 'nós'
                    verbal_agreement = 'plural'
                elif 'nós' in word_list:
                    propess_equivalence = 'nós'
                    verbal_agreement = 'plural'
                elif 'tu' in word_list:
                    propess_equivalence = 'vós'
                    verbal_agreement = 'plural'
                elif 'vós' in word_list:
                    propess_equivalence = 'vós'
                    verbal_agreement = 'plural'
                elif 'ele' in word_list or 'ela' in word_list or 'você' in word_list:
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'
                elif 'eles' in word_list or 'elas' in word_list or 'vocês' in word_list:
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'
            elif 'PROTRAT' in tag_list:
                if 'você' in word_list or 'vocês' in word_list:
                    propess_equivalence = 'eles/elas'
                    verbal_agreement = 'plural'

        return(subject_count,tag_list,word_list,verbal_agreement,propess_equivalence)




    def AN_MORF_SUBJECT_search(self):
        """Metodo de conjugação verbal (singular ou plural)"""

        singular = ['eu','tu','ele','ela','você']
        plural = ['nós', 'vós','eles','elas','vocês']

        isSingular = False
        isPlural = False
        
        verbs_indx, verbs = self.VERB_search()

        propesss_indx, propesss = self.PROPESS_search()
        nprops_indx, nprops = self.NPROP_search()
        nouns_indx, nouns = self.NOUN_search()

        term_ar = {'present':['o','as','a','amos','ais','am'], 
                    'past':['ei','aste','ou','amos','astes','aram'],
                    'future':['arei','arás','ará','aremos','areis','arão']}
        
        term_er = {'present':['o','es','e','emos','eis','em'], 
                    'past':['i','este','eu','eremos','estes','eram'],
                    'future':['erei','erás','erá','eremos','ereis','erão']}
                
        term_ir = {'present':['o','es','e','imos','is','em'], 
                    'past':['i','iste','iu','imos','istes','iram'],
                    'future':['irei','irás','irá','iremos','ireis','irão']}
        
        
        return (len(verbs_indx))

        
        
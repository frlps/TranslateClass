from xml_handler import XMLHandlerModule

list_test = [['eu','PROPESS',True,False], ['você','PROTRAT',False,False], ['comemos', 'V',False,True],['pastel', 'N',False,False], 
             ['e', 'KC',False,False], ['tomar', 'V',False,False], ['suco', 'N',False,False], ['ontem', 'ADV',False,False]]

list_test_binary = [['eu','PROPESS',1,0], ['você','PROTRAT',0,0], ['comemos', 'V',0,1],['pastel', 'N',0,0], 
             ['e', 'KC',0,0], ['tomar', 'V',0,0], ['suco', 'N',0,0], ['ontem', 'ADV',0,0]]


list_test_binary1 = [['eu','PROPESS','true','false'], ['você','PROTRAT','false','false'], ['comemos', 'V','false','true'],['pastel', 'N','false','false'], 
             ['e', 'KC','false','false'], ['tomar', 'V','false','false'], ['suco', 'N','false','false'], ['ontem', 'ADV','false','false']]

xml_handler = XMLHandlerModule()

xml_handler.import_xml_doc_to_root()
sentenca_inicial = xml_handler.get_input()
sentenca_final = xml_handler.get_grammar_frases()[0][3]
sentenca_etiquetada = xml_handler.get_pos_tag_tokens()


for sent in sentenca_etiquetada:
    print(sent)

        #return self.sentenca_etiquetada
print(sentenca_inicial)
print(sentenca_final)

xml_handler.add_treatment_frases(list_test, sentenca_final)

xml_handler.export_results_to_final_XML_document("saida.xml")

tagg_sent = [('benjamim', 'NPROP'), ('e', 'KC'), ('aline', 'NPROP'), ('comer', 'V'), ('maça', 'N'), 
             ('ontem', 'ADV'), ('gostar', 'V'), ('muito', 'ADV'), ('de', 'PREP'), ('maça', 'N')]

new_tagg_sent = [('benjamim', 'NPROP'), ('e', 'KC'), ('aline', 'NPROP'), ('comeram', 'V'), ('maça', 'N'), 
                 ('ontem', 'ADV'), ('gostar', 'V'), ('muito', 'ADV'), ('de', 'PREP'), ('maça', 'N')]


for i in range(len(tagg_sent)):
    print(tagg_sent[i])
    print(new_tagg_sent[i])
    if new_tagg_sent[i] == tagg_sent[i]:
        print('Igual')
    else:
        print('Diferente')

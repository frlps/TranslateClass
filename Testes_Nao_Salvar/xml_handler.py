from enum import Enum

from typing import List, Tuple, Any

import xml.etree.ElementTree as ET
import time

# Enum with translation step names:
class TranslationStep(Enum):
    '''TranslationStep is a enumerator class listing the different steps of the translation from input sentences in the SLK.'''
    POS_Tag = 0
    Grammar = 1
    Treatment = 2
    Closure = 3

class XMLHandlerModule:
    '''XMLHandlerModule is a module for manipulation of data of all the translation modules to a XML document and vice-versa. The XML document is used as a temporary file to import and export results from one translation module to another. This module also export all results of a translation to a final XML document as a mean to debug processes and future analisys.'''
    
    def __init__(self):
        '''Initializes the attributes of the XMLHandlerModule. The module methods work by a XML root, which can be modified on the ongoing translation process and exported to XML documents.'''
        
        # Set path of the default xml file used for results
        self.xml_path = './xml_results/'
        self.xml_default_file = self.xml_path + 'temp_results.xml'
        
        # Root initialization of the XML document for results
        self.root = ET.Element('result')
        self.xml_doc = ET.ElementTree(self.root)
        
        # Insert of tag related to the results of major steps of translation
        ET.SubElement(self.root, 'pos-tag')
        ET.SubElement(self.root, 'grammar')
        ET.SubElement(self.root, 'treatment')
        ET.SubElement(self.root, 'closure')
    
    # General XML document import methods:
    
    def import_xml_doc_to_root(self, document_name = ''):
        '''Imports the data from a already written XML document to the working root.'''
        
        document_path = self.xml_default_file if document_name == '' else self.xml_path + document_name
        self.root = ET.parse(document_path).getroot()
        
    def import_xml_closure_corpus_sentences(self, document_path = './database/corpus.xml') -> List:
        '''Import the corpus sentences used for the closure step of translation.'''
        return ET.parse(document_path).getroot().findall('sentence')
    
    def import_xml_test_set_data(self, document_path = './database/test_set.xml') -> List[Tuple[str,str,str,str]]:
        '''Import the test dataset sentences for testing the results of the translation process of SLK.'''
        test_sentences = ET.parse(document_path).getroot().findall('sentence')
        test_input_sentences = [sentence.find('input_sentence').text for sentence in test_sentences]
        test_grammar_output = [sentence.find('grammar_output').text for sentence in test_sentences]
        test_treatment_output = [sentence.find('treatment_output').text for sentence in test_sentences]
        test_output_sentences = [sentence.find('output_sentence').text for sentence in test_sentences]
        
        test_set = [(test_input_sentences[i], test_grammar_output[i], test_treatment_output[i], test_output_sentences[i]) for i in range(len(test_sentences))]
        return test_set
    
    # General XML content export methods:
    
    def export_results_to_temp_XML_document(self):
        '''Exports the results of the translation already inserted in the working root to a temporary XML file.'''
        
        self.xml_doc = ET.ElementTree(self.root)
        document_path = f'{self.xml_path}temp_results.xml'
        self.xml_doc.write(document_path, encoding='utf-8', xml_declaration=True)
        
    def export_results_to_final_XML_document(self, document_name = ''):
        '''Exports the results of the translation already inserted in the working root to a final XML file, used for debug processes and future analisys.'''
        
        self.xml_doc = ET.ElementTree(self.root)
        current_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
        document_path = f'{self.xml_path}{current_time}_results.xml' if document_name == '' else self.xml_path + document_name 
        self.xml_doc.write(document_path, encoding='UTF-8', xml_declaration=True)
    
    def get_xml_content_by_string(self) -> str:
        '''Exports the results of the translation already inserted in the working root to a string in the correct format for writting in a XML file.'''
        
        return ET.tostring(self.root)
            
    # Set General Information: general processes for to set information in the XML document
    
    def set_input(self, input: str):
        '''Sets the input sentence string of a translation to the "input" tag of 
        the XML document.'''
        result = self.root
        ET.SubElement(result, 'input').text = input

    def set_step_total_output(self, step_nr: int):
        '''This method generates the total output for a translation step. It needs the translation step index, given by the "step_nr" attribute. This index can be listed by the enumeration class "TranslationStep".'''
        
        total_output = self.root.find('input').text
        if TranslationStep(step_nr) != TranslationStep.POS_Tag:
            step_name = TranslationStep(step_nr).name.lower()
            step = self.root.find(step_name)
            frases = step.findall('frase_n')
            for frase in frases:
                frase_output = frase.find('frase_output').text
                total_output = frase_output + ' '
            ET.SubElement(step, 'total_output').text = total_output.strip()
    
    # Get General Information: processes to get general XML documentinformation
    
    def get_input(self):
        '''Returns the sentence input given by the "input" tag in the XML document.'''
        
        result = self.root
        return result.find('input').text
    
    def get_step_total_output(self, step_nr: int):
        '''Returns the total output for a translation step given by the "total_output". The translation step is identified by a index, given by the "step_nr" attribute. This index can be listed by the enumeration class "TranslationStep".'''
        
        step_name = TranslationStep(step_nr).name.lower()
        return self.root.find(step_name).find('total_output').text
    
    # Set POS-tag information: processes to set XML informations for POS-TAG step of translation
    
    def add_pos_tag_token(self, token: str, tag: str, grammar_complements: List):
        '''Sets the information of a token given by the POS-Tag process. Each token has one string content as the "token" attribute, one Tag as the "tag" attribute, and multiple complements given by the list of the "grammar_complements" attribute'''
        
        pos_tag = self.root.find('pos-tag')
        token_n = ET.SubElement(pos_tag, 'token_n')
        ET.SubElement(token_n, 'string').text = token
        ET.SubElement(token_n, 'tag').text = tag
        for complement in grammar_complements:  
            ET.SubElement(token_n, 'grammar_complement_n').text = complement
    
    # Get POS-tag information: processes to get XML informations for POS-TAG step of translation
    
    def get_pos_tag_tokens(self):
        '''Returns the information of all tokens from the input sentence given by the POS-Tag in a List collection. Each cell contains the information of a token given by a inside List, which contains the string content in the 1st cell, the tag in the 2nd, and a list of all complements in the 3rd cell.'''
        tokens = self.root.find('pos-tag').findall('token_n')
        get_tokens = [] 
        for token_n in tokens:
            token = [token_n.find('string').text, \
                        token_n.find('tag').text, \
                        [(tok.text) for tok in token_n.findall('grammar_complement_n')]]
            get_tokens.append(token)
        return get_tokens
        
    # Set Grammar information:
    # Processes to get XML informations for Grammar step of translation:
    
    def add_grammar_frase(self, subject: str, verb: str, object: str, frase_output: str, errors: List):
        '''Sets the information of a frase of the input sentence given by the grammar step. Each frase has a definition of its subject as the "subject" attribute, its verb as the "verb" attribute, its object as the "object" attribute. Also, each frase hase its return of frase output from the grammar step as the "frase_output" attribute, and its list of possible errors from this step as the "errors" attribute.'''
        
        grammar = self.root.find('grammar')
        frase_n = ET.SubElement(grammar, 'frase_n')
        ET.SubElement(frase_n, 'subject').text = subject
        ET.SubElement(frase_n, 'verb').text = verb
        ET.SubElement(frase_n, 'object').text = object
        ET.SubElement(frase_n, 'frase_output').text = frase_output
        for error in errors:
            error_n = ET.SubElement(frase_n, 'error_n')
            ET.SubElement(error_n, 'type').text = error[0]
            ET.SubElement(error_n, 'note').text = error[1]
            
    # Get Grammar information:
    # Processes to get XML informations for Grammar step of translation:

    def get_grammar_frases(self):
        '''Returns the information of all frases from the input sentence given by the grammar step in a List collection. Each cell contains the information of each frase in one inside List collection. Each frase List  contains the subject, the verb, the object, the frase output in the 1st, 2nd, 3rd and 4th cells, respectively, and a list of possible returned errors in the 5th cell.'''
        
        frases = self.root.find('grammar').findall('frase_n')
        get_frases = []
        for frase_n in frases:
            frase = [frase_n.find('subject').text, \
                        frase_n.find('verb').text, \
                        frase_n.find('object').text, \
                        frase_n.find('frase_output').text, \
                        []]
            for error in frase_n.findall('error'):
                frase[4].append([error.find('type').text, \
                                 error.find('note').text])
            get_frases.append(frase)
        return get_frases

    # Set Treatment information:
    # Processes to get XML informations for Treatment step of translation:
            
    def add_treatment_frases(self, tokens: List, frase_output: str):
        '''Sets the information of a frase of the input sentence given by the treatment step of translation. Each frase has a List of its tokens, with all data gathered in the treatment regarding each of it, given in the "tokens" attribute of the method. Each cell of the "tokens" attribute has one token data gathered in a List collection, with its string content (in the 1st cell), its POS-Tag (in the 2nd cell), a boolean indicating if this token was add or not in the treatment step (in the 3rd cell) and another boolean indicating if was flexed verb or not in this step process (in the 4th cell). Also, the "frase_output" attribute of the method receives the frase output given by the treatment step.'''
        
        treatment = self.root.find('treatment')
        frase_n = ET.SubElement(treatment, 'frase_n')
        for token in tokens:
            token_n = ET.SubElement(frase_n, 'token')
            ET.SubElement(token_n, 'changed_token').text = token[0]
            ET.SubElement(token_n, 'tag').text = token[1]
            ET.SubElement(token_n, 'added').text = 'true' if token[2] else 'false'
            ET.SubElement(token_n, 'flexion').text = 'true' if token[3] else 'false'
        ET.SubElement(frase_n, 'frase_output').text = frase_output
        
    # Get Treatment information:
    # Processes to get XML informations for Treatment step of translation: 
        
    def get_treatment_frases(self):
        '''Returns the information of all frases from the input sentence given by the treatment step in a List collection. Each cell contains the information of a frase given by one List, which contains its List of tokens and their data in the 1st cell, and a frase output in the 2nd cell. Inside the tokens List, each cell has the information regarding one token gathered in a inside List. Each token List has its string content (in the 1st cell), its POS-Tag (in the 2nd cell), a boolean indicating if this token was add or not in the treatment step (in the 3rd cell) and another boolean indicating if was flexed verb or not in this step process (in the 4th cell).'''
        
        frases = self.root.find('treatment').findall('frase_n')
        get_frases = []
        for frase_n in frases:
            frase = [[], frase_n.find('frase_output').text]
            for token_n in frase_n.findall('token_n'):
                frase[0].append([ token_n.find('changed_token').text, \
                                    token_n.find('tag').text, \
                                    token_n.find('added').text, \
                                    token_n.find('flexion').text ])
            get_frases.append(frase)
        return get_frases
    
    # Set Closure information:
    # Processes to set XML informations for Closure step of translation: 
    
    def add_closure_frase(self,  tokens: List, flexion: bool, frase_output: str):
        '''Sets the information of a frase of the input sentence given by the closure step of translation. Each frase has a List of its tokens, also with all data gathered in the treatment regarding each of it, given in the "tokens" attribute of the method. Each cell of the "tokens" attribute has one token data in a List collection, with its string content (1st cell), its POS-Tag (2nd cell) and a boolean indicating if this token was add or not in the closure step (in the 3rd cell). The "flexion" attribute is a boolean which indicates if were flexion of verbs or not in the closure process, and the "frase_output" attribute of the method receives the frase output given by the closure step.'''
        
        closure = self.root.find('closure')
        frase_n = ET.SubElement(closure, 'frase_n')
        for token in tokens:
            token_n = ET.SubElement(frase_n, 'token_n')
            ET.SubElement(token_n, 'changed_token').text = token[0]
            ET.SubElement(token_n, 'tag').text = token[1]
            ET.SubElement(token_n, 'added').text = token[2]
        ET.SubElement(frase_n, 'flexion').text = flexion
        ET.SubElement(frase_n, 'frase_output').text = frase_output
        
    # Set Closure information:
    # Processes to set XML informations for Closure step of translation: 

    def get_closure_frases(self):
        '''Returns the information of all frases from the input sentence given by the closure step in a List collection. Each cell contains the information of a frase given by one List, which contains the a List of tokens and its data in the 1st cell, a boolean indicating if verbs were flexed in this step (2nd cell), and a frase output in the 2nd cell. Inside the tokens data List, each cell has the information regarding one token in a inside List. Each token list has its string content (1st cell), its POS-Tag (2nd cell) and if this token was add in this step process as a boolean (3rd cell).'''
        
        frases = self.root.find('closure').findall('token_n')
        get_frases = []
        for frase_n in frases:
            frase = [[], \
                        frase_n.find('flexion').text , \
                        frase_n.find('frase_output').text]
            for token_n in frase_n.findall('token_n'):
                frase[0].append([ token_n.find('changed_token').text, \
                                    token_n.find('tag').text, \
                                    token_n.find('added').text ])
            get_frases.append(frase)
        return get_frases
    
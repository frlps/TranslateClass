import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("Testes_Nao_Salvar/filename2.xml", encoding='utf-8', xml_declaration=True)
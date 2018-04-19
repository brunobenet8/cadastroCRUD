import xml.etree.ElementTree as ET

tree = ET.parse('lar.xml')
root = tree.getroot()

for node in root.getiterator():
    if node.tag == '{http://www.portalfiscal.inf.br/nfe}pesoB':
        print node.text
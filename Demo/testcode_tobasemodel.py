from Pydantic_Model.pydantic import XMLModelConverter
from Module.out import Model
import xml.etree.ElementTree as ETree

emptymodel = Model()
xmletree = ETree.parse("XML_Files/demo.xml")
filledmodel = XMLModelConverter.to_basemodel(xmletree, emptymodel)

print(filledmodel)
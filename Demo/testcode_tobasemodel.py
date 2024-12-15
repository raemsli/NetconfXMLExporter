from Pydantic_Model.pydantic import XMLModelConverter
from Module.out import Model
import xml.etree.ElementTree as ET

mo = Model()
xmletree = ET.parse("XML_Files/demo.xml")

mo2 = XMLModelConverter.to_basemodel(xmletree, mo)

print("Finished")
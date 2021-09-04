""" usage 
add xml path
add classes

after run
python classCount.py
 """



import argparse
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#add xml path
xmlPath="./"

#add class
classes ={
"Dur_Tabelasi":0,
"Durak_Tabelasi":0
}



for filename in os.listdir(xmlPath):
    if filename.endswith(".xml"):
        mytree = ET.parse(xmlPath+filename)
        myroot = mytree.getroot()
        
        for pathLabel in myroot.iter('object'):
            for objectLabel in pathLabel.iter("name"):
                if (objectLabel.text in classes):
                    classes[objectLabel.text]=classes[objectLabel.text]+1
                else:
                    print("Not Found Classes test: "+objectLabel.text)



print(classes)
with open('classcount.txt', 'w') as f:
    print(classes, file=f)
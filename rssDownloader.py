import sys
import os
import xml.etree.ElementTree as ET

if len(sys.argv) == 2 and sys.argv[1].endswith('.rss'):
    xmlParsed = ET.parse(sys.argv[1])
    root = xmlParsed.getroot()

    for item in root.findall('./channel/item'):
        for child in item:
            if child.tag == 'title':
                print(child.text)
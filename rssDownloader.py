import sys
import os
import xml.etree.ElementTree as ET
import requests

if len(sys.argv) == 2 and sys.argv[1].endswith('.rss'):
    xmlParsed = ET.parse(sys.argv[1])
    root = xmlParsed.getroot()
    episodeTitle = ''

    # for item in root.findall('./channel/item'):
    #     for child in item:
    #         if child.tag == 'title':
    #             episodeTitle = child.text.replace(" ", "_") + '.mp3'
    #             print('Downloading episode: ' + child.text)
                
    #         if child.tag.endswith('content') and child.attrib['type'] == 'audio/mpeg':
    #             epReq = requests.get(child.attrib['url'])
    #             with open(episodeTitle, wb) as f:
    #                 f.write(epReq.content)

    items = root.findall('./channel/item')
    for child in items[0]:
        if child.tag == 'title':
            episodeTitle = child.text.replace(" ", "_") + '.mp3'
            print('Downloading episode: ' + child.text)
            
        if child.tag.endswith('content') and child.attrib['type'] == 'audio/mpeg':
            try:
                epReq = requests.get(child.attrib['url'])
            except requests.exceptions.Timeout: 
                print('Retrying download of episode: ' + child.text)
                epReq = requests.get(child.attrib['url'])
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            
            with open(episodeTitle, 'wb') as f:
                f.write(epReq.content)
            

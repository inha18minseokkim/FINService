import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from declaration import crtfc_key
import requests
import asyncio
import zipfile
import urllib
import xml.etree.ElementTree as elemTree
import codecs
url_code = "https://opendart.fss.or.kr/api/corpCode.xml"
def update_code():
    res, _ = urllib.request.urlretrieve(url_code + "?crtfc_key=" +crtfc_key)
    zip_file_object = zipfile.ZipFile(res,'r')
    first_file = zip_file_object.namelist()[0]
    file = zip_file_object.open(first_file)
    codedXmlFile = ""
    with zip_file_object.open(first_file) as readFile:
        for line in codecs.iterdecode(readFile, 'utf8'):
            codedXmlFile += line
    f = open("ASDF.xml", "w")
    f.write(codedXmlFile)
    
    tree = elemTree.parse("ASDF.xml")
    li = tree.findall('list')
    print(li)
    for i in li:
        print(i.find('corp_code').text, i.find('corp_name').text,i.find('stock_code').text,i.find('modify_date').text)
        
if __name__ == "__main__":
    update_code()
    # f = open("ASDF.xml","rb")
    # tree = elemTree.parse("ASDF.xml")
    # li = tree.findall('list')
    # print(li)
    # for i in li:
    #     print(i.find('corp_code').text, i.find('corp_name').text,i.find('stock_code').text,i.find('modify_date').text)
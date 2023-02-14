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

dbClientUrl = "http://localhost:8081/tb_corp_code/"

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
    resli = []
    cnt = 0
    for i in li:
        cnt+=1
        rb = {"corp_code" : i.find('corp_code').text,
        "corp_name" : i.find('corp_name').text,
        "stock_code" : i.find('stock_code').text,
        "modify_date" : i.find('modify_date').text}
        #print(i.find('corp_code').text, i.find('corp_name').text.text,i.find('stock_code').text,i.find('modify_date').text)
        try:
            resli.append(rb)
        except:
            print(cnt)
        #requests.post(dbClientUrl + "insertCorpInfo",data=rb)
        
if __name__ == "__main__":
    update_code()
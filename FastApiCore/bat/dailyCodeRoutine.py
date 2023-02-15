import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from declaration import crtfc_key,dbUrl
import requests
import asyncio
import zipfile
import urllib
import xml.etree.ElementTree as elemTree
from loguru import logger
import codecs
url_code = "https://opendart.fss.or.kr/api/corpCode.xml"

dbClientUrl = dbUrl + "/tb_corp_code/"

def update_code():
    logger.debug("dailyCodeRoutine 시작")
    res, _ = urllib.request.urlretrieve(url_code + "?crtfc_key=" +crtfc_key)
    zip_file_object = zipfile.ZipFile(res,'r')
    first_file = zip_file_object.namelist()[0]
    file = zip_file_object.open(first_file)
    logger.debug("dailyCodeRoutine dart에서 파일 파싱 시작")
    codedXmlFile = ""
    with zip_file_object.open(first_file) as readFile:
        for line in codecs.iterdecode(readFile, 'utf8'):
            codedXmlFile += line
    logger.debug("dailyCodeRoutine dart에서 파일 파싱 성공")
    tree = elemTree.fromstring(codedXmlFile)

    li = tree.findall('list')

    #print(li)
    resli = []
    cnt = 0
    for i in li:
        cnt+=1
        rb = {"corp_code" : i.find('corp_code').text,
        "corp_name" : i.find('corp_name').text,
        "stock_code" : i.find('stock_code').text,
        "modify_date" : i.find('modify_date').text}
        if cnt % 500 == 0:
            logger.debug(cnt)
        try:
            resli.append(rb)
        except:
            logger.debug("파싱 실패 있음")
            print(cnt)
        try:
            requests.post(dbClientUrl + "insertCorpInfo",json=rb)
        except Exception as e:
            logger.debug("dailyCodeRoutine 리퀘스트 에러 발생")
    logger.debug(resli[0],resli[-1])
    logger.debug("dailyCodeRoutine 성공")
if __name__ == "__main__":
    update_code()
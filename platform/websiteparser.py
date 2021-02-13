from cnn_parser import parser as cnnparser
from fox_parser import parser as foxparser
from npr_parser import parser as nprparser
#from .cnbc_parser import parser as cnbcparser

def parse(websiteDict):
    articleDict = {}
    for website in websiteDict:
        if website == 'cnn':
            for url in websiteDict[website]:
                cnnDict = cnnparser.parse(url)
                if type(cnnDict) == dict:
                    if url in articleDict:
                        articleDict[url].append([cnnDict["title"], cnnDict["body"]])
                    else:
                        articleDict[url] = [cnnDict["title"], cnnDict["body"]]
        elif website == 'fox':
            for url in websiteDict[website]:
                foxDict = foxparser.parse(url)
                if type(foxDict) == dict:
                    if url in articleDict:
                        articleDict[url].append([foxDict["title"], foxDict["body"]])
                    else:
                        articleDict[url] = [foxDict["title"], foxDict["body"]]
        elif website == 'npr':
            for url in websiteDict[website]:
                nprDict = nprparser.parse(url)
                if type(nprDict) == dict:
                    if url in articleDict:
                        articleDict[url].append([nprDict["title"], nprDict["body"]])
                    else:
                        articleDict[url] = [nprDict["title"], nprDict["body"]]
    return articleDict
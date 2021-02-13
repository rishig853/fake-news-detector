from googlesearch import search

def searchGoogle(query):
    websiteDict = {}
    for result in search(query, tld="com", num=30, stop=30, pause=2): 
        if "foxnews.com" in result or "cnn.com" in result or "cnbc.com" in result or "npr.org" in result:
            if "foxnews.com" in result:
                if "fox" in websiteDict:
                    websiteDict["fox"].append(result)
                else:
                    websiteDict["fox"] = [result]
            elif "cnn.com" in result:
                if "cnn" in websiteDict:
                    websiteDict["cnn"].append(result)
                else:
                    websiteDict["cnn"] = [result]
            elif "cnbc.com" in result:
                if "cnbc" in websiteDict:
                    websiteDict["cnbc"].append(result)
                else:
                    websiteDict["cnbc"] = [result]
            elif "npr.org" in result:
                if "npr" in websiteDict:
                    websiteDict["npr"].append(result)
                else:
                    websiteDict["npr"] = [result]
    return websiteDict

print(searchGoogle("twitter and facebook grilled by senate"))
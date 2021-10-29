import re

file1 = open('/home/anthony/Documents/code/py/powershellAnyl/pow.ps1', 'r')
Lines = file1.readlines()
foundUrls= []

count = 0

def urls(linetoParse):
    linetoParse=linetoParse.replace('`','')
    linetoParse=linetoParse.replace('\'','')
    linetoParse=linetoParse.replace('"','')
    global foundUrls
    resultHTTP = re.search('http(.*)',linetoParse)
    resultHTTPS = re.search('https(.*)',linetoParse)
    if resultHTTP or resultHTTPS:
        foundUrls.append(resultHTTP.group(0))


        #print(linetoParse)
    if resultHTTPS:
        foundUrls.append(resultHTTPS.group(0))



for line in Lines:
    #if "$" in line.strip():
    if (line.startswith("$")):
        urls(line)
        result = re.search('=(.*)',line)
        #print((line.lstrip()).rstrip())
        try:
            f=0
            #print(result.group(0))
        except:
            continue
    
        

    #count += 1
    #print(line.strip())
print(foundUrls)
import re
from collections import Counter
file1 = open('/home/anthony/Documents/code/py/powershellAnyl/pow.ps1', 'r')
Lines = file1.readlines()
foundUrls= []
totalTicks=0
count = Counter(Lines)
#print(count['a'])
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



#print(len(re.findall(file1, '1')))
for line in Lines:
    #if "$" in line.strip():
    totalTicks=totalTicks+ len(re.findall('`',line))
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
print("<-----URLS DETECTED----->")
for x in foundUrls:
    print(x)
print("<------TOTAL TICKS------>")
print(totalTicks)

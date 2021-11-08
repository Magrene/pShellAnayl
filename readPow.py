import re
file1 = open('/home/anthony/Documents/code/py/powershellAnyl/pow.ps1', 'r')
Lines = file1.readlines()
foundUrls= []
foundVaribleRef=[]
totalTicks=0

def urls(linetoParse):
    linetoParse=linetoParse.replace('`','')
    linetoParse=linetoParse.replace('\'','')
    linetoParse=linetoParse.replace('"','')
    global foundUrls
    resultHTTP = re.search('http(.*)',linetoParse)
    resultHTTPS = re.search('https(.*)',linetoParse)
    if resultHTTP or resultHTTPS:
        foundUrls.append(resultHTTP.group(0))
    if resultHTTPS:
        foundUrls.append(resultHTTPS.group(0))

for line in Lines:
    totalTicks=totalTicks+ len(re.findall('`',line))
    line=line.replace('`','')
    if (line.startswith("$")):
        urls(line)
        varibleResult=re.search('\$(.*)=',line)
        
        if varibleResult:
            if varibleResult.group(1) not in foundVaribleRef:
                foundVaribleRef.append(varibleResult.group(1))
        #print(result.group(0))
print("<-----URLS DETECTED----->")
for x in foundUrls:
    print(x)

print("<------TOTAL TICKS------>")
print(totalTicks)
print("<----Found Varibles----->")
for x in foundVaribleRef:
    print(x)

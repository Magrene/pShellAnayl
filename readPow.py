import re , sys
file1 = open('/home/anthony/Documents/code/py/powershellAnyl/' + sys.argv[1] , 'r')
print(sys.argv[0])
Lines = file1.readlines()
foundUrls= []
foundVaribleRef=[]
totalTicks=0
def findVarible(line):
    global foundVaribleRef
    if (line.startswith("$")):
        urls(line)
        varibleResult=re.search('\$(.*)=',line)
        
        if varibleResult:
            if varibleResult.group(1) not in foundVaribleRef:
                foundVaribleRef.append(varibleResult.group(1))
        #print(result.group(0))

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

def getVarRef(reSrch):
    for line in Lines:
        result=re.search(reSrch+'(.*)',line)
        if result:
            return line
        

def getRefRe(line,reSrch):
    line=re.search(reSrch+'(.*)',line)
    if line:
        return line.group(0)

def loopEachLine(Lines):
    global totalTicks
    for line in Lines:
        totalTicks=totalTicks+ len(re.findall('`',line))
        line=line.replace('`','')
        findVarible(line)
        urls(line)
    
loopEachLine(Lines)
       

print("<-----URLS DETECTED----->")
for x in foundUrls:
    print(x)

print("<------TOTAL TICKS------>")
print(totalTicks)
print("<----Found Varibles----->")
for x in foundVaribleRef:
    print(x)
print("<---Inital Declaration-->")
for x in foundVaribleRef:
    print(x)
    print(getVarRef(x))

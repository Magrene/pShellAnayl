import re , sys
file1 = open('/home/anthony/Documents/code/py/powershellAnyl/' + sys.argv[1] , 'r')
print(sys.argv[0])
Lines = file1.readlines()
foundUrls= []
foundVaribleRef=[]
foundFunctions=[]
totalTicks=0
antiVirusDetect=False
antiVirusDetectLine=[]
def findVarible(line):
    global foundVaribleRef
    if (line.startswith("$")):
        varibleResult=getRefReEnd(line,"\$","=")
        if varibleResult and varibleResult.group(1) not in foundVaribleRef:
            foundVaribleRef.append(varibleResult.group(1))
def findFunctions(linetoParse):
    global foundFunctionNames
    funResult=getRefReEnd(linetoParse,"function","{")
    if funResult:
        foundFunctions.append(funResult.group(1))

def urls(linetoParse):
    linetoParse=linetoParse.replace('`','')
    linetoParse=linetoParse.replace('\'','')
    linetoParse=linetoParse.replace('"','')
    resultHTTP = getRefRe(linetoParse,"http")
    resultHTTPS = getRefRe(linetoParse,"https")
    
    if resultHTTP or resultHTTPS:
        foundUrls.append(resultHTTP.group(0))
    if resultHTTPS:
        foundUrls.append(resultHTTPS.group(0))

def getVarRef(reSrch):
    for line in Lines:
        result=getRefReEnd(line,reSrch,"=")
        if result:
            return line
        

def getRefRe(line,reSrch):
    result=re.search(reSrch+'(.*)',line)
    if result:
        return result

def getRefReEnd(line,reSrch,reSrchEnd):
    line=re.search(reSrch+'(.*)'+reSrchEnd,line)
    if line:
        return line
def antiVirusDetection(line):
    global antiVirusDetect ,antiVirusDetectLine
    if getRefRe(line,"AntiVirusProduct"):
        antiVirusDetect=True
        antiVirusDetectLine.append(line)

def loopEachLine(Lines):
    global totalTicks
    for line in Lines:
        totalTicks=totalTicks+ len(re.findall('`',line))
        line=line.replace('`','')
        findVarible(line)
        urls(line)
        findFunctions(line)
        antiVirusDetection(line)

loopEachLine(Lines)

print("\n<-----URLS DETECTED----->")
for x in foundUrls:
    print(x)

print("\n<------TOTAL TICKS------>")
print(totalTicks)
print("<----FOUND FUNCTIONS---->")
for x in foundFunctions:
    print(x)
print("\n<----Found Varibles----->")
for x in foundVaribleRef:
    print(x)
print("\n<---Initial Declaration-->")
for x in foundVaribleRef:
    print(x)
    print(str(getVarRef(x)))
print("\n<--Anti Virus Detection-->")
print(antiVirusDetect)
if antiVirusDetect:
    print("\n  <--Offending  Lines-->")
    for x in antiVirusDetectLine:
        print(" ",x)

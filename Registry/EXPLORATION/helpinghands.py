#Reading Strings and accessing them:
#=======================================================================
def getfile(loc):
    with open(loc,  'r', encoding='utf-8') as fp:
        cont = fp.read()
    return cont

def getvalue(key):
    content = data.split(key)[1]
    target = content.split("string LocValue =")[1].split("LocEntry data")[0][2:]
    getend = -1*(target[::-1].index('"')) -1
    return (target[:getend])
#========================================================================
data = getfile("strings_localize/strings_en_US_loc.txt") 
reg = getfile("contents.txt")
all_families = ["careofmagicalcreatures","darkarts","hogwartsschool","legendsofhogwarts",
"ministry","magizoology","magicalgamesandsports","mysteriousartefacts",
"wondersofthewizardingworld","oddities"]

def listcategory(name):
    catlist = []
    reg1 = reg.split("\n")
    pos = reg1.index(name)
    catlist.append(reg1[pos]) #name
    pagelist = (reg1[pos-1][1:-1].split(","))
    newlist = []
    pos=pos+1
    for k in pagelist: newlist.append(int(k))
    catlist.append(newlist)
    for p in range(len(newlist)):
        catlist.append(reg1[pos])
        pos=pos+1
        for i in range(newlist[p]):
            catlist.append(reg1[pos])
            pos=pos+1
            
    
    
    return(catlist)

def navi():
    htm = ""
    for jj in all_families:
        htm = htm +'''<a href="family_'''+jj+'''.html" style="padding:5px;"><img src="./Media/family_'''+jj+'''.png" width="50px"></a>'''
    return htm
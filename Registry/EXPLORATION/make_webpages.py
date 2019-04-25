import helpinghands as hps

top1 = '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"/><link rel="stylesheet" href="styling/style.css">
</head>
<body><div class="categor" align="center">'''+hps.navi()+'''<table border="1"><tr><td><img width="120px" src="./Media/'''
top2 = '''.png"></td>\n<td><h1 id="header" class="text-primary">'''
top3 = '''</h1></td></table></div>'''
#title
topitem = '''<div class="item"><div class="product-info"> <h2>'''#name
miditem= '''</h2><hr><h3>''' #then desc + <hr>
closedesc='''</h3></div><img class="item-img"src="./Media/'''
enditem = '''"></div></div>"'''

end = '''
</body>

</html>'''

def write_item(id):
    html =""
    html = html+topitem
    html = html+hps.getvalue("collection_items_"+id+"_name")
    html = html+miditem
    html = html+hps.getvalue("collection_items_"+id+"_description")
    html = html+"<hr>Return to: "+hps.getvalue("collection_items_"+id+"_return_location")
    html = html+closedesc+id+".png"+enditem
    return(html)

def themain(caty):
        ziel = hps.listcategory(caty)
        print(ziel)
        sticks = ziel[1]
        
        with open("./WEB/"+caty+".html",'w',encoding='utf-8') as f:
            f.write(top1)
            f.write(ziel[0])
            f.write(top2)
            f.write(hps.getvalue("collection_"+ziel[0]+"_name"))
            f.write(top3)
            c = 2
            #now into the pages:
            for k in range(len(sticks)):
                f.write('''<div class="epage"><h2>''')
                f.write("Page "+str(k+1)+": ")
                print(ziel[c])
                f.write(hps.getvalue("collection_" + ziel[c])+"</h2><hr>")
                c = c+1
                #Into the items (img,name,ret,desc)
                for i in range(sticks[k]):
                    f.write(write_item(ziel[c]))
                    c = c+1
                
                    
                    
                f.write("</div><hr><hr>")
            f.write(end)
for zz in hps.all_families:
    themain("family_"+zz)
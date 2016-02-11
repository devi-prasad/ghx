import github3 
import sys
import re 
import collections 
import requests
import mssqlghx 
import requests
import json

num = 100
def replace(strng,replaceText): 
    rpl = 0 
    while rpl > -1: 
        rpl = strng.find(replaceText) 
        if rpl != -1: 
            strng = strng[0:rpl] + strng[rpl + len(replaceText):] 
    return strng 
#i = github3.iter_all_repos(num) 
number = 0 
lessThanPos = -1 
count = 0 
listOf = [] 
totalcount = 0
 

#print(number)
 
myconn = mssqlghx.MSSQLghx("GHXRepodb")
myconn.connect()
lastid = myconn.lastid('tbl_test')
i = github3.iter_all_repos(num) 
number = 0 
lessThanPos = -1 
count = 0 
listOf = [] 
totalcount = 0
for repo in i:
    url = 'https://github.com/'+str(repo) 
    print(url) 
    resp = requests.get(url) 
    f = open(str(number)+'.txt','w')
    try:
        f.write(resp.text)
    except:
        continue
    f.close() 
    number+=1
 

 
for i in range(num-1):
    print("here")
    #write File 
    writeto = open(str(i)+'.txt1','w') 
 
    #read file and store it in list 
    f = open(str(i)+'.txt','r') 
    listOf=[]
    for readLine in f.readlines(): 
        listOf.append(readLine)          
        #print(readLine)
    f.close() 
 
    #remove all tags   
    for line in listOf: 
        count = 0;   
        lessThanPos = -1   
        lineTemp =  line 
 
        for char in lineTemp: 
 
            if char == "<": 
                lessThanPos = count 
            if char == ">": 
                if lessThanPos > -1: 
                    if line[lessThanPos:count + 1] != '<>': 
                        lineTemp = replace(lineTemp,line[lessThanPos:count + 1]) 
                        lessThanPos = -1 
            count = count + 1 
        lineTemp = lineTemp.replace("&lt","<") 
        lineTemp = lineTemp.replace("&gt",">")                   
        writeto.write(lineTemp)   
    writeto.close()

    number=number+1  
    print(number)     



for k in range(99):  
        totalcount=0
        print("here")
        wanted = re.findall('\w+', open('c-keywords.txt').read().lower())
        unique = re.findall('\w+', open('c-keywords-unique.txt').read().lower()) 
        cnt = collections.Counter()
        keywordname = None
        try: 
            words = re.findall('\w+', open(str(k)+'.txt1').read().lower()) 
        except:
            continue
        for word in wanted: 
            cnt[word] =0 
        for word in words:
            if word in wanted:
                keywordname = word 
                cnt[word] += 1 
                totalcount +=1
        print(totalcount)
	#print(cnt)

        #if totalcount > 50:
        lastid = lastid + 1
        myconn.insert('tbl_test',lastid)
        for key,value in enumerate(cnt):
            if value in unique:
                w = '['+value+']'
                myconn.update('tbl_test', lastid, w, cnt[value])  
                continue  
            myconn.update('tbl_test', lastid, value, cnt[value])
        
          

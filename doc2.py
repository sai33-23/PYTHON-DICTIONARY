str="w3resource"
i=0
dic={}
while i<len(str):
    j=0
    count=0
    while j<len(str):
        if str[i]==str[j]:
            count=count+1
        dic[str[i]]=count
        j=j+1
    i=i+1
print(dic)
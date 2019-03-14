# 统计txt文本中的高频字
import json

fr = open("C:\\Users\\xiaoy\\Downloads\\三寸人间.txt", 'r')

characters = []
dic = {}
count = 0

for line in fr:
    line = line.strip()
    if len(line) == 0:
        continue

    for ch in line:
        if ch <u'\u4e00' or ch>=u'\u9fa5':
            continue
        count += 1
        if ch not in characters:
            characters.append(ch)
            dic[ch] = 1
        else:
            dic[ch] +=1        

print('总字数：'+str(count))
print('共使用字：'+str(len(characters)))
#########################
ll = sorted(dic.items(),key=lambda x:x[1],reverse=True)

fw = open('ret.json','w')
fw.write(json.d;umps(ll))
fw.close()

ret = open('ret.csv','w')
for l in ll:
    ret.write(str(l[0])+','+str(l[1])+'\n')
ret.close()
fr.close()

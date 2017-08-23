#lets do an example

'''
import re

#Nameage = '''
#Janice is 22 and Theon is 33
#Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}

x = 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1

print(ageDict)
'''

'''
import re

if re.search("inform", "we need to inform with the latest informations"):
    
    print("there are inform")

'''

'''
allinform =re.findall("inform", "we need to inform with th latest inform")

for i in allinform:

    print(i)
'''

'''
import re

str = "we need to inform him with the latest information"

for i in re.finditer("inform", str):

    loctup = i.span()

    print(loctup)
'''

'''
import re

str = "sat, har, mat, pat"

allstr = re.findall("[shmp]at", str)

for i in allstr:

    print (i)
'''


#continue later
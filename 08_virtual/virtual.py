import subprocess
fileRead = open('requirements.txt' , 'r')

listLib = []
readlineCount=0
for file in fileRead:
    readlineCount+=1
    if readlineCount>=3:
        listLib.append(file)

# print(listLib)
moduleList=[]
versionList =[]
for i in listLib:
    versionList.append(i.split(' ')[-1].replace('\n',''))
    moduleList.append(i.split(' ')[0])

# for i  in moduleList:
#     i = i.replace('\n','')
#     print(i.replace('\n',''))

# print(moduleList)
# print(versionList)
    
for i in range(len(versionList)):
    module_with_version = f"{moduleList[i]}=={versionList[i]}"
    subprocess.run(['pip' , 'uninstall', module_with_version])
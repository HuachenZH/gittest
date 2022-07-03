# new feature(s) of v7:
# four steps
# git stuffs. os.system()

# outputPath can be optimized
# remote and branch not set

# pb pandas loc : solved
# pb os.system("cd ") : solved, use os.chdir instead
# pb os.chdir syntax : solved, use r'string'
# pb pandas: solved, each time reset_index, a new column is created

import os
inputPath=r"D:\full_stack\py\Markdown\ITSM\ITSM-IT-Service-Management"
outputPath=r"D:\full_stack\py\Markdown\ITSM\git_automation"
#%% git pull stuffs
os.system("git config --global user.email \"huachen.zhang.23@eigsi.fr\"")
os.system("git config --global user.name \"HuachenZH\"")


os.chdir(outputPath[:outputPath.rfind('\\')]) # os.system("cd ") does not work
os.system("git clone https://gitlab.com/HuachenZH/git_automation") # it's ok to keep this line if the directory already exists in local
os.chdir(outputPath)
os.system("git pull")

#%% os stuffs ---------------------------------------------------
os.chdir(inputPath)
files=list(file for file in os.listdir(inputPath) if os.path.isfile(os.path.join(inputPath, file))) # get the file names of the directory. Put them into a list
import time
time.sleep(2)
input('[*] git is ready. Start the script?')
print(" |___ \   / ____| |                  _ \n   __) | | (___ | |_ ___ _ __  ___  (_)\n  |__ <   \___ \| __/ _ \ '_ \/ __|    \n  ___) |  ____) | ||  __/ |_) \__ \  _ \n |____/  |_____/ \__\___| .__/|___/ (_)\n                        | |            \n                        |_|            ")
print("In fact there are four steps.")
print("Step 1: An excel will be generated, fill the excel.\nStep 2: New markdown files will be generated in one same folder. Check them.\nStep 3: Place the md files to their matching folder (front, back ...)\nStep 4: git push")
print('\n')
#%% the function old md to new md ------------------------------------
def newmd(nameScript:str, inputPath:str, outputPath: str, excelName:str)->str:
    # read original file ----------------------------------
    os.chdir(inputPath) # cd to input path where we find original markdown files
    fhand=open(nameScript,encoding="UTF-8") # type: <class '_io.TextIOWrapper'>
    original=''
    for line in fhand:  # type of line: string
        original+=line
    
    # what is ------------------------------------
    whatis=''
    # find the "what is" part of the original script
    # print(original.find("## **What is")) # 0
    # print(original.find("### **Details")) #81
    whatis+=original[original.find("## **What is"):original.find("### **Details")]


    # Details ---------------------------------------
    os.chdir(outputPath)
    df=pd.read_excel(excelName)
    df.set_index('file_name', inplace = True)
    details="### **Details**"+"\n"
    detailsList=["- **Name Script** : ","- **Created by** : ","- **Created** : ","- [**_Workplace link_**]","- **File extension** : ","- **Application suite** : ","- **Module** : ","- **Type** : ","- **Scope** : ","- **Release** : ","- **Update by** : ","- **Updated** : ","- **Version** : "]
    # index  -->        0                      1                     2                    3                           4                         5                          6              7                8                 9                   10                11                  12
    # Name Script:
    detailsList[0]+=nameScript
    # Created by: 
    detailsList[1]+=original[original.find("- **Developer name** : ")+len("- **Developer name** : ") : original.find("- [**_Workplace link_**]")-1]
    # -1 is to exclude the \n at the end
    # Created:
    detailsList[2]+=original[original.find("- **Date of modification** : ")+len("- **Date of modification** : ") : original.find("- **File extension**")-1]
    # Workplace link
    detailsList[3]+=original[original.find("- [**_Workplace link_**]")+len("- [**_Workplace link_**]") : original.find("- **Date of modification**")-1]
    # File extension:
    detailsList[4]+=original[original.find("- **File extension** : ")+len("- **File extension** : ") : original.find("- **Use** :")-1]
    # Application suite:
    detailsList[5]+=original[original.find("- **Application suite** : ")+len("- **Application suite** : ") : original.find("- **Module**")-1]
    # Module:
    detailsList[6]+=original[original.find("- **Module** : ")+len("- **Module** : ") : original.find("- **Type** ")-1]
    # Type:
    detailsList[7]+=original[original.find("- **Type** : ")+len("- **Type** : ") : original.find("### **Code :**")-3]
    # Scope:
    detailsList[8]+=str(df.loc[nameScript,'Scope'])
    # Release:
    detailsList[9]+=str(df.loc[nameScript,'Release'])
    # Updated by:
    detailsList[10]+=str(df.loc[nameScript,'Updated by'])
    # Updated:
    detailsList[11]+=str(df.loc[nameScript,'Updated'])
    # Version:
    detailsList[12]+=str(df.loc[nameScript,'Version'])
    details+="\n".join(detailsList)+"\n\n\n"


    # Code ---------------------------------------------
    code="### **Code :**\n"
    code+=original[original.find("```") : original.find("### **Important notes**")]


    # importantNotes -----------------------------
    importantNotes=original[original.find("### **Imp"):]


    # out ------------------------------
    out=whatis+details+code+importantNotes
    

    # output ------------------------------
    os.chdir(outputPath) # cd to the folder of output markdown files
    try:
        with open(nameScript, "w", encoding="utf-8") as output_file:
            output_file.write(out)
            return 'congrats, output succeeded: '+nameScript
    except:
        return 'Something evil\'s lurking in the dark: '+nameScript


#%% step 1 : excel stuffs ----------------------------------------------------
# by default, the excel is in the directory of output
import pandas as pd

# check if there is already existing excel file:
os.chdir(outputPath)
files2=list(file for file in os.listdir(outputPath) if os.path.isfile(os.path.join(outputPath, file)))
flag=True
for file in files2: # little bug: the excel file cannot be opened. If it's opened, there will be a ~$excel.xlsx in the folder
    if file.find('.xlsx')>-1: # .xlsx appears in the file name
        excelName=file
        flag=False # .xlsx exists, then no need of creating a new excel
if flag: # if no existing excel, then create a new one:
    empty=list('' for i in range(len(files)))
    df=pd.DataFrame(data={'file_name':files, 'Scope':empty, 'Release':empty, 'Updated by':empty, 'Updated':list('DD/MM/AAAA' for i in range(len(files))), 'Version':empty, 'Directory':empty})
    df.set_index('file_name', inplace = True)
    os.chdir(outputPath)
    excelName='zexcel.xlsx'
    df.to_excel(excelName) # need module openpyxl. $ pip install openpyxl
    print('Existing excel not found. A new excel is created: '+excelName)
else:
    print('The excel already exists: '+excelName+'\nIt\'s not been modified.')
print('\n')
time.sleep(1)
input("[*] If the excel is filled, press return to proceed to step 2. Warning: the column Directory must be filled.")
print('\n')


#%% output stuffs ----------------------------------------------------
for file in files:
	newmd(file,inputPath,outputPath,excelName)
print('New markdown files are in: '+outputPath)
print('\n')

#%% place md files to their matching directory ------------------------
input('[*] Check the md. If they are ok, press return to proceed to step 3.')
df=pd.read_excel(excelName)
df.set_index('file_name', inplace = True)

files2=list(file for file in os.listdir(outputPath) if os.path.isfile(os.path.join(outputPath, file)) and file.find('.xlsx')==-1) # read files again, in case some of the md are deleted. Needs to exclude the excel
for i in files2: # i is the name of md files
    cmd="cd "+"\""+outputPath+"\""
    os.system(cmd)
    cmd="move "+"\""+i+"\""+" "+"\""+outputPath+"\\"+df.loc[i]["Directory"]+"\""
    os.system(cmd)

# list(dict.fromkeys(df["Directory"].values.tolist())) # turn pandas column to a list, delete duplicates

#%% git add one by one (not git add *)
# $ git add {file_name}
time.sleep(1)
input('[*] Now the md are in the right local folder. Press return to proceed forward to git add')
os.chdir(outputPath)
df=pd.read_excel(excelName) # reread the excel is better than reset_index
# iterate through pandas dataframe: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
for index, row in df.iterrows():
    os.chdir(outputPath)
    os.chdir(row["Directory"])
    cmd="git add "+"\""+row['file_name']+"\""
    print(cmd)
    os.system(cmd)

#%% git commit
commitMessage=input("\n[*] git add succeeded. Type your commit message: ")
cmd="git commit -m "+"\""+commitMessage+"\""
os.system(cmd)
#%% git push
time.sleep(1)
input("[*] push?")
os.system("git push origin main")

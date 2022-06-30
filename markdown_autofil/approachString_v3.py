# based on v2_method3
import os
os.chdir(r"D:\full_stack\py\Markdown\test")


def newmd(nameScript:int)->str:
    #%% read original file ----------------------------------
    fhand=open(nameScript) # type: <class '_io.TextIOWrapper'>
    original=''
    for line in fhand:  # type of line: string
        original+=line


    #%% what is ------------------------------------
    whatis=''
    # find the "what is" part of the original script
    # print(original.find("## **What is")) # 0
    # print(original.find("### **Details")) #81
    whatis+=original[original.find("## **What is"):original.find("### **Details")]


    #%% Details ---------------------------------------
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

    details+="\n".join(detailsList)+"\n\n\n"


    #%% Code ---------------------------------------------
    code="### **Code :**\n"
    code+=original[original.find("```") : original.find("### **Important notes**")]


    #%% importantNotes -----------------------------
    importantNotes=original[original.find("### **Imp"):]


    #%% out ------------------------------
    out=whatis+details+code+importantNotes


    #%% output ------------------------------
    #%% output. rewrite the file
    try:
        with open(nameScript[:len(nameScript)-3]+'_new.md', "w", encoding="utf-8") as output_file:
            output_file.write(out)
            return 'congrats, output succeeded'
    except:
        return 'Something evil\'s lurking in the dark'


fileList=["Attachement size check.md", "AutoFulfill Field.md", "Checksum.md", "Codesearch.md", "Convertir des dates.md", "CSMIDServerRemoteFileImport.md"]
for file in fileList:
	newmd(file)
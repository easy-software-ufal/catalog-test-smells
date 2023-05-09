import os
import csv

testsmells = {}

i = 0

with open('mycsv.csv', 'r', encoding="utf8") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        i+=1
        name = row[7].title()
        #print(row[10] == "TRUE", row[11] == "TRUE", row[12] == "TRUE")

        if(name not in testsmells):
            testsmells[name] = {}
            testsmells[name]["references"] = [{
                "url": row[2],
                "title": row[3],
                "example": row[10] == "TRUE",
                "ce": row[11] == "TRUE",
                "freq": row[12] == "TRUE"
            }]
        else:
            testsmells[name]["references"].append({
                "url": row[2],
                "title": row[3],
                "example": row[10] == "TRUE",
                "ce": row[11] == "TRUE",
                "freq": row[12] == "TRUE"
            })

for root, dirs, files in os.walk("docs\source", topdown=False):
    for name in files:
        path_file = os.path.join(root, name)
        if (path_file.count("\\") == 2 or "generated" in path_file or "_static" in path_file or "index.rst" in path_file or ".rst" not in path_file):
            continue
        
        text = ""
    
        with open(".\\"+path_file, 'r+', encoding="utf-8") as rstfile:
            title = rstfile.readline()[:-1].strip().title()
            text += title + '\n'
            linhas = rstfile.readlines()
            i = 0
            for line in linhas:
                i+=1
                text += line
                if("**References:**:" in line):
                    text+="\n"
                    break
            i+=1
            rstfile.seek(0)
            for lineReference in linhas[i:]:
                for reference in testsmells[title]["references"]:
                    if(reference["url"] in lineReference):
                        text += lineReference[:-1]

                        if(reference["example"]):
                            text += " :octicon:`file-code;1em`"
                        if(reference["ce"]):
                            text += " :octicon:`comment-discussion;1em`"
                        if(reference["freq"]):
                            text += " :octicon:`graph;1em`"
                        text += "\n"

            text+='\n'
            rstfile.seek(0, 0)

            rstfile.write(text)

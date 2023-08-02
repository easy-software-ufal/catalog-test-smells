import csv
import os
from pathlib import Path

def safe_open_w(path):
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w', encoding="utf8")

testsmells = {}


with open('./scripts/allreferences.csv', encoding="utf8") as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        if(row["Name"].title() in testsmells.keys()):
            testsmells[row["Name"].title()]["references"].append(
              {
                "link": row["Reference Title"],
                "title": row["Title"],
                "code_example": row["Code Example"] == "TRUE",
                "causes_effects": row["Causes / Effects"] == "TRUE",
                "frequency": row["Frequency"] == "TRUE",
                "refactor": row["Refactoring"] == "TRUE",
              }
            )
            testsmells[row["Name"].title()]["definitions"].append(row["Definition"])
        else:
            testsmells[row["Name"].title()] = {
              "references": [
                {
                  "link": row["Reference Title"],
                  "title": row["Title"],
                  "code_example": row["Code Example"] == "TRUE",
                  "causes_effects": row["Causes / Effects"] == "TRUE",
                  "frequency": row["Frequency"] == "TRUE",
                  "refactor": row["Refactoring"] == "TRUE",
                }
              ],
              "definitions": [row["Definition"]]
            }

for root, dirs, files in os.walk("docs\source", topdown=False):
    for name in files:
        path_file = os.path.join(root, name)
        if (path_file.count("\\") == 2 or "generated" in path_file or "_static" in path_file or "index.rst" in path_file or ".rst" not in path_file):
            continue
        
        text = ""

        with open(".\\"+path_file, 'r', encoding="utf-8") as rstfile:
            title = rstfile.readline()[:-1].strip().title()
            if(title not in testsmells.keys()):
                print(title)
                continue

            text += title + '\n'
            linhas = rstfile.readlines()
            i = 0
            for line in linhas:
                i+=1
                text += line
                if("* :octicon:`graph;1em` -  Frequency" in line):
                    text+="    * :octicon:`sync;1em` -  Refactoring\n\n"
                    break
            i+=1
            rstfile.seek(0)
            
            testsmells[title]["references"].sort(key=lambda x: x["title"])

            for reference in testsmells[title]["references"]:
                
                text += "* `"+reference["title"]+" <"+reference["link"]+">`_"
                if(reference["code_example"]):
                    text += " :octicon:`file-code;1em`"
                if(reference["causes_effects"]):
                    text += " :octicon:`comment-discussion;1em`"
                if(reference["frequency"]):
                    text += " :octicon:`graph;1em`"
                if(reference["refactor"]):
                    text += " :octicon:`sync;1em`"
                text += "\n"

        with open(".\\"+path_file, 'w', encoding="utf-8") as rstfile:
            rstfile.write(text)



# i = 0

# with open('mycsv.csv', 'r', encoding="utf8") as csvfile:
#     file = csv.reader(csvfile)
#     for row in file:
#         i+=1
#         name = row[7].title()
#         #print(row[10] == "TRUE", row[11] == "TRUE", row[12] == "TRUE")

#         if(name not in testsmells):
#             testsmells[name] = {}
#             testsmells[name]["references"] = [{
#                 "Reference Title": row[2],
#                 "title": row[3],
#                 "example": row[10] == "TRUE",
#                 "ce": row[11] == "TRUE",
#                 "freq": row[12] == "TRUE"
#             }]
#         else:
#             testsmells[name]["references"].append({
#                 "Reference Title": row[2],
#                 "title": row[3],
#                 "example": row[10] == "TRUE",
#                 "ce": row[11] == "TRUE",
#                 "freq": row[12] == "TRUE"
#             })

# for root, dirs, files in os.walk("docs\source", topdown=False):
#     for name in files:
#         path_file = os.path.join(root, name)
#         if (path_file.count("\\") == 2 or "generated" in path_file or "_static" in path_file or "index.rst" in path_file or ".rst" not in path_file):
#             continue
        
#         text = ""
    
#         with open(".\\"+path_file, 'r+', encoding="utf-8") as rstfile:
#             title = rstfile.readline()[:-1].strip().title()
#             text += title + '\n'
#             linhas = rstfile.readlines()
#             i = 0
#             for line in linhas:
#                 i+=1
#                 text += line
#                 if("**References:**:" in line):
#                     text+="\n"
#                     break
#             i+=1
#             rstfile.seek(0)
#             for lineReference in linhas[i:]:
#                 for reference in testsmells[title]["references"]:
#                     if(reference["Reference Title"] in lineReference):
#                         text += lineReference[:-1]

#                         if(reference["example"]):
#                             text += " :octicon:`file-code;1em`"
#                         if(reference["ce"]):
#                             text += " :octicon:`comment-discussion;1em`"
#                         if(reference["freq"]):
#                             text += " :octicon:`graph;1em`"
#                         text += "\n"

#             text+='\n'
#             rstfile.seek(0, 0)

#             rstfile.write(text)

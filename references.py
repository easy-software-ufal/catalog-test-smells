import os
import csv

testsmells = {}

i = 0

with open('MYCS.csv', 'r', encoding="utf8") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        i+=1
        name = row[7].title()
        print(name)
        if(name not in testsmells):
            testsmells[name] = {}
            testsmells[name]["references"] = [(row[2], row[3])]
        else:
            testsmells[name]["references"].append((row[2], row[3]))

for root, dirs, files in os.walk("docs\source", topdown=False):
    for name in files:
        path_file = os.path.join(root, name)
        if (path_file.count("\\") == 2 or "generated" in path_file or "_static" in path_file or "index.rst" in path_file or ".rst" not in path_file):
            continue
        
        text = ""
    
        with open(".\\"+path_file, 'r+', encoding="utf-8") as rstfile:
            title = rstfile.readline()[:-1].strip().title()
            text += title + '\n'
            for line in rstfile.readlines():
                text += line
                if("References:" in line):
                    text+="\n"
                    break
            for reference in testsmells[title]["references"]:
                text += f' * `{reference[1]} <{reference[0]}>`_\n'
            
            text+='\n'
            rstfile.seek(0, 0)

            rstfile.write(text)

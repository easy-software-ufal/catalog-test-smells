import csv
import os
from pathlib import Path

def safe_open_w(path):
  print(path)
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w', encoding="utf8")

testsmells = {}

# {'Category': 'Test semantic/logic', 'Subcategory': 'Other test logic related', 'Name': 'You Do Weird Things to Get at the Code Under Test', 'Sources': '1', 'AKA-ALL': '', 'Code Example': 'FALSE', 'Causes / Effects': 'TRUE', 'Frequency': 'FALSE'}

with open ('./scripts/alltests.csv', encoding="utf8") as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        testsmells[row["Name"].title()] = {"category": row["Category"].replace("/", "-"), "subcategory": row["Subcategory"].replace("/", "-"), "AKA": row["AKA"], "references": [], "definitions": []}

# Reference Title,Title,Source Type,AP/TS,Name,AKA,Definition,Code Example,Causes / Effects,Frequency

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
              }
            )
            testsmells[row["Name"].title()]["definitions"].append(row["Definition"])

txt = Path('./scripts/template.txt').read_text()
cExists = 0
nExists = 0
for name in testsmells.keys():
  filepath = f'./docs/source/{testsmells[name]["category"]}/{testsmells[name]["subcategory"]}/{name.replace("?", "").replace("::", "").replace("/", "-")}.rst'
  exists = os.path.isfile(filepath)
  if(not exists):
    with safe_open_w(filepath) as rstfile:
      
      template = txt.replace("[SMELL NAME]", name)

      references = ""

      definition = ""

      for defi in testsmells[name]["definitions"]:
        if(len(definition) < len(defi)):
            definition = defi
      

      template = template.replace("[DEFINITION]", "* " + definition + "\n")
      haveCodeExample = False
      for reference in testsmells[name]["references"]:
        references += f'* `{reference["title"]} <{reference["link"]}>`_'

        if(reference["code_example"]):
          references += " :octicon:`file-code;1em`"
          haveCodeExample = True
        if(reference["causes_effects"]):
          references += " :octicon:`comment-discussion;1em`"
        if(reference["frequency"]):
          references += " :octicon:`graph;1em`"
        references += "\n"

      if(haveCodeExample):
         template = template.replace("[CODE EXAMPLE]",
"""**Code Example:**

* No code examples yet...
.. TODO CODE EXAMPLE""")
      else:
         template = template.replace("[CODE EXAMPLE]", "")

      template = template.replace("[REFERENCE]", references)

      if(testsmells[name]["AKA"] != ""):
        akas = "**Also Known As:**\n\n"
        akas += "* "+ testsmells[name]["AKA"]
        akas += "\n"
        template = template.replace("[AKA]", akas)
      else:
        template = template.replace("[AKA]", "")
      
      rstfile.write(template)

# with open ('nocodeexamples.csv', encoding="utf8") as csvfile:
#     file = csv.reader(csvfile)
#     next(file)
#     for row in file:
#         name = row[6].title()
#         if(name not in testsmells):
#             testsmells[name] = {}
#             testsmells[name]["category"] = row[0].replace("/", "-")
#             testsmells[name]["subcategory"] = row[1].replace("/", "-")
#             testsmells[name]["references"] = [(row[2], row[3])]
#             if(row[7]!=""):
#                 testsmells[name]["aka"] = [row[7].title()]
#             else:
#                 testsmells[name]["aka"] = []
#             testsmells[name]["definitions"] = [row[8]]
#         else:
#             testsmells[name]["references"].append((row[2], row[3]))
#             if(row[7]!=""):
#                 testsmells[name]["aka"].append(row[7])
#             testsmells[name]["definitions"].append(row[8])

# txt = Path('./mytemplate.txt').read_text()
# for name in testsmells.keys():
#     with safe_open_w(f'./docs/source/testsmells/{testsmells[name]["category"]}/{testsmells[name]["subcategory"]}/{name.replace("?", "").replace("::", "").replace("/", "-")}.rst') as rstfile:
#         template = txt.replace("[SMELLNAME]", name)

#         definitions = ""
#         for definition in testsmells[name]["definitions"]:
#             definitions += f'* {definition}\n'

#         template = template.replace("[DEFINITION]", definitions)

#         if(len(testsmells[name]["aka"])>0):
#             akas = "Also Known As:\n\n"
#             for aka in testsmells[name]["aka"]:
#                 akas += f'* {aka}\n'
            
#             template = template.replace("[AKA]", akas)
#         else:
#             template = template.replace("[AKA]", "")

#         references = ""
#         for reference in testsmells[name]["references"]:
#             references += f'* `{reference[0]} <{reference[1]}>`_\n'
        
#         template = template.replace("[REFERENCES]", references)

#         rstfile.write(template)

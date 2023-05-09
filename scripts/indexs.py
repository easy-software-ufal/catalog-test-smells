import os
from pathlib import Path

txt = Path('./scripts/index.txt').read_text()

for root, dirs, files in os.walk(".\docs\\source", topdown=False):
  for name in dirs:
    if(name == "_static"): continue
    if(root.count("\\") == 2): continue

    path = os.path.join(root, name)

    template = txt.replace("[SUBCATEGORY]", name)

    for file in os.listdir(path):
      if(file.endswith(".rst") and file != "index.rst"):
        template += f"    {file[:-4]}\n"
    
    template += "\n"

    with open(f"{path}\\index.rst", "w") as index:
      index.write(template)
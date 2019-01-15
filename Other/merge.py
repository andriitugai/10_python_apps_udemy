pattern = "*.txt"
path = "."

import glob
from datetime import datetime

now = datetime.now()
output_filename = now.strftime("%Y-%m-%d-%H-%M-%S-%f")
print(output_filename)

source_files = glob.glob(pattern)

with open(output_filename,"w") as destination:
    for file_name in source_files:
        with open(file_name) as source:
            content = source.read()
            destination.write(content+'\n')

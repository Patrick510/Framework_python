import os
from tqdm import tqdm

directory = os.listdir(r"C:\Users\Patrick Dias\Downloads\ESTOQUE")

for file in tqdm(directory):
  print(file)
print(directory)
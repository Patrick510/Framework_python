import os
from tqdm import tqdm
import time

directory = os.listdir(r"C:\Users\Patrick Dias\Downloads\ESTOQUE")

for file in tqdm(directory, colour='blue'):
  print(file)
  time.sleep(0.1)
print(directory)
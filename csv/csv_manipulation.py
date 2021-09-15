import csv
from pathlib import Path
fileToBeRead = Path(__file__).parent / "innovators.csv"

innovators = []
with fileToBeRead.open('r') as file:
  spamreader = csv.reader(file, delimiter = ';', skipinitialspace=True)
  for row in spamreader:
    print(f'{row}')
    innovators.append(row)

fileToBeWritten = Path(__file__).parent / "innovators_tobewritten.csv"
with fileToBeWritten.open('w', newline='') as file:
  innovator_writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  # for row in innovators:
  innovator_writer.writerows(innovators)

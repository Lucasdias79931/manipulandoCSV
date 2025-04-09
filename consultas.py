import os
import pandas

class Dataset:
    def __init__(self):
        self.allDataset = list()
        #Salva os caminhos para os datasest
        self.sizeDatasetes = 0

    def varredura(self, allDatasetPath):
        try:
            for dirpath, _, filenames in os.walk(allDatasetPath):
                for file in filenames:
                    if file.endswith(".csv"):
                        full_path = os.path.join(dirpath, file)
                        self.allDataset.append(full_path)
                        self.sizeDatasetes += 1
        except Exception as e:
            print(e)
import sys
import os
import pandas as pd

# Verifica se o nome do arquivo foi passado como argumento
if len(sys.argv) < 2:
    print("Argumentos faltando!")
    print("Passe o nome do arquivo .csv")
    sys.exit(1)

arquivo_csv = sys.argv[1]

# Verifica se o arquivo existe
if not os.path.exists(arquivo_csv):
    print("Arquivo passado incorretamente!")
    sys.exit(1)

# Lê o CSV com pandas
try:
    df = pd.read_csv(arquivo_csv)
    print("Colunas disponíveis no CSV:", df.columns.tolist())

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    sys.exit(1)



try:
    
    

    tuplas = [tuple(linha) for linha in df.to_numpy()]
    print(tuplas[0])
except Exception as e:
    print(f"Ocorreu um erro: {e}")

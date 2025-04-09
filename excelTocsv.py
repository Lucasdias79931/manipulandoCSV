import pandas as pd
import os

here = os.path.abspath(os.path.dirname(__file__))

# Lê o arquivo Excel

df = pd.read_excel(os.path.join(here, "Agregados_por_setores_basico_BR.xlsx"))

# Salva como CSV
df.to_csv(os.path.join(here, "Agregados_por_setores_basico_BR.csv"), index=False)

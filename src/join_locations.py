import pandas as pd
import matplotlib.pyplot as plt

# MAN = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/concatenated_series_MAN_30prec_3y.csv')
# AFL = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/AFL/experiments/30perc_reduction/concatenated_series_AFL_30prec_3y.csv')
# ALP = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/ALP/experiments/30perc_reduction/concatenated_series_ALP_30prec_3y.csv')
# FEC = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/FEC/experiments/30perc_reduction/concatenated_series_FEC_30prec_3y.csv')
# CAX = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/CAX/experiments/30perc_reduction/concatenated_series_CAX_30prec_3y.csv')

# # Adicionando a coluna 'location' a cada dataframe
# MAN['location'] = 'MAN'
# AFL['location'] = 'AFL'
# ALP['location'] = 'ALP'
# FEC['location'] = 'FEC'
# CAX['location'] = 'CAX'

# # Concatenando os dataframes
# df_concatenado = pd.concat([MAN, AFL, ALP, FEC, CAX], ignore_index=True)

# df_concatenado['total_carbon'] = df_concatenado[['cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']].sum(axis=1)

# df_concatenado['date_dateformat'] = pd.to_datetime(df_concatenado['Date'])

# print(df_concatenado.columns)
# df_concatenado.to_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/ALL_LOCATIONS/concatenated_series_ALL_LOCATIONS_30prec_3y.csv', index=False)

df = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/ALL_LOCATIONS/concatenated_series_ALL_LOCATIONS_30prec_3y.csv')

# Criar subplots para cada variável
plt.figure(figsize=(18, 20))

# Número de linhas e colunas
num_rows = 1
num_cols = 1

# Criar subplots para cada variável
fig, axes = plt.subplots(num_rows, num_cols, sharex=True)


for location in set(df['location']):
    # Filtrar o DataFrame para a localização atual
    df_loc = df[df['location'] == location]
    

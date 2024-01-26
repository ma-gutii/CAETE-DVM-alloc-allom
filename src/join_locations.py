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

# Lista de variáveis a serem plotadas
variables_to_plot = ['npp', 'total_carbon', 'ls', 'evapm']

for variable in variables_to_plot:
    # Número de linhas e colunas
    num_rows = len(set(df['location']))
    num_cols = 1

    # Criar subplots para cada variável
    plt.figure(figsize=(18, 20))

    # Criar subplots para cada variável
    fig, axes = plt.subplots(num_rows, num_cols, sharex=True)

    for i, location in enumerate(set(df['location'])):
        # Filtrar o DataFrame para a localização atual e a variável atual
        df_loc_var = df[(df['location'] == location) & (df[variable].notnull())]

        # Plotar cada variável no subplot correspondente
        axes[i].plot(df_loc_var['date_dateformat'], df_loc_var[variable], label=location, linewidth=0.5, alpha=0.7)
        axes[i].set_ylabel(variable, fontsize=18)
        axes[i].legend()

    # Rotacionar os rótulos no eixo x
    plt.xticks(rotation=45, ha='right')

    # Ajustar o layout para melhor espaçamento
    plt.tight_layout()

    # Salvar o gráfico como um arquivo PNG
    plt.savefig(f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/ALL_LOCATIONS/{variable}_multiple_locations.png')

    # Fechar a figura atual para criar uma nova para a próxima variável
    plt.close()
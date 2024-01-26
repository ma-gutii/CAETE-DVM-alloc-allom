import pandas as pd
import os
import matplotlib.pyplot as plt
import glob

base_path = "/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/"
# path_regclim = os.path.join(base_path, f"experiments/MAN_regularclimate/gridcell186-239/concatenated_series_MAN_regularclimate.csv")

# df = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/concatenated_series_MAN_allprec_3y.csv')
# df_regclim = pd.read_csv(path_regclim)

# df_regclim['perc'] = 0

# # Concatenar os DataFrames
# result_df = pd.concat([df, df_regclim], ignore_index=True)

# result_df['total_carbon'] = result_df[['cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']].sum(axis=1)

# result_df['date_dateformat'] = pd.to_datetime(result_df['Date'])


# # # # Agora, result_df contém ambos os DataFrames concatenados
# # # # Você pode salvar result_df em um novo arquivo CSV se necessário
# result_df.to_csv(os.path.join(base_path, "experiments/concatenated_series_MAN_allprec_3y.csv"), index=False)

df_allperc = pd.read_csv(os.path.join(base_path, "experiments/concatenated_series_MAN_allprec_3y.csv"))

niveis_perc = df_allperc['perc'].unique()
# Criando subplots para cada nível
fig, axs = plt.subplots(len(niveis_perc), 1, figsize=(10, 5 * len(niveis_perc)), sharex=True)

# Iterando sobre cada nível e criando o gráfico correspondente
for i, nivel in enumerate(niveis_perc):
    dados_nivel = df_allperc[df_allperc['perc'] == nivel]
    axs[i].plot(dados_nivel['date_dateformat'], dados_nivel['npp'])
    axs[i].set_title(f'Nível {nivel}')
    axs[i].set_ylabel('npp')

# Adicionando rótulos ao eixo x ao último subplot
axs[-1].set_xlabel('date_dateformat')

# Adicionando um título geral para a figura
fig.suptitle('Gráficos de NPP para cada nível de perc')

# Salvando a figura em um arquivo PNG
plt.savefig('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/graficos_npp_por_nivel.png')

# Exibindo a figura (opcional)
plt.show()
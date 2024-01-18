# Import libraries
import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


while True:
    grd_acro = 'MAN' #input('Gridcell acronym [ALP, FEC, MAN, CAX, NVX]: ')

    if grd_acro == 'ALP':
        grd = '188-213'
        break
    elif grd_acro == 'FEC':
        grd = '200-225'
        break
    elif grd_acro == 'MAN':
        grd = '186-239'
        break
    elif grd_acro == 'CAX':
        grd = '183-257'
        break
    elif grd_acro == 'NVX':
        grd = '210-249'
        break
    else:
        print('This acronym does not correspond')
        break

main_path = f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/state_start/'
       
# Input the main run name
main_run_name = 'MAN_save_spin' #input('Main run name: ')

# Create a dictionary to store the temporal series
dfs = {}

# Loop through the 10 runs
for i in range(1, 10 + 1):
    run_name = f'{main_run_name}_{i}'

    # Navigate to the specified folder to access spins
    os.chdir(f'{main_path}{run_name}/gridcell{grd}')

    # Read the CSV file corresponding to the concatenated series
    df = pd.read_csv(f'{main_path}{run_name}/gridcell{grd}/csv/concatenated_series_{run_name}.csv')

    # Convert the 'Date' column to the datetime data type
    df['Date'] = pd.to_datetime(df['Date'])

    # Store the DataFrame in the dictionary
    dfs[run_name] = df

# Lista para armazenar as séries temporais
series = []

# Loop através do dicionário dfs para obter cada série temporal
for run_name, df in dfs.items():
    # Converta a coluna 'Date' para o formato de datetime, se já não estiver
    df['Date'] = pd.to_datetime(df['Date'])

    series.append(df['npp'].values)

# Converter a lista de listas em um array NumPy
series_array = np.array(series)

# Calcular a média ao longo do eixo 0 (média de cada ponto de dado ao longo das séries)
media_geral = np.mean(series_array, axis=0)

# Agora, media_geral contém a média geral das suas séries temporais para cada ponto de dado.
# O eixo x será as datas presentes na coluna 'Date' do DataFrame
datas = dfs[next(iter(dfs))]['Date']  # Assume que todas as séries têm as mesmas datas

# Plotar a média em relação ao tempo
plt.plot(datas, media_geral, label='Média Geral')
plt.xlabel('Data')
plt.ylabel('Valor Médio')
plt.title('Média Geral das Séries Temporais')
plt.legend()

# Salvar os gráficos como um único arquivo PNG
plt.savefig(f'{main_path}/timeseries_mean_spinup.png')

plt.show()

# Calcular a diferença para cada série em relação à média geral
diferencas = series_array - media_geral

# Calcular a variância para cada série em relação à média geral
variancias = np.var(diferencas, axis=1)

# Calcular o desvio padrão para cada série em relação à média geral
desvios_padrao = np.std(series_array, axis=1)

# Identificar a série com a maior variância
indice_maior_variancia = np.argmax(variancias)
serie_maior_variancia = dfs[list(dfs.keys())[indice_maior_variancia]]

print(f"Série com Maior Variância em Relação à Média Geral: {list(dfs.keys())[indice_maior_variancia]}")

# Identificar a série com a maior variância
indice_menor_variancia = np.argmin(variancias)
serie_menor_variancia = dfs[list(dfs.keys())[indice_menor_variancia]]

print(f"Série com Menor Variância em Relação à Média Geral: {list(dfs.keys())[indice_menor_variancia]}")

# Obter o valor de 'ls' para a série de maior variância
valor_ls_maior_variancia = serie_maior_variancia['ls'].values[0]

print(f"Valor de 'ls' para a Série com Maior Variância: {valor_ls_maior_variancia}")

# Obter o valor de 'ls' para a série de menor variância
valor_ls_menor_variancia = serie_menor_variancia['ls'].values[0]

print(f"Valor de 'ls' para a Série com Meenor Variância: {valor_ls_menor_variancia}")

# Identificar a série com o maior desvio padrão
indice_maior_desvio_padrao = np.argmax(desvios_padrao)
serie_maior_desvio_padrao = dfs[list(dfs.keys())[indice_maior_desvio_padrao]]

# Identificar a série com o menor desvio padrão

indice_menor_desvio_padrao = np.argmin(desvios_padrao)
serie_menor_desvio_padrao = dfs[list(dfs.keys())[indice_menor_desvio_padrao]]
print(f"Série com Maior Desvio Padrão em Relação à Média Geral: {list(dfs.keys())[indice_maior_desvio_padrao]}")
print(f"Série com Menor Desvio Padrão em Relação à Média Geral: {list(dfs.keys())[indice_menor_desvio_padrao]}")

## Calcular o desvio padrão para cada série em relação à média geral
desvios_padrao = np.std(series_array, axis=0)

# Identificar a série com o maior desvio padrão
indice_maior_desvio_padrao = np.argmax(desvios_padrao)
serie_maior_desvio_padrao = dfs[list(dfs.keys())[indice_maior_desvio_padrao]]

# Identificar a série com o menor desvio padrão
indice_menor_desvio_padrao = np.argmin(desvios_padrao)
serie_menor_desvio_padrao = dfs[list(dfs.keys())[indice_menor_desvio_padrao]]

# Calcular o desvio padrão para a série com o maior desvio padrão
desvio_padrao_maior = np.std(serie_maior_desvio_padrao['npp'].values)

# Calcular o desvio padrão para a série com o menor desvio padrão
desvio_padrao_menor = np.std(serie_menor_desvio_padrao['npp'].values)

# Plotar a média geral
plt.plot(datas, media_geral, label='Média Geral')

# Adicionar sombra representando o desvio padrão para a série de maior desvio padrão
plt.fill_between(datas,
                 media_geral - desvio_padrao_maior,
                 media_geral + desvio_padrao_maior, alpha=0.2, label='Desvio Padrão (Maior)')

# Adicionar sombra representando o desvio padrão para a série de menor desvio padrão
plt.fill_between(datas,
                 media_geral - desvio_padrao_menor,
                 media_geral + desvio_padrao_menor, alpha=0.2, label='Desvio Padrão (Menor)')

plt.xlabel('Data')
plt.ylabel('Valores')
plt.title('Média Geral e Desvio Padrão para Séries Temporais')
plt.legend()

# Salvar os gráficos como um único arquivo PNG
plt.savefig(f'{main_path}/timeseries_mean_std_shade_spinup.png')

plt.show()

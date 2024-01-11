# Import libraries
import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

grd_acro = input('Gridcell acronym [ALP, FEC, MAN, CAX, NVX]: ')

# Prompt the user to determine if the script is running on a server or locally
while True:
    server = 'y'#input('Are you running in the server? y/n ')

    # Set the main_path accordingly based on the user's response
    if server == 'y':
        main_path = f'/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{grd_acro}/spinup_runs/'
        break
    elif server == 'n':
        # Set the main_path accordingly for local machine
        main_path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/'
        break

# Input the main run name
main_run_name = input('Main run name: ')

# Input the number of runs
run_number = int(input('Number of runs: '))

# Input the latitude and longitude from grd
grd_name = input('lat and long from grd: ')

# Create a dictionary to store DataFrames
dfs = {}

# Loop through the specified number of runs
for i in range(1, run_number + 1):
    run_name = f'{main_run_name}_{i}'

    # Navigate to the specified folder to access spins
    os.chdir(f'{main_path}{run_name}/gridcell{grd_name}')

    # Read the CSV file corresponding to the concatenated series
    df = pd.read_csv(f'{main_path}{run_name}/gridcell{grd_name}/concatenated_series_{run_name}.csv')

    # Convert the 'Date' column to the datetime data type
    df['Date'] = pd.to_datetime(df['Date'])

    # Store the DataFrame in the dictionary
    dfs[run_name] = df

# Configuração do layout do gráfico
# fig, ax = plt.subplots(figsize=(15, 8))
fig, (ax_ls, ax_npp, ax_photo) = plt.subplots(nrows=3, figsize = (15,8), sharex=True)

# Iterar sobre as rodadas e plotar cada uma
for run_name, df in dfs.items():
    ax_ls.plot(df['Date'], df['ls'], label=f'{run_name} - ls', alpha = 0.8, linewidth = 1.)
    ax_npp.plot(df['Date'], df['npp'], label=f'{run_name} - npp', alpha = 0.5, linewidth = 0.6)
    ax_photo.plot(df['Date'], df['photo'], label=f'{run_name} - photo', alpha = 0.5, linewidth = 0.6)

# Adicionar rótulos e título aos subplots
ax_ls.set_ylabel('ls')
ax_ls.set_title('Time Series of ls for All Runs')

ax_ls.set_ylabel('photo')
ax_ls.set_title('Time Series of photo for All Runs')

ax_npp.set_xlabel('Date')
ax_npp.set_ylabel('npp')
ax_npp.set_title('Time Series of npp for All Runs')

# Adicionar legendas aos subplots
ax_ls.legend()
ax_npp.legend()
ax_photo.legend()

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Salvar os gráficos como arquivos PNG separados
fig.savefig(f'{main_path}/timeseries_{main_run_name}.png')

# Exibir os gráficos
plt.show()

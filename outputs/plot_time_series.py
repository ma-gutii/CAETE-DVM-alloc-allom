import pandas as pd
import matplotlib.pyplot as plt
import os

run_name = input('run name: ')
# Leia o arquivo CSV
data = pd.read_csv('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235/concatenated_series_all_spins.csv'.format(run_name))

# Imprima uma pequena parte dos dados
print(data.head())


# Converta a coluna Date para o tipo de dado datetime se ainda não estiver
data['Date'] = pd.to_datetime(data['Date'])

# Plote a série temporal para 'NPP' em relação à coluna Date
plt.plot(data['Date'], data['NPP'])
plt.xlabel('Date')
plt.ylabel('NPP')
plt.title('Time Series of NPP')

plt.savefig('timeseries_{}.png'.format(run_name))

# Obtém o diretório do script (assumindo que o script está no mesmo diretório que o CSV)
script_directory = os.path.dirname(os.path.realpath(__file__))

# Salva a figura no mesmo diretório do script
plt.savefig(os.path.join(script_directory, 'timeseries_{}.png'.format(run_name)))
import pandas as pd
import matplotlib.pyplot as plt

# Leia o arquivo CSV
data = pd.read_csv('/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/test_vel2/gridcell175-235/concatenated_series_all_spins.csv')

# Imprima uma pequena parte dos dados
print(data.head())

# Converta a coluna Date para o tipo de dado datetime se ainda não estiver
data['Date'] = pd.to_datetime(data['Date'])

# Plote a série temporal para 'NPP' em relação à coluna Date
plt.plot(data['Date'], data['NPP'])
plt.xlabel('Date')
plt.ylabel('NPP')
plt.title('Time Series of NPP')
plt.show()

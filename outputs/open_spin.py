# import numpy as np
# import joblib
# import os
# import matplotlib.pyplot as plt

# run_name = input('run name: ')
# path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # Navegue para a pasta
# os.chdir(path)

# # Liste os arquivos e diretórios na pasta
# conteudo = os.listdir()
# for item in conteudo:
#     print(item)

# # Inicialize uma lista para armazenar todas as séries temporais
# all_series = []

# # Itere sobre os spins desejados (de 12 a 19)
# for spin in range(12, 20):
#     # Carregue os dados do spin atual
#     with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
#         dt = joblib.load(fh)

#     # Obtenha a série temporal NPP do spin atual
#     npp_series = dt.get('npp', [])

#     # Adicione a série temporal à lista
#     all_series.append(npp_series)

# # Encontre o comprimento máximo entre as séries temporais
# max_length = max(len(series) for series in all_series)

# # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# all_series = [np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan) for series in all_series]

# # Concatene as séries temporais
# concatenated_series = np.concatenate(all_series, axis=0)

# # Plote a série temporal concatenada
# plt.plot(concatenated_series)
# plt.title('NPP for spins 12 to 19')
# plt.show()




# import numpy as np
# import joblib
# import os
# import matplotlib.pyplot as plt

# run_name = input('run name: ')
# path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # Navegue para a pasta
# os.chdir(path)

# # Liste os arquivos e diretórios na pasta
# conteudo = os.listdir()
# for item in conteudo:
#     print(item)

# # Inicialize uma lista para armazenar todas as séries temporais
# all_series = []

# # Itere sobre os spins desejados (de 12 a 19)
# for spin in range(12, 20):
#     # Carregue os dados do spin atual
#     with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
#         dt = joblib.load(fh)

#     # Obtenha a série temporal NPP do spin atual
#     npp_series = dt.get('npp', [])

#     # Adicione a série temporal à lista
#     all_series.append(npp_series)

# # Encontre o comprimento máximo entre as séries temporais
# max_length = max(len(series) for series in all_series)

# # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# all_series = [np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan) for series in all_series]

# # Concatene as séries temporais
# concatenated_series = np.concatenate(all_series, axis=0)

# # Plote a série temporal concatenada
# plt.plot(concatenated_series)
# plt.title('NPP for spins 12 to 19')
# plt.show()







import joblib
import os


run_name = input('run name: ')

path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# Navegue para a pasta
os.chdir(path)

# Liste os arquivos e diretórios na pasta
conteudo = os.listdir()
for item in conteudo:
    print(item)

spin = input('which spin?')

with open("spin{}.pkz".format(spin), 'rb') as fh:
   dt = joblib.load(fh)
print(dt.keys()) # list the available keys for the ouputs
# PLot some variables
import matplotlib.pyplot as plt
plt.plot(dt['npp'])
plt.title('NPP')  # Adicione um título para o gráfico npp
plt.show()

plt.plot(dt['photo'])
plt.title('PH')  # Adicione um título para o gráfico npp
plt.show()

plt.plot(dt['ar'])

plt.title('ar')  # Adicione um título para o gráfico npp
plt.show()

plt.plot(dt['rm'])

plt.title('rm')  # Adicione um título para o gráfico npp
plt.show()

plt.plot(dt['rg'])

plt.title('rg')  # Adicione um título para o gráfico npp
plt.show()


plt.plot(dt['cleaf'])
plt.title('Gráfico de Cleaf')  # Adicione um título para o gráfico cleaf
plt.show()

plt.plot(dt['cwood'])
plt.title('Gráfico de Cwood')  # Adicione um título para o gráfico cwood
plt.show()

plt.plot(dt['croot'])
plt.title('Gráfico de Croot')  # Adicione um título para o gráfico croot
plt.show()

plt.plot(dt['csap'])
plt.title('Gráfico de Sapwood')  # Adicione um título para o gráfico croot
plt.show()

plt.plot(dt['cheart'])
plt.title('Gráfico de Heartwood')  # Adicione um título para o gráfico croot
plt.show()

plt.plot(dt['csto'])
plt.title('Gráfico de storage')  # Adicione um título para o gráfico croot
plt.show()	


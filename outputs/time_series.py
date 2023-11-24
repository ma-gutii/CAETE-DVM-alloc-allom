import numpy as np
import joblib
import os
import pandas as pd

run_name = input('run name: ')
path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# Navegue para a pasta
os.chdir(path)

# Inicialize uma lista para armazenar todas as séries temporais e datas
all_series = []
all_dates = []
all_spins = []

# Intervalo de datas para cada spin
run_breaks_hist = [('19790101', '19801231'),
                   ('19810101', '19821231'),
                   ('19830101', '19841231'),
                   ('19850101', '19861231'),
                   ('19870101', '19881231'),
                   ('19890101', '19901231'),
                   ('19910101', '19921231'),
                   ('19930101', '19941231'),
                   ('19950101', '19961231'),
                   ('19970101', '19981231'),
                   ('19990101', '20001231'),
                   ('20010101', '20021231'),
                   ('20030101', '20041231'),
                   ('20050101', '20061231'),
                   ('20070101', '20081231'),
                   ('20090101', '20101231'),
                   ('20110101', '20121231'),
                   ('20130101', '20141231'),
                   ('20150101', '20161231')]

# Itere sobre todos os spins disponíveis
for spin, (start_date, end_date) in enumerate(run_breaks_hist, start=1):
    # Carregue os dados do spin atual
    with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
        dt = joblib.load(fh)

    # Obtenha a série temporal NPP do spin atual e suas datas
    npp_series = dt.get('npp', [])
    date_index = pd.date_range(start=start_date, end=end_date, freq='D')

    # Adicione a série temporal, datas e o número do spin às listas
    all_series.extend(npp_series)
    all_dates.extend(date_index)
    all_spins.extend([spin] * len(date_index))

# Crie um DataFrame com as séries temporais, datas e números de spin
df = pd.DataFrame({'Spin': all_spins, 'Date': all_dates, 'NPP': all_series})

# Salve o DataFrame em um arquivo CSV
df.to_csv('concatenated_series_all_spins.csv', index=False)


# import numpy as np
# import joblib
# import os
# import pandas as pd

# run_name = input('run name: ')
# path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # Navegue para a pasta
# os.chdir(path)

# # Inicialize uma lista para armazenar todas as séries temporais e datas
# all_series = []
# all_dates = []

# # Intervalo de datas para cada spin
# run_breaks_hist = [('19790101', '19801231'),
#                    ('19810101', '19821231'),
#                    ('19830101', '19841231'),
#                    ('19850101', '19861231'),
#                    ('19870101', '19881231'),
#                    ('19890101', '19901231'),
#                    ('19910101', '19921231'),
#                    ('19930101', '19941231'),
#                    ('19950101', '19961231'),
#                    ('19970101', '19981231'),
#                    ('19990101', '20001231'),
#                    ('20010101', '20021231'),
#                    ('20030101', '20041231'),
#                    ('20050101', '20061231'),
#                    ('20070101', '20081231'),
#                    ('20090101', '20101231'),
#                    ('20110101', '20121231'),
#                    ('20130101', '20141231'),
#                    ('20150101', '20161231')]

# # Itere sobre todos os spins disponíveis
# for spin, (start_date, end_date) in enumerate(run_breaks_hist, start=1):
#     # Carregue os dados do spin atual
#     with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
#         dt = joblib.load(fh)

#     # Obtenha a série temporal NPP do spin atual e suas datas
#     npp_series = dt.get('npp', [])
#     date_index = pd.date_range(start=start_date, end=end_date, freq='D')

#     # Adicione a série temporal e datas às listas
#     all_series.extend(npp_series)
#     all_dates.extend(date_index)

# # Crie um DataFrame com as séries temporais e datas
# df = pd.DataFrame({'Date': all_dates, 'NPP': all_series})

# # Salve o DataFrame em um arquivo CSV
# df.to_csv('concatenated_series_all_spins.csv', index=False)


# # import numpy as np
# # import joblib
# # import os
# # import pandas as pd

# # run_name = input('run name: ')
# # path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # # Navegue para a pasta
# # os.chdir(path)

# # # Inicialize uma lista para armazenar todas as séries temporais
# # all_series = []

# # # Intervalo de datas para cada spin
# # run_breaks_hist = [('19790101', '19801231'),
# #                    ('19810101', '19821231'),
# #                    ('19830101', '19841231'),
# #                    ('19850101', '19861231'),
# #                    ('19870101', '19881231'),
# #                    ('19890101', '19901231'),
# #                    ('19910101', '19921231'),
# #                    ('19930101', '19941231'),
# #                    ('19950101', '19961231'),
# #                    ('19970101', '19981231'),
# #                    ('19990101', '20001231'),
# #                    ('20010101', '20021231'),
# #                    ('20030101', '20041231'),
# #                    ('20050101', '20061231'),
# #                    ('20070101', '20081231'),
# #                    ('20090101', '20101231'),
# #                    ('20110101', '20121231'),
# #                    ('20130101', '20141231'),
# #                    ('20150101', '20161231')]

# # # Itere sobre todos os spins disponíveis
# # for spin, (start_date, end_date) in enumerate(run_breaks_hist, start=1):
# #     # Carregue os dados do spin atual
# #     with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
# #         dt = joblib.load(fh)

# #     # Obtenha a série temporal NPP do spin atual
# #     npp_series = dt.get('npp', [])

# #     # Adicione a série temporal à lista
# #     all_series.append((npp_series, pd.date_range(start=start_date, end=end_date, freq='D')))

# # # Encontre o comprimento máximo entre as séries temporais
# # max_length = max(len(series) for series, _ in all_series)

# # # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# # all_series_padded = [
# #     (np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan), date_index)
# #     for series, date_index in all_series
# # ]

# # # Converta a lista de séries temporais em um DataFrame do pandas
# # columns = [f'Spin_{spin:02d}' for spin in range(1, len(run_breaks_hist) + 1)]
# # df = pd.DataFrame({column: series for series, _ in all_series_padded for column in columns})

# # # Adicione a série temporal diária ao DataFrame
# # df['Date'] = all_series_padded[0][1]  # Usa as datas do primeiro spin

# # # Reorganize as colunas para que 'Date' seja a primeira
# # df = df[['Date'] + columns]

# # # Salve o DataFrame em um arquivo CSV
# # df.to_csv('concatenated_series_with_dates.csv', index=False)

# # # import numpy as np
# # # import joblib
# # # import os
# # # import pandas as pd

# # # run_name = input('run name: ')
# # # path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # # # Navegue para a pasta
# # # os.chdir(path)

# # # # Inicialize uma lista para armazenar todas as séries temporais
# # # all_series = []

# # # # Itere sobre todos os spins disponíveis
# # # for spin in range(1, 20):
# # #     # Carregue os dados do spin atual
# # #     with open("spin{:02d}.pkz".format(spin), 'rb') as fh:
# # #         dt = joblib.load(fh)

# # #     # Obtenha a série temporal NPP do spin atual
# # #     npp_series = dt.get('npp', [])

# # #     # Adicione a série temporal à lista
# # #     all_series.append(npp_series)

# # # # Encontre o comprimento máximo entre as séries temporais
# # # max_length = max(len(series) for series in all_series)

# # # # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# # # all_series_padded = [np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan) for series in all_series]

# # # # Converta a lista de séries temporais em um DataFrame do pandas
# # # columns = [f'Spin_{spin:02d}' for spin in range(1, 20)]
# # # df = pd.DataFrame(np.vstack(all_series_padded).T, columns=columns)

# # # # Adicione a série temporal diária ao DataFrame
# # # idxT1 = pd.date_range("2015-01-01", "2016-12-31", freq='D')
# # # df['Date'] = idxT1

# # # # Reorganize as colunas para que 'Date' seja a primeira
# # # df = df[['Date'] + columns]

# # # # Salve o DataFrame em um arquivo CSV
# # # df.to_csv('concatenated_series_all_spins.csv', index=False)

# # # # import numpy as np
# # # # import joblib
# # # # import os
# # # # import pandas as pd

# # # # run_name = input('run name: ')
# # # # path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # # # # Navegue para a pasta
# # # # os.chdir(path)

# # # # # Inicialize uma lista para armazenar todas as séries temporais
# # # # all_series = []

# # # # with open("spin19.pkz", 'rb') as fh:
# # # #     dt = joblib.load(fh)

# # # #     # Obtenha a série temporal NPP do spin atual
# # # #     npp_series = dt.get('npp', [])

# # # #     # Adicione a série temporal à lista
# # # #     all_series.append(npp_series)

# # # # # Encontre o comprimento máximo entre as séries temporais
# # # # max_length = max(len(series) for series in all_series)

# # # # # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# # # # all_series_padded = [np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan) for series in all_series]

# # # # # Converta a lista de séries temporais em um DataFrame do pandas
# # # # df = pd.DataFrame(np.vstack(all_series_padded).T, columns=[f'Spin_19'])

# # # # # Adicione uma nova coluna com a série temporal diária
# # # # start_date = pd.to_datetime('20150101', format='%Y%m%d')
# # # # end_date = pd.to_datetime('20161231', format='%Y%m%d')
# # # # daily_date_range = pd.date_range(start_date, end_date, freq='D')

# # # # df['Date'] = daily_date_range

# # # # # Reorganize as colunas para ter a coluna 'Date' no início
# # # # df = df[['Date'] + [col for col in df.columns if col != 'Date']]

# # # # # Salve o DataFrame em um arquivo CSV
# # # # df.to_csv('concatenated_series.csv', index=False)


# # # # # import numpy as np
# # # # # import joblib
# # # # # import os
# # # # # import matplotlib.pyplot as plt
# # # # # import pandas as pd

# # # # # run_name = input('run name: ')
# # # # # path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/outputs/{}/gridcell175-235'.format(run_name)

# # # # # # Navegue para a pasta
# # # # # os.chdir(path)


# # # # # # Inicialize uma lista para armazenar todas as séries temporais
# # # # # all_series = []


# # # # # with open("spin19.pkz", 'rb') as fh:
# # # # #     dt = joblib.load(fh)

# # # # #     # Obtenha a série temporal NPP do spin atual
# # # # #     npp_series = dt.get('npp', [])

# # # # #     # Adicione a série temporal à lista
# # # # #     all_series.append(npp_series)

# # # # # # Encontre o comprimento máximo entre as séries temporais
# # # # # max_length = max(len(series) for series in all_series)

# # # # # # Preencha as séries temporais com valores nulos se forem mais curtas que o comprimento máximo
# # # # # all_series_padded = [np.pad(series, (0, max_length - len(series)), mode='constant', constant_values=np.nan) for series in all_series]

# # # # # # Converta a lista de séries temporais em um DataFrame do pandas
# # # # # df = pd.DataFrame(np.vstack(all_series_padded).T, columns=[f'Spin_19'])

# # # # # # Salve o DataFrame em um arquivo CSV
# # # # # df.to_csv('concatenated_series.csv', index=False)


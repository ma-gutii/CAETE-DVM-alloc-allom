import bz2
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Defina os anos inicial e final
start_year = 1979
end_year = 2016  # Ajustado para 2016 para corresponder aos dados fornecidos

# Leia o arquivo CSV com a coluna 'Date' no formato 'ano-mes-dia'
caminho_arquivo_csv = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/concatenated_series_MAN_10prec_3y.csv'  # Substitua pelo caminho real do seu arquivo CSV
df_dates = pd.read_csv(caminho_arquivo_csv)
dates = pd.to_datetime(df_dates['Date'], format='%Y-%m-%d')
print(len(dates))
# # Substitua 'seuarquivo.pbz2' e 'saida_pr.csv' pelos caminhos reais dos seus arquivos
caminho_arquivo_pbz2 = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/input/central/input_data_186-239.pbz2'

caminho_saida_csv = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/prec_values.csv'

with bz2.BZ2File(caminho_arquivo_pbz2, mode='r') as fh:
    dados = pickle.load(fh)
dados['pr'] = [valor * 86400 for valor in dados['pr']]

# Criar DataFrame pandas
df_pr = pd.DataFrame({'pr': dados['pr'][:13880], 'data': dates[:13880]})
# Salvar os dados em um arquivo CSV
df_pr.to_csv(caminho_saida_csv, index=False)
print(f'Dados da variável "pr" (até o 13880º valor) salvos em {caminho_saida_csv}')

# Calcular a média mensal de precipitação
df_pr['mes'] = df_pr['data'].dt.to_period('M')
df_mensal = df_pr.groupby('mes').sum().reset_index()
print(len(df_mensal))

# # Salvar os dados mensais em um arquivo CSV
caminho_saida_csv_mensal = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/prec_values_monthly_grouped.csv'
# df_mensal.to_csv(caminho_saida_csv_mensal, index=False)
# print(f'Dados mensais de precipitação salvos em {caminho_saida_csv_mensal}')

# Carregar os dados mensais do arquivo CSV
df_mensal = pd.read_csv(caminho_saida_csv_mensal)

# Converter a coluna 'mes' para o formato adequado
df_mensal['mes'] = pd.to_datetime(df_mensal['mes']).dt.to_period('M')

# Obter valores numéricos para o eixo x (número de meses a partir de uma data de referência)
df_mensal['mes_numerico'] = df_mensal['mes'].dt.year * 12 + df_mensal['mes'].dt.month

# Extrair os anos da coluna 'mes' e criar uma nova coluna 'ano'
df_mensal['ano'] = df_mensal['mes'].dt.year

# Plotar os dados mensais
plt.figure(figsize=(10, 6))
plt.plot(df_mensal['mes'], df_mensal['pr'],  linestyle='-', color='b')
plt.title('Média Mensal de Precipitação')
plt.xlabel('Meses desde o início')
plt.ylabel('Precipitação (mm)')
plt.grid(True)


# Salvar o gráfico em um arquivo PNG
plt.savefig('/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/prec_monthly_regclim.png')
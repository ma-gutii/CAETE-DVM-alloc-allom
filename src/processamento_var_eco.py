import pandas as pd
import joblib
import os # Importado para verificar se o arquivo existe

# --- Configurações Iniciais ---
# Caminho para os outputs
path = f"/home/amazonfaceme/marcelagutierrez/novas_rodadas/CAETE-DVM-alloc-allom/outputs"
run_name = "spin_normal"
grd = '186-239'
start_year = 1979
end_year = 1989

# Lista de variáveis de interesse
variables = ['photo', 'ar', 'npp', 'lai', 'f5', 'evapm',
             'cleaf', 'cwood', 'croot', 'csap', 'cheart',
             'csto', 'wue', 'ls']

# --- Processamento em Loop ---

# 1. Inicializa uma lista vazia para guardar os DataFrames de cada ano
lista_de_dfs_anuais = []

print("Iniciando o processamento dos arquivos anuais...")

# 2. Cria um loop que vai do ano inicial ao final
for year in range(start_year, end_year + 1):
    
    # Calcula o número do spin-up correspondente ao ano
    # Ex: 1979 -> spin1, 1980 -> spin2, etc.
    numero_spin = year - start_year + 1
    
    # Monta o caminho completo para o arquivo do ano corrente
    file_path = f"{path}/{run_name}/gridcell{grd}/spin{numero_spin}.pkz"
    
    # Verifica se o arquivo realmente existe antes de tentar abri-lo
    if not os.path.exists(file_path):
        print(f"AVISO: Arquivo não encontrado para o ano {year}, pulando: {file_path}")
        continue # Pula para o próximo ano do loop
        
    print(f"Processando o ano {year} (arquivo: spin{numero_spin}.pkz)...")

    # Abrir o arquivo PKZ do ano corrente
    with open(file_path, 'rb') as fh:
        dt = joblib.load(fh)

    # Gerar a sequência de datas APENAS para o ano corrente
    date_index = pd.date_range(start=f"{year}-01-01", end=f"{year}-12-31", freq='D')
    num_days = len(date_index)

    # Inicializa um dicionário para os dados deste ano
    data_dict_anual = {'Date': date_index}

    # Adiciona cada variável ao dicionário
    for var in variables:
        series = dt.get(var, [])
        if len(series) != num_days:
            # Se um erro ocorrer, ele informará exatamente em qual ano e variável
            raise ValueError(f"Erro no arquivo 'spin{numero_spin}.pkz': a variável '{var}' tem {len(series)} valores, mas o esperado para o ano {year} era {num_days}.")
        data_dict_anual[var] = series

    # Cria o DataFrame para este ano e o adiciona à lista
    df_anual = pd.DataFrame(data_dict_anual)
    lista_de_dfs_anuais.append(df_anual)

# --- Finalização ---

# 3. Concatena (junta) todos os DataFrames anuais em um único DataFrame final
print("\nConcatenando todos os anos em um único DataFrame...")
df_final = pd.concat(lista_de_dfs_anuais, ignore_index=True)

# 4. Salva o DataFrame completo em um arquivo CSV
output_path = f"{path}/{run_name}/gridcell{grd}/dados_completos_{start_year}-{end_year}.csv"
df_final.to_csv(output_path, index=False)

print(f"\nProcessamento concluído!")
print(f"Arquivo CSV com {len(df_final)} dias de dados salvo em: {output_path}")
print(df_final.info())
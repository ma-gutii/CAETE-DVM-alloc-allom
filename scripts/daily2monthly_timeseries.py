import pandas as pd

#read csv
df = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/concatenated_series_MAN_30prec_1y.csv")

# Certifique-se de que a coluna 'date' está no formato de data
df['date'] = pd.to_datetime(df['Date'])

# Agrupe os dados por mês e faça a média da coluna 'npp'
monthly_npp_mean = df.groupby(df['date'].dt.to_period("M"))['npp'].mean()

# Crie um novo DataFrame com os resultados
result_df = pd.DataFrame({'Date': monthly_npp_mean.index, 'Monthly_NPP_Mean': monthly_npp_mean.values})

result_df.to_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/MAN_30prec_1y_monthly.csv")
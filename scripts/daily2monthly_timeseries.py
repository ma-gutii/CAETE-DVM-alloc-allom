import pandas as pd

# # Manaus 
#-------------------------------
#        Regular climate
#-------------------------------

# #read csv

#path server
# df_regclim = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/MAN_regularclimate/gridcell186-239/concatenated_series_MAN_regularclimate.csv")

# #path local
# df_regclim = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/concatenated_series_MAN_regularclimate.csv")

# # Certify the column 'date' is in the right format
# df_regclim['date'] = pd.to_datetime(df_regclim['Date'])

# # Define a list of columns to calculate monthly mean
# columns_to_mean = ['npp', 'photo', 'ar', 'evapm', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']

# # Group data by month and calculate the mean for each column
# monthly_means_regclim = df_regclim.groupby(df_regclim['date'].dt.to_period("M"))[columns_to_mean].mean()

# monthly_means_regclim.to_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/monthly_mean_tables/MAN_regularclimate_monthly.csv")


# Manaus - 30% prec reduction

#-------------------------------
#           1y freq
#-------------------------------

# df_1y = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/concatenated_series_MAN_30prec_1y.csv")

# # Certify the column 'date' is in the right format
# df_1y['date'] = pd.to_datetime(df_1y['Date'])

# # Define a list of columns to calculate monthly mean
# columns_to_mean = ['npp', 'photo', 'ar', 'evapm', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']

# # Group data by month and calculate the mean for each column
# monthly_means_1y = df_1y.groupby(df_1y['date'].dt.to_period("M"))[columns_to_mean].mean()

# monthly_means_1y.to_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/monthly_mean_tables/MAN_30prec_1y_monthly.csv")

# #read csv
# df = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/concatenated_series_MAN_30prec_1y.csv")

# # Certifique-se de que a coluna 'date' está no formato de data
# df['date'] = pd.to_datetime(df['Date'])

# # Agrupe os dados por mês e faça a média da coluna 'npp'
# monthly_npp_mean = df.groupby(df['date'].dt.to_period("M"))['npp'].mean()

# # Crie um novo DataFrame com os resultados
# result_df = pd.DataFrame({'Date': monthly_npp_mean.index, 'Monthly_NPP_Mean': monthly_npp_mean.values})

# result_df.to_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/MAN_30prec_1y_monthly.csv")


#-------------------------------
#           3y freq
#-------------------------------

#read csv
# df = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_3y/gridcell186-239/concatenated_series_MAN_30prec_3y.csv")
# df_3y = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/concatenated_series_MAN_30prec_3y.csv")

# # Certify the column 'date' is in the right format
# df_3y['date'] = pd.to_datetime(df_3y['Date'])

# # Define a list of columns to calculate monthly mean
# columns_to_mean = ['npp', 'photo', 'ar', 'evapm', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']

# # Group data by month and calculate the mean for each column
# monthly_means_3y = df_3y.groupby(df_3y['date'].dt.to_period("M"))[columns_to_mean].mean()

# monthly_means_3y.to_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/monthly_mean_tables/MAN_30prec_3y_monthly.csv")

# # Certifique-se de que a coluna 'date' está no formato de data
# df['date'] = pd.to_datetime(df['Date'])

# # Agrupe os dados por mês e faça a média da coluna 'npp'
# monthly_npp_mean = df.groupby(df['date'].dt.to_period("M"))['npp'].mean()

# # Crie um novo DataFrame com os resultados
# result_df = pd.DataFrame({'Date': monthly_npp_mean.index, 'Monthly_NPP_Mean': monthly_npp_mean.values})

# result_df.to_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_3y/gridcell186-239/MAN_30prec_3y_monthly.csv")



#-------------------------------
#           5y freq
#-------------------------------

#read csv
# df_5y = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_5y/gridcell186-239/concatenated_series_MAN_30prec_5y.csv")
# df_5y = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/concatenated_series_MAN_30prec_5y.csv")

# # Certify the column 'date' is in the right format
# df_5y['date'] = pd.to_datetime(df_5y['Date'])

# # Define a list of columns to calculate monthly mean
# columns_to_mean = ['npp', 'photo', 'ar', 'evapm', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']

# # Group data by month and calculate the mean for each column
# monthly_means_5y = df_5y.groupby(df_5y['date'].dt.to_period("M"))[columns_to_mean].mean()

# monthly_means_5y.to_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/monthly_mean_tables/MAN_30prec_5y_monthly.csv")

# # # Certifique-se de que a coluna 'date' está no formato de data
# df_5y['date'] = pd.to_datetime(df_5y['Date'])

# # # Agrupe os dados por mês e faça a média da coluna 'npp'
# monthly_npp_mean_5y = df_5y.groupby(df_5y['date'].dt.to_period("M"))['npp'].mean()

# # # Crie um novo DataFrame com os resultados
# result_df_5y = pd.DataFrame({'Date': monthly_npp_mean_5y.index, 'Monthly_NPP_Mean': monthly_npp_mean_5y.values})

# result_df_5y.to_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_5y/gridcell186-239/MAN_30prec_5y_monthly.csv")

#-------------------------------
#           7y freq
#-------------------------------

#read csv
# df_7y = pd.read_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_7y/gridcell186-239/concatenated_series_MAN_30prec_7y.csv")

df_7y = pd.read_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/concatenated_series_MAN_30prec_7y.csv")

# Certify the column 'date' is in the right format
df_7y['date'] = pd.to_datetime(df_7y['Date'])

# Define a list of columns to calculate monthly mean
columns_to_mean = ['npp', 'photo', 'ar', 'evapm', 'cleaf', 'cwood', 'croot', 'csap', 'cheart', 'csto']

# Group data by month and calculate the mean for each column
monthly_means_7y = df_7y.groupby(df_7y['date'].dt.to_period("M"))[columns_to_mean].mean()

monthly_means_7y.to_csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/monthly_mean_tables/MAN_30prec_7y_monthly.csv")

# # # Certifique-se de que a coluna 'date' está no formato de data
# df_7y['date'] = pd.to_datetime(df_7y['Date'])

# # # Agrupe os dados por mês e faça a média da coluna 'npp'
# monthly_npp_mean_7y = df_7y.groupby(df_7y['date'].dt.to_period("M"))['npp'].mean()

# # # Crie um novo DataFrame com os resultados
# result_df_7y = pd.DataFrame({'Date': monthly_npp_mean_7y.index, 'Monthly_NPP_Mean': monthly_npp_mean_7y.values})

# result_df_7y.to_csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_7y/gridcell186-239/MAN_30prec_7y_monthly.csv")

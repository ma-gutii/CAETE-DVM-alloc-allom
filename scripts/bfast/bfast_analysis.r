library(bfast)
library(zoo)


# ################################
# #-------------------------------
# #           Manaus
# #-------------------------------
# ################################
# 
# #-------------------------------
# #        regular climate
# #-------------------------------
# 
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_regclim <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/MAN_regularclimate/gridcell186-239/MAN_regularclimate_monthly.csv")
df_regclim <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_regularclimate_monthly.csv")
# # Converta a coluna 'Date' para o tipo de data 'yearmon'
df_regclim$Date <- as.yearmon(df_regclim$Date)

# # Crie um objeto de série temporal usando a função ts 
time_series_regclim <- ts(df_regclim$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)

# Executar bfast 
res_bfast_regclim <- bfast(time_series_regclim, h = 0.25, max.iter = 1)

plot(res_bfast_regclim)

res_bfast_regclim

# #-------------------------------
# # testing h values - reg clim
# #-------------------------------
#dir for testing h values:
dir_path = "h_sensitivity/regclim"

h_values = seq(0.05, 0.95, by = 0.05)

# Criar uma lista para armazenar os resultados
result_list <- list()

for (h in h_values) {
  print(h)
  
  # Executar bfast e armazenar o resultado na lista
  res_bfast_regclim <- bfast(time_series_regclim, h = h, max.iter = 1)
  # Criar o nome do arquivo com base no valor de h
  filename <- file.path(dir_path, paste("regclim_h_", 
                                        gsub("\\.", "_", as.character(h)), ".png", sep = ""))
  
  # Iniciar a gravação do arquivo PNG
  png(filename)
  
  # Gerar o plot
  plot(res_bfast_regclim, main = paste("h = ", h))
  
  # Encerrar a gravação do arquivo PNG
  dev.off()
  
  # Adicionar o resultado à lista
  result_list[[as.character(h)]] <- res_bfast_regclim
}
result_list


# 
# 
# res_bfast_regclim <- bfast(time_series_regclim, h = 0.09)
# print(res_bfast_regclim)
# 
# # # # Crie o gráfico
# # png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_regclim.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast_regclim, main = "NPP\n Regular climate", ylab = "NPP", xlab = "Time")
# # dev.off()
# 
# 
# 
# 
# #-------------------------------
# #-------------------------------
# #    30% prec reduction
# #-------------------------------
# #-------------------------------
# 
# #-------------------------------
# #           1y freq
# #-------------------------------
# 
# # Manaus - 30% prec reduction - 1 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_1y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_1y_monthly.csv")
# 
# # # Converta a coluna 'Date' para o tipo de data 'yearmon'
df_1y$Date <- as.yearmon(df_1y$Date)
# 
# # # Crie um objeto de série temporal usando a função ts de uma maneira diferente
time_series_1y <- ts(df_1y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)

# Executar bfast 
res_bfast_1y <- bfast(time_series_1y, h = 0.25, max.iter = 1)

plot(res_bfast_1y)

res_bfast_1y


# #-------------------------------
# # testing h values - 1y
# #-------------------------------
#dir for testing h values:
dir_path = "h_sensitivity/freq_1y"


h_values = seq(0.05, 0.95, by = 0.05)

# Criar uma lista para armazenar os resultados
result_list <- list()

for (h in h_values) {
  print(h)
  
  # Executar bfast e armazenar o resultado na lista
  res_bfast_1y <- bfast(time_series_1y, h = h, max.iter = 1)
  # Criar o nome do arquivo com base no valor de h
  filename <- file.path(dir_path, paste("1yfreq_h_", 
                                        gsub("\\.", "_", as.character(h)), ".png", sep = ""))
  
  # Iniciar a gravação do arquivo PNG
  png(filename)
  
  # Gerar o plot
  plot(res_bfast_1y, main = paste("h = ", h))
  
  # Encerrar a gravação do arquivo PNG
  dev.off()
  
  # Adicionar o resultado à lista
  result_list[[as.character(h)]] <- res_bfast_1y
}
result_list
# 
# 
# res_bfast <- bfast(time_series, h =0.2)
# print(res_bfast)
# 
# # # # Crie o gráfico
# # png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_1y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast, main = "NPP\n-30% prec  1year freq", ylab = "NPP", xlab = "Time")
# # dev.off()
# 
# #-------------------------------
# #           3y freq
# #-------------------------------
# 
# # Manaus - 30% prec reduction - 3 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_3y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_3y/gridcell186-239/MAN_30prec_3y_monthly.csv")
df_3y<-read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_3y_monthly.csv")
# # # Converta a coluna 'Date' para o tipo de data 'yearmon'
df_3y$Date <- as.yearmon(df_3y$Date)

# # # Crie um objeto de série temporal usando a função ts de uma maneira diferente
time_series_3y <- ts(df_3y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)

res_bfast_3y <- bfast(time_series_3y, h = 0.25, max.iter = 1)

plot(res_bfast_3y)

res_bfast_3y

#-------------------------------
# testing h values - 3y
#-------------------------------

#dir for testing h values:
dir_path = "h_sensitivity/freq_3y"


h_values = seq(0.05, 0.95, by = 0.05)

# Criar uma lista para armazenar os resultados
result_list <- list()

for (h in h_values) {
  print(h)
  
  # Executar bfast e armazenar o resultado na lista
  res_bfast_3y <- bfast(time_series_3y, h = h, max.iter = 1)
  # Criar o nome do arquivo com base no valor de h
  filename <- file.path(dir_path, paste("3yfreq_h_", 
                                        gsub("\\.", "_", as.character(h)), ".png", sep = ""))
  
  # Iniciar a gravação do arquivo PNG
  png(filename)
  
  # Gerar o plot
  plot(res_bfast_3y, main = paste("h = ", h))
  
  # Encerrar a gravação do arquivo PNG
  dev.off()
  
  # Adicionar o resultado à lista
  result_list[[as.character(h)]] <- res_bfast_3y
}

# 
# res_bfast_3y <- bfast(time_series)
# print(res_bfast_3y)
# 
# # # # Crie o gráfico
# # png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_3y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# # plot(res_bfast_3y, main = "NPP\n-30% prec  3year freq", ylab = "NPP", xlab = "Time")
# # dev.off()
# 
# #-------------------------------
# #           5y freq
# #-------------------------------
# 
# 
# # Manaus - 30% prec reduction - 3 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# # df_5y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_5y/gridcell186-239/MAN_30prec_5y_monthly.csv")
df_5y<-read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_5y_monthly.csv")

# Converta a coluna 'Date' para o tipo de data 'yearmon'
df_5y$Date <- as.yearmon(df_5y$Date)


# # # Crie um objeto de série temporal usando a função ts de uma maneira diferente
time_series_5y <- ts(df_5y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)

res_bfast_5y <- bfast(time_series_5y, h = 0.25, max.iter = 1)

plot(res_bfast_5y)

res_bfast_5y

#-------------------------------
# testing h values - 5y
#-------------------------------

#dir for testing h values:
dir_path = "h_sensitivity/freq_5y"


h_values = seq(0.05, 0.95, by = 0.05)

# Criar uma lista para armazenar os resultados
result_list <- list()

for (h in h_values) {
  print(h)
  
  # Executar bfast e armazenar o resultado na lista
  res_bfast_5y <- bfast(time_series_5y, h = h, max.iter = 1)
  # Criar o nome do arquivo com base no valor de h
  # filename <- file.path(dir_path, paste("5yfreq_h_", 
  #                                       gsub("\\.", "_", as.character(h)), ".png", sep = ""))
  
  # Iniciar a gravação do arquivo PNG
  # png(filename)
  
  # Gerar o plot
  plot(res_bfast_5y, main = paste("h = ", h))
  
  # Encerrar a gravação do arquivo PNG
  # dev.off()
  
  # Adicionar o resultado à lista
  result_list[[as.character(h)]] <- res_bfast_5y
}

# 
# # #------------------------
# # #       regular bfast
# # #------------------------
# res_bfast_5y <- bfast(time_series)
# print(res_bfast_5y)
# 
# # # # Crie o gráfico
# # png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_5y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# # plot(res_bfast_5y, main = "NPP\n-30% prec  5year freq", ylab = "NPP", xlab = "Time")
# # dev.off()
# 
# #-------------------------------
# #           7y freq
# #-------------------------------
# 
# 
# # Manaus - 30% prec reduction - 7 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# # df_7y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_7y/gridcell186-239/MAN_30prec_7y_monthly.csv")
df_7y<-read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_7y_monthly.csv")
# 
# # # Converta a coluna 'Date' para o tipo de data 'yearmon'
df_7y$Date <- as.yearmon(df_7y$Date)

# # # Crie um objeto de série temporal usando a função ts de uma maneira diferente
time_series_7y <- ts(df_7y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)

res_bfast_7y <- bfast(time_series_7y, h = 0.25, max.iter = 1)

plot(res_bfast_7y)

res_bfast_7y

#-------------------------------
# testing h values - 7y
#-------------------------------

#dir for testing h values:
dir_path = "h_sensitivity/freq_7y"


h_values = seq(0.05, 0.95, by = 0.05)

# Criar uma lista para armazenar os resultados
result_list <- list()

for (h in h_values) {
  print(h)
  
  # Executar bfast e armazenar o resultado na lista
  res_bfast_7y <- bfast(time_series_7y, h = h, max.iter = 1)
  # Criar o nome do arquivo com base no valor de h
  filename <- file.path(dir_path, paste("7yfreq_h_", 
                                        gsub("\\.", "_", as.character(h)), ".png", sep = ""))
  
  # Iniciar a gravação do arquivo PNG
  png(filename)
  
  # Gerar o plot
  plot(res_bfast_7y, main = paste("h = ", h))
  
  # Encerrar a gravação do arquivo PNG
  dev.off()
  
  # Adicionar o resultado à lista
  result_list[[as.character(h)]] <- res_bfast_7y
}

# 
# #------------------------
# #       regular bfast
# #------------------------
# res_bfast_7y <- bfast(time_series)
# print(res_bfast_7y)
# 
# # # # # Crie o gráfico
# # png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_7y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# # plot(res_bfast_7y, main = "NPP\n-30% prec  7year freq", ylab = "NPP", xlab = "Time")
# # dev.off()
# 
# 
# 
# 
# 
# 
# 

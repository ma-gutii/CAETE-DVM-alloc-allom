library(bfast)
library(zoo)

################################
#-------------------------------
#           Manaus
#-------------------------------
################################

#-------------------------------
#        regular climate
#-------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_regclim <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/MAN_regularclimate/gridcell186-239/MAN_regularclimate_monthly.csv")

# # Converta a coluna 'Date' para o tipo de data 'yearmon'
# df_regclim$Date <- as.yearmon(df_regclim$Date)

# # Crie um objeto de série temporal usando a função ts de uma maneira diferente
# time_series_regclim <- ts(df_regclim$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


# res_bfast_regclim <- bfast(time_series_regclim)
# print(res_bfast_regclim)

# # # Crie o gráfico
# png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_regclim.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast_regclim, main = "NPP\n Regular climate", ylab = "NPP", xlab = "Time")
# dev.off()




#-------------------------------
#-------------------------------
#    30% prec reduction
#-------------------------------
#-------------------------------

#-------------------------------
#           1y freq
#-------------------------------

# Manaus - 30% prec reduction - 1 year frequency application
# !!!!! note this is the monthly integrated data frame!!!!!!!
# df_1y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/MAN_30prec_1y_monthly.csv")

# # Converta a coluna 'Date' para o tipo de data 'yearmon'
# df_1y$Date <- as.yearmon(df_1y$Date)

# # Crie um objeto de série temporal usando a função ts de uma maneira diferente
# time_series <- ts(df_1y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


# res_bfast <- bfast(time_series, h = 0.1, max.iter = 10)
# print(res_bfast)

# # # Crie o gráfico
# png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_1y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast, main = "NPP\n-30% prec  1year freq", ylab = "NPP", xlab = "Time")
# dev.off()

#-------------------------------
#           3y freq
#-------------------------------

# # Manaus - 30% prec reduction - 3 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_3y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_3y/gridcell186-239/MAN_30prec_3y_monthly.csv")

# # # Converta a coluna 'Date' para o tipo de data 'yearmon'
# df_3y$Date <- as.yearmon(df_3y$Date)

# # # Crie um objeto de série temporal usando a função ts de uma maneira diferente
# time_series <- ts(df_3y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


# res_bfast_3y <- bfast(time_series, h = 0.1, max.iter = 10)
# print(res_bfast_3y)

# # # Crie o gráfico
# png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_3y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast_3y, main = "NPP\n-30% prec  3year freq", ylab = "NPP", xlab = "Time")
# dev.off()

#-------------------------------
#           5y freq
#-------------------------------


# # Manaus - 30% prec reduction - 3 year frequency application
# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_5y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_5y/gridcell186-239/MAN_30prec_5y_monthly.csv")

# # Converta a coluna 'Date' para o tipo de data 'yearmon'
# df_5y$Date <- as.yearmon(df_5y$Date)

# # Crie um objeto de série temporal usando a função ts de uma maneira diferente
# time_series <- ts(df_5y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


# #------------------------
# #       regular bfast
# #------------------------
# res_bfast_5y <- bfast(time_series)
# print(res_bfast_5y)

# # # Crie o gráfico
# png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_5y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(res_bfast_5y, main = "NPP\n-30% prec  5year freq", ylab = "NPP", xlab = "Time")
# dev.off()

#-------------------------------
#           7y freq
#-------------------------------


# Manaus - 30% prec reduction - 7 year frequency application
# !!!!! note this is the monthly integrated data frame!!!!!!!
df_7y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_7y/gridcell186-239/MAN_30prec_7y_monthly.csv")
# # Converta a coluna 'Date' para o tipo de data 'yearmon'
df_7y$Date <- as.yearmon(df_7y$Date)

# # Crie um objeto de série temporal usando a função ts de uma maneira diferente
time_series <- ts(df_7y$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


#------------------------
#       regular bfast
#------------------------
res_bfast_7y <- bfast(time_series)
print(res_bfast_7y)

# # # Crie o gráfico
png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/res_bfast_30perc_7y.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
plot(res_bfast_7y, main = "NPP\n-30% prec  7year freq", ylab = "NPP", xlab = "Time")
dev.off()






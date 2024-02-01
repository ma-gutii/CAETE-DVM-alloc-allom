library(bfast)
library(zoo)

# Manaus - 30% prec reduction - 1 year frequency application
df_1y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/MAN_30prec_1y_monthly.csv")

# Converta a coluna 'Date' para o tipo de data 'yearmon'
df_1y$Date <- as.yearmon(df_1y$Date)

# Filtra os dados para o período entre 1980 e 1990
# df_subset <- subset(df_1y, Date >= as.yearmon("1980-01") & Date <= as.yearmon("1990-12"))

df_subset = df_1y
# Crie um objeto de série temporal usando a função ts
time_series <- ts(df_subset$Monthly_NPP_Mean, start = c(1979, 1), frequency = 12)


# # Crie o gráfico
# png("serie_temporal.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
# plot(time_series, main = "Série Temporal", ylab = "Valor", xlab = "Ano-Mês")
# dev.off()

res_bfast <- bfast(time_series)

print(res_bfast)

# # Crie o gráfico
png("res_bfast.png", width = 800, height = 600, units = "px", pointsize = 12, res = 96)
plot(res_bfast, main = "NPP\n-30% prec  1year freq", ylab = "NPP", xlab = "Time")
dev.off()

# # Execute o BFAST
# bfast_results <- bfast(ts_data, season="multiplicative", max.iter=2)

# # Visualize os resultados
# plot(bfast_results)

# # Cria a série temporal apenas para o período desejado
# time_series <- ts(df_subset$npp, start = min(df_subset$Date), frequency = 365)

# # Reduzir o tamanho da fonte dos rótulos
# par(cex.lab = 1, cex.axis = 1, cex.main = 1)  # Experimente diferentes valores
# plot(time_series, type = "l", xlab = "Data", ylab = "NPP", main = "Série Temporal de NPP (1980-1990)")

# # Mensagem de status
# cat("Análise iniciada...\n")

# # Roda a análise bfast apenas para o período selecionado
# bfast_result <- tryCatch(
#   bfast(time_series),
#   error = function(e) e
# )

# # Verifica se a análise foi concluída com sucesso
# if (inherits(bfast_result, "error")) {
#   cat("Erro na análise bfast:\n")
#   print(bfast_result)
# } else {
#   cat("Análise concluída com sucesso.\n")
#   # Adicione aqui qualquer código adicional que você queira executar após a análise bem-sucedida
# }

# # # Manaus - 30% prec reduction - 1 year frequency application
# # df_1y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/concatenated_series_MAN_30prec_1y.csv")

# # df_1y$Date <- as.Date(df_1y$Date, format = "%Y-%m-%d")

# # # Cria a série temporal
# # time_series <- ts(df_1y$npp, start = min(df_1y$Date), frequency = 365)

# # ## Reduzir o tamanho da fonte dos rótulos
# # par(cex.lab = 1, cex.axis = 1, cex.main = 1)  # Experimente diferentes valores
# # plot(time_series, type = "l", xlab = "Data", ylab = "NPP", main = "Série Temporal de NPP")

# # # Mensagem de status
# # cat("Análise iniciada...\n")

# # # Roda a análise bfast
# # bfast_result <- tryCatch(
# #   bfast(time_series),
# #   error = function(e) e
# # )

# # # Verifica se a análise foi concluída com sucesso
# # if (inherits(bfast_result, "error")) {
# #   cat("Erro na análise bfast:\n")
# #   print(bfast_result)
# # } else {
# #   cat("Análise concluída com sucesso.\n")
# #   # Adicione aqui qualquer código adicional que você queira executar após a análise bem-sucedida
# # }

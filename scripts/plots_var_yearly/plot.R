library(zoo)
library(anytime)
library(ggplot2)
library(viridis)
library(dplyr)
library(tidyr)
library(scales)

df_1y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/yearly_mean_tables/MAN_30prec_1y_yearly.csv")
df_1y$frequency = "1y"

# df_3y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/yearly_mean_tables/MAN_30prec_3y_yearly.csv")
# df_3y$frequency = "3y"
# 
# df_5y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/yearly_mean_tables/MAN_30prec_5y_yearly.csv")
# df_5y$frequency = "5y"

df_7y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/yearly_mean_tables/MAN_30prec_7y_yearly.csv")
df_7y$frequency = "7y"

df_regclim <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/yearly_mean_tables/MAN_regularclimate_yearly.csv")
df_regclim$frequency = "regclim"

# df_combined <- rbind(df_1y, df_3y, df_5y, df_7y, df_regclim)
df_combined <- rbind(df_1y, df_7y, df_regclim)


# df_combined$date = anydate(df_combined$date)

# Converta a coluna "frequency" para o tipo fator
df_combined$frequency <- as.factor(df_combined$frequency)



## Definição das cores para cada categoria
# cores <- c("1y" = "lightsalmon2",
#            "3y" = "gold1",
#            "5y" = "#9370DB",
#            "7y" = "seagreen4",
#            "regclim" = "steelblue3")

## Definição das cores para cada categoria
cores <- c("1y" = "lightsalmon2",
           "7y" = "seagreen4",
           "regclim" = "steelblue3")

# Lista das variáveis que deseja plotar
variaveis <- c("npp", "ctotal", "evapm", "wue", "ls")

# Plot das séries temporais para cada variável
df_combined %>%
  pivot_longer(cols = all_of(variaveis)) %>%
  ggplot(aes(x = date, y = value, color = frequency)) +
  geom_line() +
  scale_color_manual(values = cores) +  # Aplicando as cores específicas
  labs(title = "",
       x = "",
       y = "") +
  theme_minimal() +
  facet_wrap(~name, nrow = 2, ncol = 3, scales = "free_y", 
             drop = TRUE,   # Remove subplots vazios
             labeller = labeller(name = c("npp" = "NPP",
                                          "ctotal" = "Total carbon",
                                          "evapm" = "Evapotranspiration",
                                          "wue" = "Water use efficiency",
                                          "ls" = "N. of surviving strategies")))

  

#normalizado:
library(ggplot2)
library(tidyr)
library(dplyr)

# Definição das cores para cada categoria
cores <- c("1y" = "firebrick3",
           "7y" = "#9370DB",
           "regclim" = "steelblue1")

# Lista das variáveis que deseja plotar
variaveis <- c("npp", "ctotal", "evapm", "wue", "ls")

# Normalização dos dados para o intervalo de 0 a 1
normalize_0_1 <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

# Aplicar a função de normalização às variáveis desejadas
df_normalized <- df_combined %>%
  mutate(across(variaveis, normalize_0_1))

# Especifique o diretório onde deseja salvar os plots
directory <- "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/plots_var_yearly/"

# Criar e salvar cada plot separadamente
plots <- lapply(unique(df_normalized$name), function(var) {
  plot <- ggplot(data = filter(df_normalized, name == var), aes(x = date, y = value, color = frequency)) +
    geom_line() +
    scale_color_manual(values = cores) +
    labs(title = "",
         x = "Year",
         y = "Normalized value",
         color = "Frequency of disturbance") +
    theme_minimal() +
    theme(legend.position = "bottom")
  
  # Definir o nome do arquivo com o diretório especificado
  file_name <- paste(directory, "normalized_plot_", var, ".png", sep = "")
  
  # Salvar o plot como um arquivo PNG
  ggsave(plot = plot, filename = file_name, width = 8, height = 6, dpi = 300)
  
  return(plot)
  dev.off()
})

# Imprimir os plots
print(plots)

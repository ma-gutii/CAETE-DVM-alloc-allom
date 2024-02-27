library(earlywarnings)
library(ggplot2)
library(dplyr)
library(tidyr)
library(RColorBrewer)
library(zoo)
library(tidyverse)

# Create a data frame with sequences of years and months
date_ym <- expand.grid(y = 1979:2016, m = sprintf("%02d", 1:12))

# Combine the year and month columns into a date column in the "y-m" format
date_ym <- date_ym %>% mutate(date = paste(y, m, sep = "-"))

# Sort the data by the "date" column in ascending order
date_ym_arranged <- date_ym %>% arrange(date)

# Display the sorted data
date = date_ym_arranged$date
# table_regclim = cbind(final_df_regclim, date)



## TESTING SLIDING WINDOW SIZE ##


# Function to perform common operations
process_data <- function(file_path) {
  df <- read.csv(file_path)
  df_npp <- df$Monthly_NPP_Mean
  
  winsize <- seq(15, 35, by = 5)
  
  results_list <- lapply(winsize, function(ws) {
    gws <- generic_ews(df_npp, winsize = ws, detrending = 'loess',
                       logtransform = FALSE, interpolate = FALSE, 
                       AR_n = FALSE, powerspectrum = FALSE)
    gws$ws <- ws
    return(gws)
  })
  
  results_list <- lapply(results_list, function(result) {
    if (result$timeindex[1] != 1) {
      additional_rows <- data.frame(
        timeindex = seq(1, result$timeindex[1] - 1),
        ar1 = rep(NA, result$timeindex[1] - 1),
        ws = rep(result$ws[1], result$timeindex[1] - 1)
      )
      return(bind_rows(additional_rows, result))
    } else {
      return(result)
    }
  })
  
  results_list <- lapply(results_list, function(result) {
    result$new_column <- as.yearmon(paste(result$new_column, "-01", sep = ""))
    return(result)
  })
  
  final_df <- bind_rows(results_list)
  final_df$ws <- as.factor(final_df$ws)
  
  distinct_colors <- brewer.pal(nlevels(final_df$ws), "Set1")
  
  ggplot(final_df, aes(x = timeindex, y = ar1, color = ws)) +
    geom_line() +
    scale_color_manual(values = distinct_colors) +
    labs(title = "AR1 over Timeindex",
         x = "Timeindex",
         y = "AR1") +
    theme_minimal()
}

# Example usage for each file
file_path_1y <- "/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_1y_monthly.csv"
plot_1y <- process_data(file_path_1y)


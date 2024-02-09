library(earlywarnings)
library(ggplot2)
library(dplyr)
library(tidyr)


#----------------------------------------------

#               MANAUS

#----------------------------------------------

#investigating EWS during the whole time series


#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 1 year
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_1y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/
                  MAN_30prec_1y_monthly.csv")

#select the variable of interest
df_1y_npp <- df_1y$Monthly_NPP_Mean

# Aplicar generic early warning signals
df_1y_npp_gws <- generic_ews(df_1y_npp, winsize = 15, detrending = 'loess',
                             logtransform = FALSE, interpolate = FALSE, 
                             AR_n = TRUE, powerspectrum = TRUE)

df_1y_npp_gws$frequency = "1"

# 
write.csv(df_1y_npp_gws, file =
            "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/MAN_30prec_1y_timeseries_ews.csv", row.names = FALSE)

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 3 year
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_3y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_3y_monthly.csv")


#select the variable of interest
df_3y_npp <- df_3y$Monthly_NPP_Mean

# Aplicar generic early warning signals
df_3y_npp_gws <- generic_ews(df_3y_npp, winsize = 15, detrending = 'loess',
                             logtransform = FALSE, interpolate = FALSE, 
                             AR_n = TRUE, powerspectrum = TRUE)

df_3y_npp_gws$frequency = "3"

# 
write.csv(df_1y_npp_gws, file =
            "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/MAN_30prec_3y_timeseries_ews.csv", row.names = FALSE)

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 5 year
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_5y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_5y_monthly.csv")


#select the variable of interest
df_5y_npp <- df_5y$Monthly_NPP_Mean

# Aplicar generic early warning signals
df_5y_npp_gws <- generic_ews(df_5y_npp, winsize = 15, detrending = 'loess',
                             logtransform = FALSE, interpolate = FALSE, 
                             AR_n = TRUE, powerspectrum = TRUE)

df_5y_npp_gws$frequency = "5"

# 
write.csv(df_5y_npp_gws, file =
            "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/MAN_30prec_5y_timeseries_ews.csv", row.names = FALSE)


#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 7 year
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_7y <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_30prec_7y_monthly.csv")


#select the variable of interest
df_7y_npp <- df_7y$Monthly_NPP_Mean

# Aplicar generic early warning signals
df_7y_npp_gws <- generic_ews(df_7y_npp, winsize = 15, detrending = 'loess',
                             logtransform = FALSE, interpolate = FALSE, 
                             AR_n = TRUE, powerspectrum = TRUE)

df_7y_npp_gws$frequency = "7"

# 
write.csv(df_7y_npp_gws, file =
            "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/MAN_30prec_7y_timeseries_ews.csv", row.names = FALSE)


#----------------------------------------------
#   precipitation reduction: regular climate
#   frequency: NA
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
df_regclim <- read.csv("/home/bianca/bianca/CAETE-DVM-alloc-allom/src/MAN_regularclimate_monthly.csv")


#select the variable of interest
df_regclim_npp <- df_regclim$Monthly_NPP_Mean

# Aplicar generic early warning signals
df_regclim_npp_gws <- generic_ews(df_regclim_npp, winsize = 15, detrending = 'loess',
                             logtransform = FALSE, interpolate = FALSE, 
                             AR_n = TRUE, powerspectrum = TRUE)

df_regclim_npp_gws$frequency = "regularclimate"

# 
write.csv(df_regclim_npp_gws, file =
            "/home/bianca/bianca/CAETE-DVM-alloc-allom/scripts/MAN_30prec_regclim_timeseries_ews.csv", row.names = FALSE)





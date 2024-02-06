library(earlywarnings)
library(ggplot2)

#----------------------------------------------

#               MANAUS

#----------------------------------------------

#investigating EWS before the identified break points through the library bfast (script: bfast_analysis.R)

##############################################
#       BREAK POINT FROM 1 YEAR FREQUENCY
#                   1987-08
##############################################

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 1 year
#   1st breakpoint: 1987-08
#   variable: NPP
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_1y <- read.csv("/home/bianca/bianca/backup/Doutorado/tese/doc_resilience_chap/EWS_analysis/MAN_30prec_1y_monthly.csv")
# 
# #selecting before 1st breakpoint:
# df_1y_bp <- df_1y[df_1y$Date < "1987-08",]
# 
# df_1y_bp_npp <- df_1y_bp$Monthly_NPP_Mean
# 
# df_1y_bp_npp_gws <- generic_ews(df_1y_bp_npp, winsize = 10, detrending = 'gaussian', 
#                                 bandwidth = 10, logtransform = FALSE,interpolate = FALSE, 
#                                 AR_n = TRUE, powerspectrum = TRUE)
# 
# 
# # Create or display the plot
# plot(df_1y_bp_npp_gws)
# 
# # Close the PNG device to save the plot
# dev.off()

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 3 years
#   1st breakpoint: 1987-08
#   variable: NPP
#----------------------------------------------

# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_3y <- read.csv("/home/bianca/bianca/backup/Doutorado/tese/doc_resilience_chap/EWS_analysis/MAN_30prec_3y_monthly.csv")
# 
# #selecting before 1st breakpoint:
# df_3y_bp <- df_3y[df_3y$Date < "1987-08",]
# 
# df_3y_bp_npp <- df_3y_bp$Monthly_NPP_Mean
# 
# df_3y_bp_npp_gws <- generic_ews(df_3y_bp_npp, winsize = 10, detrending = 'gaussian',
#                                 bandwidth = 10, logtransform = FALSE,interpolate = FALSE,
#                                 AR_n = TRUE, powerspectrum = TRUE)
# 
# 
# # Create or display the plot
# plot(df_3y_bp_npp_gws)
# 
# # Close the PNG device to save the plot
# dev.off()

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 5 years
#   1st breakpoint: 1987-08
#   variable: NPP
#----------------------------------------------
# !!!!! note this is the monthly integrated data frame!!!!!!!
# df_5y <- read.csv("/home/bianca/bianca/backup/Doutorado/tese/doc_resilience_chap/EWS_analysis/MAN_30prec_5y_monthly.csv")
# 
# #selecting before 1st breakpoint:
# df_5y_bp <- df_5y[df_5y$Date < "1987-08",]
# 
# df_5y_bp_npp <- df_5y_bp$Monthly_NPP_Mean
# 
# df_5y_bp_npp_gws <- generic_ews(df_5y_bp_npp, winsize = 10, detrending = 'gaussian',
#                                 bandwidth = 10, logtransform = FALSE,interpolate = FALSE,
#                                 AR_n = TRUE, powerspectrum = TRUE)
# 
# 
# # Create or display the plot
# plot(df_5y_bp_npp_gws)
# 
# # Close the PNG device to save the plot
# dev.off()

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 7 years
#   1st breakpoint: 1987-08
#   variable: NPP
#----------------------------------------------
# !!!!! note this is the monthly integrated data frame!!!!!!!
df_7y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/MAN_regularclimate/gridcell186-239/MAN_regularclimate_monthly.csv")

#selecting before 1st breakpoint:
df_7y_bp <- df_7y[df_7y$Date < "1987-08",]
# 
df_7y_bp_npp <- df_7y_bp$Monthly_NPP_Mean
# 
df_7y_bp_npp_gws <- generic_ews(df_7y_bp_npp, winsize = 10, detrending = 'gaussian',
                                bandwidth = 10, logtransform = FALSE,interpolate = FALSE,
                                AR_n = TRUE, powerspectrum = FALSE)
# 

# Create or display the plot
plot(df_7y_bp_npp_gws)

# Close the PNG device to save the plot
dev.off()

# ----------------------------------------------
#   precipitation reduction: regular climate
#   frequency: regular climate
#   1st breakpoint: 1987-08
#   variable: NPP
# ----------------------------------------------
# !!!!! note this is the monthly integrated data frame!!!!!!!
# df_regularclimate <- read.csv("/home/bianca/bianca/backup/Doutorado/tese/doc_resilience_chap/EWS_analysis/MAN_regularclimate_monthly.csv")

# #selecting before 1st breakpoint:
# df_regularclimate_bp <- df_regularclimate[df_regularclimate$Date < "1987-08",]

# df_regularclimate_bp_npp <- df_regularclimate_bp$Monthly_NPP_Mean

# df_regularclimate_bp_npp_gws <- generic_ews(df_regularclimate_bp_npp, winsize = 10, detrending = 'gaussian',
#                                 bandwidth = 10, logtransform = FALSE,interpolate = FALSE,
#                                 AR_n = TRUE, powerspectrum = TRUE)


# # Create or display the plot
# plot(df_regularclimate_bp_npp_gws)

# # Close the PNG device to save the plot
# dev.off()

##############################################
#       BREAK POINT FROM 3 YEAR FREQUENCY
#                  1991-11
##############################################

# ----------------------------------------------
#   precipitation reduction: regular climate
#   frequency: regular climate
#   1st breakpoint: 1991-11
#   variable: NPP
# ----------------------------------------------


# # !!!!! note this is the monthly integrated data frame!!!!!!!
# df_regularclimate <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/MAN_regularclimate/gridcell186-239/MAN_regularclimate_monthly.csv")

# # #selecting before 1st breakpoint:
# df_regularclimate_bp <- df_regularclimate[df_regularclimate$Date < "1991-11",]

# df_regularclimate_bp_npp <- df_regularclimate_bp$Monthly_NPP_Mean

# df_regularclimate_bp_npp_gws <- generic_ews(df_regularclimate_bp_npp, winsize = 10, detrending = 'gaussian',
#                                 bandwidth = 10, logtransform = FALSE,interpolate = FALSE,
#                                 AR_n = TRUE, powerspectrum = FALSE)

# df_regularclimate_bp_npp_gws$ar1

# plot(df_regularclimate_bp_npp_gws)
# first_plot = recordPlot()
# # # Create or display the plot
# png("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/ews_30perc_before_3ybp_regclim.png")
# replayPlot(first_plot)
# dev.off()

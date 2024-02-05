library(earlywarnings)
library(ggplot2)

#----------------------------------------------

#               MANAUS

#----------------------------------------------

#investigating EWS before the identified break points through the library bfast (script: bfast_analysis.R)

#----------------------------------------------
#   precipitation reduction: 30%
#   frequency: 1 year
#   1st breakpoint: 1987-08
#   variable: NPP
#----------------------------------------------

# !!!!! note this is the monthly integrated data frame!!!!!!!
df_1y <- read.csv("/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/outputs/MAN/experiments/30perc_reduction/MAN_30prec_1y/gridcell186-239/MAN_30prec_1y_monthly.csv")

#selecting before 1st breakpoint:
df_1y_bp <- df_1y[df_1y$Date < "1987-08",]

df_1y_bp_npp <- df_1y_bp$Monthly_NPP_Mean

df_1y_bp_npp_gws <- generic_ews(df_1y_bp_npp, winsize = 10)
# Open the PNG device for plotting
png("plot.png", width = 8, height = 6, units = "in", res = 300)

# Create or display the plot
plot(df_1y_bp_npp_gws)

# Close the PNG device to save the plot
dev.off()

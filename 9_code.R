library(tidyverse)
library(tidyquant)

options("getSymbols.warning4.0"=FALSE)
options("getSymbols.yahoo.warning"=FALSE)

candleStick_plot = function(symbol,from,to){
  tq_get(symbol,
         from = from,
         to = to,
         warnings = FALSE) %>% 
    mutate(greenRed=ifelse(open-close>0,
                           "Red",
                           "Green")) %>% 
    ggplot()+
    geom_segment(aes(x = date,
                     xend=date,
                     y =open,
                     yend =close,
                     colour=greenRed),
                 size=3)+
    theme_tq()+
    geom_segment(aes(x = date,
                     xend=date,
                     y =high,
                     yend =low,
                     colour=greenRed))+
    scale_color_manual(values=c("Forest Green","Red"))+
    ggtitle(paste0(symbol,' ', 'Price [$]'))+
    theme(legend.position ="none",
          axis.title.y = element_blank(),
          axis.title.x=element_blank(),
          axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
          plot.title= element_text(hjust=0.5))
}

# Opening visualization device:
quartz()

# Plotting data:
candleStick_plot("AMZN",from = '2023-10-14',to = lubridate::today())

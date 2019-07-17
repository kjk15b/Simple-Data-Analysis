#!/bin/env R


in_data <- read.table("labled_data.txt", header=TRUE, sep="\t")


boxplot(in_data[1:13], main="NUDT5 Expression Among Estrogen Receptor Status", notch=FALSE, col=1:13, las=2, par(mar = c(9,5,1,2) + 0.1), names=c("Curtis Positive", "VandeVijver Positive", "Gluck Positive", "Chin Positive", "TCGA Positive", "Curtis Negative", "VandeVijver Negative", "Gluck Negative", "Chin Negative", "TCGA Negative", "Curtis Normal", "Gluck Normal", "TCGA Normal"), ylab="NUDT5 Expression")

quartz()


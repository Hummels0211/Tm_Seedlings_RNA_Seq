# import necessary packages
import csv
import os

# Change the file directory to read and write the data
os.chdir("C://Users/giaccoyu/Documents/GitHub/Tm_Seedlings_RNA_Seq/RNA_Seq_Seedlings")

# Load the original csv data of RNA copies
df = open('RNAseq20180228Arabidopsis.csv')
data = csv.reader(df)

# Create a new file to store all the relative RNA expression of the transcriptome
with open('rna_expression.csv', 'w+') as rnaprofile:
    writer = csv.write(rnaprofile)
    writer.writecolumn([''])

# Create a new columns for storing the calculations in the same csv file
df.write()


#####################
# Plotting the data #
#####################

import os
dir="C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/mapped/bam/sorted/readgrouped/heteroSNPs/"
output=open("heteroSNP.csv",'w')
for file in os.listdir(dir):
    input=open(dir+file)
    sample=[0]*18
    for line in input:
        sample[int(line.split()[0][-2:].strip("_"))-1]+=1
    output.write(file)
    for value in sample:
        output.write(","+str(value))
    output.write("\n")
output.close()
import os
dir="C:/Users/asim/Documents/TransferFiles/Dothistroma/2015-2016/coverage/loci_coverage_per_base/"
genes={}
threshold=5
gene=""
coveragecount=0
length=0
for file in os.listdir(dir):
    if file[1]=="_": index=int(file[0])
    else: index=int(file[0:2])
    input=open(dir+file)
    for line in input:
        line=line.split()
        if int(line[4])==1:
            if gene!="":
                if coveragecount/length<.5:
                    if line[3] not in genes:
                        genes[line[3]]=["present"]*18
                    genes[line[3]][index-1]="absent"
            gene=line[3]
            length=0
            coveragecount=0
        length+=1
        if int(line[5])>=threshold:
            coveragecount+=1
    if coveragecount/length<.5:
        if line[3] not in genes:
            genes[line[3]]=["present"]*18
        genes[line[3]][index-1]="absent"

            

output=open("presence_absence_5xthreshold.csv",'w')
for gene in genes:
    output.write(gene)
    for value in genes[gene]:
        output.write(",") 
        output.write(value)
    output.write("\n")

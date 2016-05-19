import os
import math
dir="C:/Users/Andre/Desktop/Linux/Dothi/loci_cov/"
genes={}
for file in os.listdir(dir):
    lines=[]
    sum=0.0
    count=0
    if file[1]=="_": index=int(file[0])
    else: index=int(file[0:2])
    input=open(dir+file)
    for line in input:
        line=line.split()
        lines.append(line)
        if float(line[7])<.5:
            if line[3] not in genes:
                genes[line[3]]=["present"]*18
            genes[line[3]][index-1]="absent"
        else:
            if float(line[4])/float(line[6])<3:
                sum+=float(line[4])/float(line[6])
                count+=1
    mean=sum/count
    sum=0.0
    for line in lines:
        if float(line[7])>=.5 and float(line[4])/float(line[6])<3:
            sum+=(float(line[4])/float(line[6])-mean)*(float(line[4])/float(line[6])-mean)
    stddev=math.sqrt(sum/count)
    print mean, stddev
    for line in lines:
        if float(line[4])/float(line[6])>=(mean+(3*stddev)):
            if line[3] not in genes:
                genes[line[3]]=["present"]*18
            if genes[line[3]][index-1]!="present":
                print(genes[line[3]][index-1])
            genes[line[3]][index-1]="duplicated"

output=open("presence_absence_abundance.csv",'w')
for gene in genes:
    output.write(gene)
    for value in genes[gene]:
        output.write(",") 
        output.write(value)
    output.write("\n")

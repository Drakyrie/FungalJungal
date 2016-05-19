import os
dir="C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/coverage/loci_coverage/"
genes={}
for file in os.listdir(dir):
    if file[1]=="_": index=int(file[0])
    else: index=int(file[0:2])
    input=open(dir+file)
    for line in input:
        print line
        line=line.split()
        if float(line[7])<.5:
            if line[3] not in genes:
                genes[line[3]]=["present"]*18
            genes[line[3]][index-1]="absent"

output=open("presence_absence.csv",'w')
for gene in genes:
    output.write(gene)
    for value in genes[gene]:
        output.write(",") 
        output.write(value)
    output.write("\n")

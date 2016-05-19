import os
dir="C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/PAV/"
genes={}
for file in os.listdir(dir):
    if "dupcov" in file:
        if file[1]=="_": index=int(file[0])-1
        else: index=int(file[0:2])-1
        file=open(dir+file)
        for line in file:
            if float(line.split()[12])>0.5:
                id=line.split()[8].split("proteinId=")[1].split(";")[0]
                if id not in genes:
                    genes[id]=["1"]*18
                genes[id][index]="0"
output=open("CNV_dup.csv",'w')
for gene in genes:
    output.write(gene)
    for x in genes[gene]:
        output.write(","+x)
    output.write('\n')
output.close()
                        
                
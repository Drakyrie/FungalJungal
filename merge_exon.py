import os
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/exon_SNP_coverage/"
for file in os.listdir(dir):
    genes={}
    print genes
    input=open(dir+file)
    output=open(dir+file+".combined",'w')
    for line in input:
        line=line.split()
        if line[3] not in genes:
            genes[line[3]]=[line[0],line[1],line[3],int(line[5].strip(';')),int(line[6].strip(';'))]
        else:
            genes[line[3]][3]+=int(line[5])
            genes[line[3]][4]+=int(line[6])        
            
    for gene in genes:
        output.write(genes[gene][0]+','+genes[gene][1]+','+genes[gene][2]+','+str(genes[gene][3])+','+str(genes[gene][4])+','+str(float(genes[gene][3])/float(genes[gene][4]))+'\n')
    output.close()
    input.close()
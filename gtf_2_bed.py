gtf=open("C:/Users/Andre/Desktop/Linux/Dothi/Dotse1_GeneCatalog_genes_20100818.gff")
#gtf=open("toy.txt")
genes={}
output=open("dothi_exon.bed",'w')
for line in gtf:
    line=line.split()
    name = line[9].strip(";").strip('"')
    #if name not in genes:
    genes[name]=[line[0], 99999999, 0]
    if int(line[3])<genes[name][1]:
        genes[name][1]=int(line[3])
    if int(line[4])>genes[name][2]:
        genes[name][2]=int(line[4])
    if "CDS" in line[2] and len(genes[name])<4:
        output.write(line[0]+"\t")
        if int(line[3])<int(line[4]):
            output.write(line[3]+"\t"+line[4]+"\t")
        else:
            output.write(line[4]+"\t"+line[3]+"\t")
        genes[name].append(line[11])
        output.write(line[11]+"\n")
#for gene in genes:
#   output.write(genes[gene][0]+"\t"+str(genes[gene][1])+"\t"+str(genes[gene][2])+"\t"+genes[gene][3]+"\n")
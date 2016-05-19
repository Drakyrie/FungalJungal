file =open("C:/Users/Andre/Desktop/Dothi_novel_genes.gtf.csv")
geneStart={}
geneEnd={}
geneOrientation={}
geneScaffold={}
genes=[]
for line in file:
    gene=("XLOC_"+line.split("XLOC_")[1][0:6])
    if gene in genes:
        if int(line.split(",")[3]) < int(geneStart[gene]):
            geneStart[gene]=line.split(",")[3]
        if int(line.split(",")[4]) > int(geneEnd[gene]):
            geneEnd[gene]=line.split(",")[4]
    else:
        genes.append(gene)
        geneStart[gene]=line.split(",")[3]
        geneEnd[gene]=line.split(",")[4]
        geneOrientation[gene]=line.split(",")[6]
        geneScaffold[gene]=line.split(",")[0]
        
for gene in genes:
    print gene+','+geneScaffold[gene]+','+geneStart[gene]+','+geneEnd[gene]+','+geneOrientation[gene]
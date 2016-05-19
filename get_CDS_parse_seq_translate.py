'''
Created on 19/01/2016

@author: Andre
'''
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet.IUPAC import IUPACUnambiguousDNA
bedfile=open("C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/target_gene_sequences.bed.csv")
geneCoord={}
geneExons={}
for line in bedfile:
    line=line.split(',')
    geneCoord[line[3]]=[line[1],line[2]]
gff=open("C:/Users/Andre/Desktop/Work files/Linux/Dotse1_all_genes_20100818.gff")
for line in gff:
    line=line.split()
    if "CDS" in line[2]:
        #id=line[8].split(";")
        id=line[11].strip(";")
        #id=id[2].split(" ")[1]
        if id not in geneExons:
            geneExons[id]=[line[6]]
        geneExons[id].append([int(line[3]),int(line[4])])
genesequences=open("C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/target_gene_sequences.csv")
output=open("target_sequence_translated.csv",'w')
for line in genesequences:
    line=line.split(',')
    #id=line[0][2:]
    output.write(line[0])
    for i in range(8,26):
        sequence=line[i]
        nsequence=""
        if geneExons[line[0]][0]=="+":
            nsequence="A"
            for exon in geneExons[line[0]]:
                if line[0]=="73814":
                    print exon
                if len(exon)>1:
                    nsequence+=sequence[exon[0]-int(line[3]):(exon[0]-int(line[3]))+exon[1]-exon[0]]
            output.write(",")
            output.write(str(Seq(nsequence,IUPACUnambiguousDNA()).translate()))
        '''else:
            for exon in geneExons[line[0]]:
                if len(exon)>1:
                    nsequence+=sequence[exon[0]-int(line[3]):(exon[0]-int(line[3]))+exon[1]-exon[0]]
            output.write(",")
            output.write(str(Seq(nsequence,IUPACUnambiguousDNA()).reverse_complement().translate()))'''
    output.write("\n")
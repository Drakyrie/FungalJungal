from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_input = "novel_genes.faa"
sequences=[]
count=1
for seq in SeqIO.parse(open(fasta_input),"fasta"):
    cys=0
    for letter in seq.seq:
        if letter == "C":
            cys+=1
    print seq.name, len(seq.seq), cys, seq.seq

#SeqIO.write(sequences,str(count)+"_input.faa","fasta")
           

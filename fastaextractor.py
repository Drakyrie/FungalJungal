from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_input = "Dotse1_GeneCatalog_proteins_20100818.aa.fasta"
sequences=[79359,71155,71156,71157,71158,71159,71160,71161,71162,71163,71166,170687,87718,33868,61885,71168,71169,71170,71172,128803,150350,87725,79371,71176,23391,33877,150357,33879,71178,71179]
count=1
for seq in SeqIO.parse(open(fasta_input),"fasta"):
    for id in sequences:
        if id in seq.name:
            print id
            print seq.seq
    """if len(seq.seq)>6000:continue
    sequences.append(seq)
    if len(sequences) == 2000:
        SeqIO.write(sequences,str(count)+"_input.faa","fasta")
        sequences=[]
        count+=1
SeqIO.write(sequences,str(count)+"_input.faa","fasta")
print count"""
           



        

import os
from Bio import SeqIO
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/CDS_sequences/"
atg=0
leng=0
for file in os.listdir(dir):
    if ".fasta" in file:
        length=""
        flag=False
        for seq_record in SeqIO.parse(dir+file, "fasta"):
            if file=="118184.txt.fasta":
                print seq_record.seq.translate()
            if length=="": length=len(seq_record.seq)
            if length!=len(seq_record.seq):
                flag=True
            if "*" in seq_record.seq.translate()[:-1]:
                flag=True
        if seq_record.seq[0:3]!="ATG" or flag == True:
            os.rename(dir+file,dir+"invalid/"+file)
            
                
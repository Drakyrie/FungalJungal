from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_input = "C:/Users/Andre/Desktop/Work files/Dothistroma/Genome data/Dotse1_AssemblyScaffolds_Repeatmasked.fasta"
for seq in SeqIO.parse(open(fasta_input),"fasta"):
    print seq.name, len(seq.seq)

#SeqIO.write(sequences,str(count)+"_input.faa","fasta")
           

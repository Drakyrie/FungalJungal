contigsfile=open("contigs_file.fasta")
contigs=[]
for line in contigsfile:
    if ">" in line:
        contigs.append(line[1:].strip())
contigsfile.close()
alignedcontigs=[]
coordsfile=open("nucmer.coords")
for line in contigsfile:
    line=line.split('|')
    if len(line)==7:
        alignedcontigs.append(line[6].split(" ")[1].strip())
for contig in alignedcontigs:
    if contig in contigs:
        contigs.remove(contig)
output=open("unaligned_contigs.fasta",'w')
for contig in contigs:
    output.write(contig)
    output.write('\n')
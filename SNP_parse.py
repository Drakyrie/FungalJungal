genomefile=open("C:/Users/Andre/Desktop/Work files/Dothistroma/Genome data/Dotse1_AssemblyScaffolds_Repeatmasked.fasta")
genome={}
id="scaffold_1"
sequence=""
for line in genomefile:
    if ">" in line:
        genome[id]=sequence
        id=line.strip()[1:]
        sequence=""
    else:
        sequence+=line.strip()
genome[id]=sequence

snpfile=open("file")

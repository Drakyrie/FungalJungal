from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

input = open("//tur-storage1/BradshawLab/18Genomes/Presence_Absence/cnvnator_duplication_coverage.csv")
first=True
output=open("DuplicatedGenes.csv",'w')
for line in input:
    if first:
        output.write(line)
        first=False
        continue
    string=""
    deletion=False
    line=line.split(",")
    string+=line[0].split("proteinId=")[1].split(";transcript")[0]
    for value in line[1:]:
        string+=","+value
        if float(value)>=.9:
            deletion=True
    if deletion:
        output.write(string)
    
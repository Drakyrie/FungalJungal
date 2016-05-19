file=open("RPMKwithGOIDS.txt")

#change goterms and terms.append as needed
filename="secondary metabolic process"
goterms=open(filename+".txt")
terms=[]
terms.append("GO:0019748")  #add in parent go term
goterms.readline()
for line in goterms:
    terms.append(line.strip().split("\t")[-1].strip('"'))

termdict={}
goterms=open("goterms.txt")
for line in goterms:
    line=line.split("\t")
    if len(line)==2:
        termdict[line[0].strip('"')]=":"+line[1].strip().strip('"')+";"

compareterms=[]
for term in terms:
    compareterms.append(termdict[term])
    
genes=[]
file.readline()
for line in file:
    if len(genes)>99:break
    line=line.split("\t")
    for term in compareterms:
        if term in line[5]:
            genes.append(line)
            break
        
print len(genes)

file=open(filename+".csv", 'w')
for gene in genes:
    file.write(gene[0])
    file.write(",")
    file.write(gene[2])
    file.write(",")
    file.write(gene[3])
    file.write(",")
    file.write(gene[4])
    file.write("\n")
    


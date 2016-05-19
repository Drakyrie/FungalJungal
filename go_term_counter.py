file=open("DEGseq_E-M_cutoff_noless2FC.txt")
file2=open("DEGseq_M-L_cutoff_noless2FC.txt")
#file3=open("DEGseq_L-FM_cutoff_noless2FC.txt")

#change goterms and terms.append as needed
goterms=open("oxidation-reduction process.txt")
terms=[]
terms.append("GO:0055114")  #add in parent go term
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
    
up=0
down=0
file.readline()
for line in file:
    line=line.split("\t")
    for term in compareterms:
        if term in line[2]:
            if float(line[1])<1:up+=1
            if float(line[1])>1:down+=1
            break
        
print up
print down

up2=0
down2=0
file2.readline()
for line in file2:
    line=line.split("\t")
    for term in compareterms:
        if term in line[2]:
            if float(line[1])<1:up2+=1
            if float(line[1])>1:down2+=1
            break
        
print up2
print down2

#up3=0
#down3=0
#file3.readline()
#for line in file3:
#    line=line.split("\t")
#    for term in compareterms:
#        if term in line[2]:
#            if float(line[1])<1:up3+=1
#            if float(line[1])>1:down3+=1
#            continue
        
#print up3
#print down3


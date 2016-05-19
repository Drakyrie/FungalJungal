import os
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/SNP_coverage/"
genome=[]
for i in range(20):
    genome.append([])
for scaffold in genome:
    for i in range(18):
        scaffold.append("")
print genome
for file in os.listdir(dir):
    input=open(dir+file)
    if file[1]=="_": index=int(file[0])-1
    else: index=int(file[0:2])-1
    for line in input:
        line=line.split()
        if genome[int(line[0].split('_')[1])-1][index]=="": 
            genome[int(line[0].split('_')[1])-1][index]=[]
        #    if index==9: print genome
        genome[int(line[0].split('_')[1])-1][index].append(line[7])
    input.close()

count=1
for scaffold in genome:
    output=open('SNPs_'+str(count)+'.csv','w')
    count+=1
    for i in range(len(scaffold[0])):
        flag=True
        for sample in scaffold:
            if flag != True:
                output.write(',')
            output.write(sample[i])
            flag=False
        output.write('\n')
    output.close()
        
    
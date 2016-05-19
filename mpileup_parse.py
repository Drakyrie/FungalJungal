import os
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/target_gene_sequences/"
for file in os.listdir(dir):
    genes=[""]*18
    for seqfile in os.listdir(dir+file):
        input=open(dir+file+"/"+seqfile)
        last=0
        if "trimmed" not in seqfile:
            continue
        if seqfile[1]=="_": index=int(seqfile[0])-1
        else: index=int(seqfile[0:2])-1
        for line in input:
            line=line.split()
            if int(line[1])!=last+1 and genes[index]!="":
                genes[index]+="N"*((int(line[1])-last)-1)
            last=int(line[1])
            A=0
            T=0
            G=0
            C=0
            ref=0   
            if int(line[3])<10: #coverage threshold
                genes[index]+="N"
                continue
            count=0
            flag=False
            startflag=False
            insertflag=False
            insert=""
            for i in line[4]:
                inserts=[]
                if flag==True:
                    flag=False
                    count=int(i)
                    continue
                if startflag:
                    startflag=False
                    continue
                if count > 0:
                    count-=1
                    if insertflag:
                        insert+=i
                    if count==0:
                        insertflag=False
                        inserts.append(insert)
                    continue
                if i.lower()=='+' or i.lower()=='-':
                    flag=True
                    if i.lower()=='+':
                        insertflag=True
                        insert=""
                    continue
                if i.lower()=='^':
                    startflag=True 
                if i.lower()=='.' or i.lower()==',': ref+=1
                if i.lower()=='a':A+=1
                elif i.lower()=='t':T+=1 
                elif i.lower()=='g':G+=1 
                elif i.lower()=='c':C+=1
            for insert in inserts:
                if inserts.count(insert)>(int(line[3])/2.5):
                    genes[index]+=insert
                    continue
            max=""  
            maxcount=0   
            if A>=T:
                max='A'
                maxcount=A
            else:
                max='T'
                maxcount=T
            if G>=maxcount:
                max='G'
                maxcount=G
            if C>=maxcount:
                max='C'
                maxcount=C
            if ref>=maxcount:
                max=line[2]
                maxcount=ref
            if maxcount < 10: #there are more deletions or insertions
                max='N'
            genes[index]+=max
    output=open(dir+file+".fa",'w')
    count=1
    for gene in genes:
        output.write(">sample_"+str(count)+'\n')
        count+=1
        #output.write(str(gene))
        #for sequence in genes[gene]:
        output.write("".join(gene)+'\n')
    #output.write('\n')
    output.close()
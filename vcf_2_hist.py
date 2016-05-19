import os
dir="//tur-storage1/BradshawLab/18Genomes/SNPs/SNPs/"
for file in os.listdir(dir):
    if ".vcf" in file:
        output=open(file+".hist",'w')
        input=open(dir+file)
        scaffold=1
        count=0
        box=0
        for line in input:
            if line[0]=="#": continue
            line=line.split()
            if int(line[1])>=box*10000 and int(line[1])<(box+1)*10000:
                count+=1
            if line[0]!="scaffold_"+str(scaffold):
                output.write("scaffold_"+str(scaffold)+"\t"+str(box*10000)+"\t"+str((box+1)*10000)+"\t"+str(count)+"\n")
                scaffold+=1
                box=0
                count=0
            if int(line[1])>=(box+1)*10000:
                output.write("scaffold_"+str(scaffold)+"\t"+str(box*10000)+"\t"+str((box+1)*10000)+"\t"+str(count)+"\n")
                box+=1
        output.write("scaffold_"+str(scaffold)+"\t"+str(box*10000)+"\t"+str((box+1)*10000)+"\t"+str(count)+"\n")        
        output.close()
            
            
            
            
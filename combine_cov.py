import os
dir="//tur-storage1/BradshawLab/18Genomes/Coverage/scaffold_coverage/"
for file in os.listdir(dir):
    if ".hist" in file:
        filename=file
        scaffolds=[]
        for i in range(25):
            scaffolds.append([""])
        file=open(dir+file)
        for line in file:
            if line.split()[0] == "genome":
                scaffolds[0].append(line.split()[4])
            else:
                scaffolds[int(line.split()[0].split('_')[1])].append(line.split()[4])
        output=open(filename+".csv",'w')
        output.write("coverage,genome")
        for i in range(1,15):
            output.write(',')
            output.write("scaffold_"+str(i))
        output.write('\n')
        for i in range (1,200):
            output.write(str(i))
            for x in range(15):
                output.write(',')
                if len(scaffolds[x])<i+1:
                    output.write("0")
                else: 
                    output.write(scaffolds[x][i])
            output.write('\n')
        output.close()
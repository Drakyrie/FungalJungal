import os
dir="C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/mapped/bam/sorted/cnvnator/"
for file in os.listdir(dir):
    if "50bp.txt" in file:
        output=open(file+".csv",'w')
        input=open(dir+file)
        lastend=-1
        for line in input:
            if "scaffold_4" in line:
                if lastend+1!=int(line.split()[1].split(':')[1].split('-')[0]):
                    output.write(str(lastend+1)+",1\n")
                lastend=int(line.split()[1].split(':')[1].split('-')[1])
                output.write(line.split()[1].split(':')[1].split('-')[0])#start
                output.write(',')
                if "duplication" in line:
                    output.write("2")
                elif "deletion" in line:
                    output.write("0")
                output.write('\n')
        output.close()
        input.close()
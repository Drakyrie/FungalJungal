import os
dir="C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/mapped/bam/sorted/cnvnator/"
output=open("CNVnator.bed",'w')
count=1
for file in os.listdir(dir):
    if "50bp.txt" in file:
        input=open(dir+file)
        for line in input:
            if True:
            #if "duplication" in line:
                output.write(line.split()[1].split(':')[0]) #scaffold
                output.write(',')
                output.write(line.split()[1].split(':')[1].split('-')[0])#start
                output.write(',')
                output.write(line.split()[1].split(':')[1].split('-')[1])#end
                output.write(',')
                output.write(file.split("_")[1])
                output.write(',1,')# score
                if "duplication" in line.split()[0]:
                    output.write('1')
                else: output.write('-1')
                output.write(',')
                output.write(str(count))
                output.write('\n')
        count+=1
output.close()
input.close()
input=open("C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/mapped/bam/sorted/readgrouped/heteroSNPs/14_NZE8_C80GLANXX_AGTTCCGT_L001_.at.r1.trimmed.paired.fq.sorted.bam.diploid.vcf.filter.vcf")
snps=[]
for line in input:
    linesplit=line.split()
    if len(linesplit[3])==1 and len(linesplit[4])==1:
        snps.append(linesplit[0]+":"+linesplit[1])
input.close()
print len(snps)
import os
dir="C:/Users/asim/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/mapped/bam/sorted/readgrouped/"
output=open("heteroSNP.csv",'w')
for file in os.listdir(dir):
    if "Q20.vcf.stripped" in file:
        input=open(dir+file)
        if linesplit[0]+":"+linesplit[1] in snps:
            print linesplit[0]+":"+linesplit[1] + "\t" + file
    
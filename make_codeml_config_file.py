import os
from Bio import SeqIO
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/CDS_sequences/"
for file in os.listdir(dir):
    output=open(dir+"control/"+file+".ctl",'w')
    output.write("seqfile = /media/shared/AGRF_CAGRF11237_C80GLANXX/CDS_sequences/"+file+"\n")
    output.write("outfile = /media/shared/AGRF_CAGRF11237_C80GLANXX/CDS_sequences/results/"+file+"\n")
    output.write("treefile = treefile.txt *tree file\nnoisy = 0      * 0,1,2,3,9: how much rubbish on the screen\nverbose = 0      * 1:detailed output\nrunmode = -2     * -2:pairwise\nseqtype = 1      * 1:codons\nCodonFreq = 0      * 0:equal, 1:F1X4, 2:F3X4, 3:F61\nmodel = 0      *\nNSsites = 0      *\nicode = 0      * 0:universal code\nfix_kappa = 1      * 1:kappa fixed, 0:kappa to be estimated\nkappa = 1      * initial or fixed kappa\nfix_omega = 0      * 1:omega fixed, 0:omega to be estimated\nomega = 0.5    * initial omega value")
    output.close()
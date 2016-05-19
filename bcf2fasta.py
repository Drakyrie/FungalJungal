from Bio.Seq import Seq
import os
sequences=[""]*18
#for i in range(1,19):
for file in os.listdir("./"):
    if ".bcf" in file:
        input=open(file)
    #input=open(str(i)+".bcf")
        sequence=""
        print ">"+file
        for line in input:
            line=line.split()
            if "#" not in line[0]:
                if "." in line[4]:
                    sequence+=line[3]
                else: sequence+=line[4][0]
        #sequences[i-1]=sequence
        if sequence[0:3]!="ATG":
            if Seq(sequence).complement()[0:3]!="ATG":
                if Seq(sequence).reverse_complement()[0:3]!="ATG":
                    print Seq(sequence).reverse_complement().complement()
                else: print Seq(sequence).reverse_complement()
            else: print Seq(sequence).complement()
        else: print sequence

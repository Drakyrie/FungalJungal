#Parses through CodeML output to find the average Dn/Ds for each gene based on all genome pairwise comparisons
#Does not include values into the average if either the Dn or Ds equals 0
#Also outputs the 17 Dn/Ds compared to NZE8
import os
dir="C:/Users/asim/Desktop/Dothistroma/CDS_sequences/results/"
output=open("DnDs.csv",'w')
for file in os.listdir(dir):
    input=open(dir+file)
    isMatrix=False
    NZE8=[]
    count=0
    sum=0
    for line in input:
        #if reached part with the correct information
        if isMatrix:
            #print line
            #parse through the matrix and sum values
            for i in range(len(line.split('('))):
                value=line.split('(')[i][-8:].strip()
                if ")" not in value and "-" not in value:
                    count+=1
                    sum+=float(value)
                #collect NZE8 values seperately
                if line.split()[0]=="14" and ")" not in value:
                    NZE8.append(value)
                if i==13  and ")" not in value:
                    NZE8.append(value)
        #determine when to start/end processing lines
        if len(line.split())>0:
            if line.split()[0][0]=="1":
                isMatrix=True
            if line.split()[0]=="18":
                output.write(file.split(".")[0]+",")
                if count==0:
                    output.write("No Ds,")
                else:
                    output.write(str(sum/count)+",")
                for value in NZE8:
                    output.write(value+",")
                output.write("\n")
                break
    #break

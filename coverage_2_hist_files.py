#generates several files per scaffold which has a column for coverage and its cooresponding % of bases to be used in R to plot the coverage histograms
import os
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/coverage/"
for file in os.listdir(dir):
    os.mkdir("hists/"+file)
    input=open(dir+file)
    scaffolds=[]
    scaffolddict={}
    for line in input:
        line=line.split() #scaffold_1    0(coverage)    110929(bases with this coverage)    5111597(bases on scaffold)    0.0217014(percentage of scaffold)
        if "genome" not in line[0]:
            if int(line[0].split("_")[3])<1000:continue
        if line[1]=="0":
            scaffolddict[line[0]]=[[line[1],line[4]]]
            scaffolds.append(line[0])
        else:
            if line[0] not in scaffolddict: 
                scaffolddict[line[0]]=[[line[1],line[4]]]
                scaffolds.append(line[0])
            else: scaffolddict[line[0]].append([line[1],line[4]])
    for scaffold in scaffolds:
        output=open("hists/"+file+"/"+scaffold+".csv",'w')
        for value in scaffolddict[scaffold]:
            output.write(value[0]+','+value[1]+'\n')
        output.close()
                
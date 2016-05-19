import os
#takes output from samtools genome cov and generates statistics of coverage for each scaffold for each sample. These are % of bases with 0 coverage, the percentage of bases at mode coverage, and the mode coverage
dir="C:/Users/Andre/Desktop/Linux/AGRF_CAGRF11237_C80GLANXX/coverage/"
for file in os.listdir(dir):
    scaffoldlist=[]
    input=open(dir+file)
    max=[0,0]
    for line in input:
        line=line.split() #scaffold_1    0(coverage)    110929(bases with this coverage)    5111597(bases on scaffold)    0.0217014(percentage of scaffold)
        if line[1]=="0":
            if scaffoldlist!=[]:scaffoldlist[-1]=scaffoldlist[-1]+max
            scaffoldlist.append([line[0],line[4]])
            max=[0,0]
        if float(line[4])>float(max[1]) and line[1]!="0":
            max=[line[1],line[4]]    
    scaffoldlist[-1]=scaffoldlist[-1]+max
    print"\n"+file,
    for scaffold in scaffoldlist:
        #print scaffold[0],
        print scaffold[1],scaffold[3],scaffold[2],
        
'''print "\n"       
for i in range(1,18):
    print "SC"+str(i)+"_%cov_@_0",
    print "SC"+str(i)+"_mode_%cov",
    print "SC"+str(i)+"_cov_@_mode",
'''
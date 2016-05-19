import os
for dir in os.listdir("C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/de_novo"):
    if "_C" in dir:
        alignment=open("C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/de_novo/"+dir+"/K77/nucmer_layout.filter")
        contigs=open("C:/Users/Andre/Desktop/Work files/Dothistroma/2015-2016/de_novo/"+dir+"/K77/final_contigs.fasta")
        output=open("unaligned_contigs/"+dir+".fa",'w')
        selected_contigs=[]
        for line in alignment:
            if "scaffold_12" in line: line=line.split()
            else: continue
            if "scaffold_12" in line[0]: selected_contigs.append(line[1])
        for line in contigs:
            if ">" in line:
                flag=False
                if line[1:].strip() in selected_contigs:
                    flag=True
                    output.write(line)
            else:
                if flag==True:
                    output.write(line)
        alignment.close()
        contigs.close()
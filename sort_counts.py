import os
E1_file=[]
M1_file=[]
L1_file=[]
FM1_file=[]
E2_file=[]
M2_file=[]
L2_file=[]
FM2_file=[]
for filename in os.listdir("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts"):    
    if "processed" not in filename:
        #file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
        if "ER1_" in filename or "H8DE3" in filename:
            E1_file.append(filename)
        if "ER2_" in filename:
            E2_file.append(filename)
        if "MR1_" in filename:
            M1_file.append(filename)
        if "MR2_" in filename:
            M2_file.append(filename)
        if "LR1_" in filename:
            L1_file.append(filename) 
        if "LR2_" in filename:
            L2_file.append(filename)
        if "ER1NEW" in filename:
            FM1_file.append(filename)
        if "ER2NEW" in filename:
            FM2_file.append(filename)
file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
length=len(file.readlines())
E1=[0]*length
E2=[0]*length
M1=[0]*length
M2=[0]*length
L1=[0]*length
L2=[0]*length
FM1=[0]*length
FM2=[0]*length
file.close()
for filename in E1_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        E1[i]+=int(filelines[i].split()[1])
for filename in E2_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        E2[i]+=int(filelines[i].split()[1])
for filename in M1_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        M1[i]+=int(filelines[i].split()[1])
for filename in M2_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        M2[i]+=int(filelines[i].split()[1])
for filename in L1_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        L1[i]+=int(filelines[i].split()[1])
for filename in L2_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        L2[i]+=int(filelines[i].split()[1])
for filename in FM1_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        FM1[i]+=int(filelines[i].split()[1])
for filename in FM2_file:
    file=open("C:/Users/Andre/Desktop/Linux/Dothi/novel_counts/"+filename)
    filelines=file.readlines()
    for i in range(len(filelines)):
        FM2[i]+=int(filelines[i].split()[1])
output=open("novel_counts.csv","w")        
for i in range(len(E1)):
    output.write(filelines[i].split()[0]+","+str(E1[i])+","+str(E2[i])+","+str(M1[i])+","+str(M2[i])+","+str(L1[i])+","+str(L2[i])+","+str(FM1[i])+","+str(FM2[i])+"\n")
    
        
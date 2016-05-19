file=open("timeseries_ToReadByCode.csv")

pp=[]
po=[]
pn=[]
op=[]
oo=[]
on=[]
np=[]
no=[]
nn=[]

file.readline() #GeneNames,E RPMK,M RPMK,E-M,q-value(Storey et al. 2003),sig,M RPMK,L RPMK,M-L,q-value(Storey et al. 2003),sig
for line in file:
    line=line.split(",")
    if(int(line[5])==1 and float(line[3])>1):
        if(int(line[10])==1 and float(line[8])>1):
            pp.append(line[0])
        if(int(line[10])==1 and float(line[8])<1):
            pn.append(line[0])
        if(int(line[10])==0):
            po.append(line[0])
    if(int(line[5])==1 and float(line[3])<1):
        if(int(line[10])==1 and float(line[8])>1):
            np.append(line[0])
        if(int(line[10])==1 and float(line[8])<1):
            nn.append(line[0])
        if(int(line[10])==0):
            no.append(line[0])
    if(int(line[5])==0):
        if(int(line[10])==1 and float(line[8])>1):
            op.append(line[0])
        if(int(line[10])==1 and float(line[8])<1):
            on.append(line[0])
        if(int(line[10])==0):
            oo.append(line[0])
        
ppf=open("pp",'w')
for line in pp:
    ppf.write(line)
    ppf.write("\n")

pof=open("po",'w')
for line in po:
    pof.write(line)
    pof.write("\n")

pnf=open("pn",'w')
for line in pn:
    pnf.write(line)
    pnf.write("\n")

opf=open("op",'w')
for line in op:
    opf.write(line)
    opf.write("\n")

oof=open("oo",'w')
for line in oo:
    oof.write(line)
    oof.write("\n")

onf=open("on",'w')
for line in on:
    onf.write(line)
    onf.write("\n")

npf=open("np",'w')
for line in np:
    npf.write(line)
    npf.write("\n")

nof=open("no",'w')
for line in no:
    nof.write(line)
    nof.write("\n")

nnf=open("nn",'w')
for line in nn:
    nnf.write(line)
    nnf.write("\n")

print len(pp)
print len(po)
print len(pn)
print len(op)
print len(oo)
print len(on)
print len(np)
print len(no)
print len(nn)
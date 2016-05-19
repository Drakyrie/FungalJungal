from Bio import SearchIO
queries=[]
for qresult in SearchIO.parse("B7ZGAT9Y114-Alignment.xml",'blast-xml'):
    queries.append(qresult)
print queries[0]
import os
import time
from Bio import Entrez
Entrez.email = "1959720480@qq.com"

av_filename = "/home/whosy/mydata/mitochondral/zaolei/00_streptophyta/id_todownload"
#seq_filename = "replicon.fa"
input_handle = open(av_filename,"r")
#output_handle = open(seq_filename,"w")
#res = ""
for line in input_handle:
    iline = line
    name = line.strip()
    time.sleep(4)
    search_handle = Entrez.esearch(db="nuccore",term=iline,usehistory="y")
    search_results = Entrez.read(search_handle)
    search_handle.close()
    #res.append(search_results)
    gi_list = search_results["IdList"]
    count = int(search_results["Count"])
    assert count == len(gi_list)
    webenv = search_results["WebEnv"]
    query_key = search_results["QueryKey"]
    batch_size = 3
    out_handle = open(name, "w")
    for start in range(0,count,batch_size):
        end = min(count, start+batch_size)
        print ("Going to download record %i to %i" % (start+1, end))
        fetch_handle = Entrez.efetch(db="nuccore", rettype="gb", retmode="text",retstart=start, retmax=batch_size,webenv=webenv, query_key=query_key)
        data = fetch_handle.read()
        fetch_handle.close()
        out_handle.write(data)
    out_handle.close()
input_handle.close()
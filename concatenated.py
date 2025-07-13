from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

trimedpath = "/home/whosy/mydata/mitochondral/alldata/landplants_genes/genes/gene_process_re/11_process3/rere_process/12_edited_mannual/000_megaedit_pep"
allidspath = "/home/whosy/mydata/mitochondral/alldata/landplants_genes/genes/gene_process_re/11_process3/rere_process/12_edited_mannual/0000allids"
outfile = "/home/whosy/mydata/mitochondral/alldata/landplants_genes/genes/gene_process_re/11_process3/rere_process/12_edited_mannual/concatenated_pep/concatenated_all_cds_1c.fa"
sitefile = "/home/whosy/mydata/mitochondral/alldata/landplants_genes/genes/gene_process_re/11_process3/rere_process/12_edited_mannual/concatenated_pep/site_info1"
sitefile2 = "/home/whosy/mydata/mitochondral/alldata/landplants_genes/genes/gene_process_re/11_process3/rere_process/12_edited_mannual/concatenated_pep/site_info2"

#所有id
with open(allidspath,"r") as f:
    allidlist = [lines.strip() for lines in f]

trimfile_list = os.listdir(trimedpath)
dir2 = {}
ii = 0
for trimfile in trimfile_list:
    filedict = SeqIO.to_dict(SeqIO.parse(trimedpath+os.sep+trimfile,"fasta"))

    first_record = next(SeqIO.parse(trimedpath+os.sep+trimfile,"fasta"))
    seqlen = len(first_record.seq)
    ii1 = ii+1
    ii +=  seqlen
    
    with open(sitefile,"a") as sitef:
        sitef.write(trimfile.replace(".fa","") +"\t"+ str(seqlen)+"\n")
    with open(sitefile2,"a") as sitef2:
        sitef2.write(trimfile.replace(".fa","")+"_pos1"+" = "+str(ii1)+"-"+str(ii)+"\\3;"+"\n"+
        trimfile.replace(".fa","")+"_pos2"+" = "+str(ii1+1)+"-"+str(ii)+"\\3;"+"\n"+
        trimfile.replace(".fa","")+"_pos3"+" = "+str(ii1+2)+"-"+str(ii)+"\\3;"+"\n")

    dir = {}
    for allids in allidlist:       
            
            if allids in filedict.keys():
                dir[allids] = str(filedict[allids].seq)
            else:
                dir[allids] = "-" * seqlen
    if dir2=={}:
        dir2 = dir
    else:
        for k,v in dir.items():
            dir2[k] += dir[k]
for k,v in dir2.items():
    print(k+"\t%d" %(len(v)))
    print("%d seqs were cincatenated" %(len(list(dir2.keys()))))
    with open(outfile,"a") as out:
        out.write(">" + k +"\n" + v +"\n")



        


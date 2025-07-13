import sys
from Bio import SeqIO
from Bio.Seq import Seq

args = sys.argv
input_f = args[1]
output_f = args[2]

# input_f = "/home/whosy/workspace/re_jul28/Results_Jul28/Orthogroups/astral/LCN5_80-singlec_65_ogseq3/cdsextract/cds_extracted_aligned/OG0008758.fa"
# output_f = "/home/whosy/workspace/re_jul28/Results_Jul28/Orthogroups/astral/LCN5_80-singlec_65_ogseq3/cdsextract/cds_extracted_aligned_12/test"

output_fo = open(output_f,"w")
for records in SeqIO.parse(input_f,"fasta"):
    id1 = records.id
    n = 0
    seq = Seq("")
    all_seq = records.seq
    lenth = int(len(all_seq)/3)
    for i in range(0,lenth):
        seq += all_seq[n:n+2]
        n += 3
    output_fo.write(">"+id1 +"\n" + str(seq)+"\n")
output_fo.close()


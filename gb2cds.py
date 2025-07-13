# _*_ coding: utf-8 _*_

"genbank2cds"

_author_ = "hushuaiya"

import shutil,os    #1shutil用于移动文件
from Bio.Seq import Seq
from Bio import SeqIO 
from Bio.SeqFeature import SeqFeature, FeatureLocation

def fasta(gbpath,fapath):
    
#mypath = input("please input your abspath:")
    for x in os.listdir(gbpath):   #'mapath'no 不能加引号。遍历路径文件夹里的所有文件
        #name = x
        # gbk_filename = name
        # faa_filename = name + ".fasta"     #变量加字符串命名

        input_handle  = open(gbpath + x,"r")
        output_handle = open(fapath+ x , "w")  #路径是字符串类型
        
        record = SeqIO.read(input_handle, "genbank")
        for feature in record.features:
            #if feature.qualifiers["key"] != "gene":   #key为可变字符（变量？）不能用于表示字典键
            qua = feature.qualifiers    #要赋值给变量，不能直接作为下一句not in 的对象（为什么？）
            if "gene" not in qua:       #判断键是否在字典中
                continue

            elif feature.type == "CDS":
                fa_seq =  feature.extract(record.seq)    #.reverse_complement()。不用反向互补
                gene_name = feature.qualifiers["gene"][0]       #qualifiers是字典对象，字典的值是列表
                output_handle.write(">%s\n%s\n" % (gene_name,fa_seq))
                #shutil.move('/home/whosy/文档/my_code/test/faa_filename','/home/whosy/文档/my_code/test_fa')
        output_handle.close()
        input_handle.close()
if __name__ == "__main__":   
    gbpath = input("please input you genbank absolute path(/):")
    fapath = input("please input you fasta absolute path(/):")
    fasta(gbpath,fapath)
       
    
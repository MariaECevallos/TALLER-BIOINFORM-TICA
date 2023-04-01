from Bio import SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Entrez
from Bio import SeqIO 
import csv 
import re 
import matplotlib
import matplotlib.pyplot as plt
from Bio.Align.Applications import ClustalwCommandline
import os

with open("seq.txt", "r") as gen1:
    id_seq = gen1.readlines()
    #id_seq_list = ",".join(gen11.split("\n")).split(",")
    #id_seq = gen12.readlines()
    list_seq= [ ]
    for ids in id_seq:
         handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
         Entrez.email = "mecr23mm@gmail.com"
         secuencias = SeqIO.read(handle, "fasta")
         list_seq.append(secuencias)
         SeqIO.write(list_seq, "info.fasta", "fasta")
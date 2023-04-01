from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pdb
listado=[]
for seq in SeqIO.parse("info.fasta", "fasta"):
    caracter= seq.seq
    prot=caracter.translate()
    lista= [linea.strip() for linea in prot]
        
    def peso_molecular(proteinas):
        peso= []
        for amino in proteinas:
            analisis= ProteinAnalysis(str(prot))
            weight= analisis.molecular_weight()
            peso.append(weight)
            #print (peso)
            pdb.set_trace()
        return peso
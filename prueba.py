dna = "ATGTTCGGT"
ultimo = len(dna)-2
codones = []
for ini in range(0,ultimo,3):
    codon = dna[ini:ini+3]
    codones.append(codon)
    print(codones)
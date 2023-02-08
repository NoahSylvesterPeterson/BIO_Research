from BioInfer import *

seqs = ReadMultiFromFASTA("Globin_seq.fasta", Discriptor = True)
for i in seqs:
    print(i)
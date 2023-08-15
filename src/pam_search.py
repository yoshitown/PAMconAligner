from Bio import SeqIO
from collections import defaultdict

# Given gRNA sequences
gRNA_seq = ['GGATTTTAAATTTTGCCTTTGG', 'TAAAGATTATAATACAAGTGGG', 'GGATTTTTATAATCTTTGATGG', 
            'CTTTAATTGCGCTTGATAATGG', 'GGTGTAGTTAAAGATACAAAGG', 'AAAAGTATTTTTGCCCTCTTGG', 
            'GTGCCTGCTTTTAAAGAATTGG', 'AAGAATTGGCAAGAAAAATAGG', 'GCTTAAATAAACTTTCTTATGG', 
            'TTCAAAAATCGATACCTTTTGG', 'AAAATCGATACCTTTTGGCTGG', 'AAAAAATTTATGCCAAAACAGG', 
            'TAAATTTAGCTTGGATTGTTGG']

# Genome sequence reading
genome_seq = SeqIO.parse("/content/drive/MyDrive/creat_grna/similar_DNAs.fasta", "fasta")

# defaultdict initialization to count off-targets
off_targets_count = defaultdict(int)

# Compare gRNA sequences with each genome sequence and count off-targets
for genome in genome_seq:
    genome_seq_str = str(genome.seq)
    for gRNA in gRNA_seq:
        off_targets_count[gRNA] += genome_seq_str.count(gRNA)

# Print off-target counts
for gRNA, count in off_targets_count.items():
    print(f"{gRNA}: {count} off-targets")
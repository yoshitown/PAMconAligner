import os
import subprocess
import sys
import pandas as pd
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline

def align(target_sequences,simillar_seqencens): 
    def run_muscle(target_sequences, simillar_seqencens):
        muscle_cline = MuscleCommandline(input=target_sequences, out=simillar_seqencens)
        aligned_seqs = muscle_cline()
        return aligned_seqs

    if not os.path.isfile(target_sequences):
        print(f"Input file '{target_sequences}' not found.")
    else:
        stdout, stderr = run_muscle(target_sequences, simillar_seqencens)
        print("Alignment completed.")
    return stdout, stderr
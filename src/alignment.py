import os
import subprocess
import sys
import pandas as pd
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline

if len(sys.argv) > 1:
    filepath = sys.argv[1]
    input_file = filepath
else:
    print("CSVファイルのパスを指定してください。")
def run_muscle(input_file, output_file):
    muscle_cline = MuscleCommandline(input=input_file, out=output_file)
    stdout, stderr = muscle_cline()
    return stdout, stderr
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Input file '{input_file}' not found.")
else:
    stdout, stderr = run_muscle(input_file, output_file)
    print("Alignment completed.")
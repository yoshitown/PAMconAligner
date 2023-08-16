#アライメントされた配列からコンセンサス配列を生成する関数
from Bio import AlignIO
from Bio.Align import AlignInfo

# アライメントファイルを読み込む
alignment = AlignIO.read(r"G:\マイドライブ\creat_grna\alignment.fasta", "fasta")  

# AlignInfoオブジェクトを作成
summary_align = AlignInfo.SummaryInfo(alignment)

# コンセンサス配列を取得
consensus_seq = summary_align.dumb_consensus()

# コンセンサス配列を文字列に変換
consensus_seq_str = str(consensus_seq)

# 出力ファイル名
output_file = "consensus_sequence.fasta"

# FASTAファイルにコンセンサス配列を書き込む
with open(output_file, "w") as f:
    f.write(">Consensus_Sequence\n")
    f.write(consensus_seq_str + "\n")

print(f"Consensus sequence has been written to '{output_file}'.")
print("Consensus sequence:")
print(consensus_seq_str)
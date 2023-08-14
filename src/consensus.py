#アライメントされた配列からコンセンサス配列を生成する関数
from Bio import AlignIO
from Bio.Align import AlignInfo
# # スクリプトのあるディレクトリのパスを取得
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # アライメントファイルの相対パスを指定する
# alignment_file_path = os.path.join(current_dir, "input_gene.fasta")
# アライメントファイルを読み込む
alignment = AlignIO.read(r"G:\マイドライブ\creat_grna\alignment.fasta", "fasta")  

# AlignInfoオブジェクトを作成
summary_align = AlignInfo.SummaryInfo(alignment)

# コンセンサス配列を取得
consensus_seq = summary_align.dumb_consensus()

# コンセンサス配列を文字列に変換
consensus_seq_str = str(consensus_seq)

# 出力ファイル名
output_file = "consensus_sequence.txt"

# テキストファイルにコンセンサス配列を書き込む
with open(output_file, "w") as f:
    f.write(consensus_seq_str)

print(f"Consensus sequence has been written to '{output_file}'.")
print("Consensus sequence:")
print(consensus_seq_str)

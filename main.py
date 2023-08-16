import argparse
from src import alignment, consensus, pam_search
from src.fetch_sequences import fetch_from_ncbi  # 仮にfetch_ncbi_sequencesという関数名で関数化した場合
    # if len(sys.argv) > 1:
    #     # filepath = sys.argv[1]
    #     else:
        # print("CSVファイルのパスを指定してください。")
def main(args):
    email = "your_email@example.com"
    search_term = "extended-spectrum beta-lactamase class A"
    output_path = r"C:\Users\yoshi\OneDrive\ドキュメント\GitHub\PAMconAligner_iGEM\data\ESBL_classA_DNAs.fasta"
    # 入力FASTAファイルからのデータの読み込み
    sequences = read_fasta(args.input)
    # NCBIから配列を取得して保存する
    simillar_seqencens=fetch_from_ncbi(email, search_term, output_path)  

    # アライメントの実行
    aligned_sequences,align_erro = alignment.align(sequences,simillar_seqencens)

    # コンセンサス配列の取得
    consensus_sequence = consensus.get_consensus(aligned_sequences)

    # PAM配列の検索
    pams = pam_search.find_pams(consensus_sequence)

    # # 最大公約数のPAMを検索
    # common_pam_sequence = common_pam.find_common(pams)

    # 結果の表示または保存
    print("Common PAM:")

def read_fasta(filename):
    with open(filename, 'r') as f:
        # FASTAファイルの読み込みとシーケンスの返却の簡単なロジック
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find common PAM sequences from aligned sequences.")
    parser.add_argument('input', type=str, help='Path to the input FASTA file.')

    args = parser.parse_args()
    main(args)
    

from Bio import Entrez, SeqIO

def fetch_from_ncbi(email, search_term, output_path, database='nucleotide', retmax=10):
    """
    Fetch sequences from NCBI based on the given search term.
    
    Parameters:
    - email: Email address for NCBI connection.
    - search_term: Query for searching the NCBI database.
    - output_path: Path to save the fetched sequences in FASTA format.
    - database: NCBI database to search (default is 'nucleotide').
    - retmax: Maximum number of records to fetch (default is 10).
    
    Returns:
    - A message indicating the path where the sequences were saved.
    """
    
    # NCBIへの接続に必要なメールアドレスを指定します
    Entrez.email = email

    # NCBIで検索を実行し、結果を取得します
    handle = Entrez.esearch(db=database, term=search_term, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()

    # 取得した結果のIDを使用して、配列を取得します
    fasta_records = []
    for uid in record["IdList"]:
        handle = Entrez.efetch(db=database, id=uid, rettype="fasta", retmode="text")
        fasta_records.append(SeqIO.read(handle, "fasta"))
        handle.close()

    # 結果をFASTAファイルに保存します
    SeqIO.write(fasta_records, output_path, "fasta")

    return f"Sequences saved to {output_path}"

# # 使用例
# print(fetch_from_ncbi("your_email@example.com", "extended-spectrum beta-lactamase class A", "/content/drive/MyDrive/creat_grna/ESBL_classA_DNA.fasta"))

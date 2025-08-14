from Bio import SeqIO

def fastq_to_fasta(fastq_path, fasta_path):
    with open(fastq_path, 'r') as fq, open(fasta_path, 'w') as fa:
        while True:
            header = fq.readline()
            if not header:
                break  # End of file
            seq = fq.readline()
            plus = fq.readline()
            qual = fq.readline()
            # Check for incomplete records
            if not seq or not plus or not qual:
                break
            if not header.startswith('@') or not plus.startswith('+'):
                continue  # Skip malformed records
            fa.write(f'>{header[1:].strip()}\n{seq.strip()}\n')

if __name__ == "__main__":
    fastq_file = "/home/rajpalh/DISSO_PAT/FASTQ_files/combined.fastq"
    fasta_file = "/home/rajpalh/DISSO_PAT/FASTQ_files/combined.fasta"
    fastq_to_fasta(fastq_file, fasta_file)

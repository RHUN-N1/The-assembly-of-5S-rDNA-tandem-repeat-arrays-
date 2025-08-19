# The-assembly-of-5S-rDNA-tandem-repeat-arrays-

# FASTQ to FASTA Converter

## Overview  
This repository contains a simple Python script to convert **FASTQ** files into **FASTA** format.  
The script reads sequencing data from a FASTQ file, validates record structure, and outputs a clean FASTA file containing only sequence identifiers and bases.

## Features  
- ✅ Reads standard FASTQ format (4‑line records).  
- ✅ Skips malformed or incomplete records to prevent downstream issues.  
- ✅ Produces a FASTA file compatible with most bioinformatics tools.  
- ✅ Minimal dependencies — uses only Python’s built‑in file handling.

## Requirements  
- Python 3.x  
- (Optional) [Biopython](https://biopython.org/) — although `SeqIO` is imported here, this version uses native file reading/writing.

## Usage  

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Set your input and output file paths** in the script:
   ```python
   fastq_file = "/path/to/input.fastq"
   fasta_file = "/path/to/output.fasta"
   ```

3. **Run the script**:
   ```bash
   python fastq_to_fasta.py
   ```

4. **Output**: A `.fasta` file containing the sequences from your original FASTQ file.

## Script Logic  
The script:
1. Reads the FASTQ file **4 lines at a time**:  
   - `@header` (sequence ID)  
   - `sequence`  
   - `+` (separator)  
   - `quality`  
2. Verifies that the header and separator lines are properly formatted.  
3. Writes the header (as `>header`) and sequence to the FASTA file.  

## Example  
**Input** (FASTQ):
```
@seq1
ATCGATCGATCG
+
IIIIIIIIIIII
```
**Output** (FASTA):
```
>seq1
ATCGATCGATCG
```

## Notes  
- If you plan to process large FASTQ files or use additional formats, consider using Biopython’s `SeqIO` for efficiency and built‑in validation:
  ```python
  from Bio import SeqIO
  SeqIO.convert("input.fastq", "fastq", "output.fasta", "fasta")
  ```
- Adjust the file paths to match your local or HPC environment.

#!/usr/bin/env bash
echo "Enter sequence file path:"
read filepath
outputfile = $filepath"_ALIGNED.fasta"

clustalw -align -infile=$filepath -gapopen=10 -gapext=0.2 -output=PIR -outfile=$outputfile
raxml-ng --all --msa $outputfile --model TPM3+G+I --bs-trees 1000

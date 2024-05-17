#!usr/bin/bash)
echo "Enter sequence file path:"
read filepath
raxml-ng --all --msa $filepath --model TPM3+G+I --bs-size 1000
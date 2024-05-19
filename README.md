# Scripts for Phylogenetic Analysis
Contains all the scripts used to perform simple phylogenetic analysis using ClustalW alignments, MPBoot for Maximum Parsimony tree creation (with 1000 replicate branch support assessments) RAxML Next Generation for Maximum Likelihood tree creation (TPM3+G+I as a model, bootstrapping analysis of 1000 replicates).

## Usage
### Tree Creation script
***WARNING: You MUST have ClustalW, MPBoot and RAxML Next Generation installed for the script to run or it will NOT work.***
Insert the full path for your sequence file. The script will then use ClustalW to align the sequence, followed by the tree creation. It should output all the trees with the corresponding bootstrap values, using both the Maximum Parsimony and Maximum Likelihood methods.

### Tree Writer
#### Mandatory arguments
You must use these arguments in order for the tree SVG creation to work.

`-i` or `--input`: Input tree file.

`-r` or `--root`: Tree root/outgroup identifier.

`-o` or `--output`: Output SVG file (use the .svg suffix to avoid issues).

## Credits
These scripts were developed by fonors, goncalof21, MadalenaFranco2 & scmdcunha.

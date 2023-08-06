Contents of this File:
Introduction
Requirements
Installation
Use
Reading the Output

Introduction

The DGRpy package was developed to search for diversity-generating retroelements (or “DGRs”) in microbial genomes and assembled metagenomes. The workflow enables a user to identify primary DGR features - reverse transcriptase (RT), variable and template imperfect repeats (VR and TR, respectively), as well as non-DGR RTs. 

DGRpy searches for patterns of site-specific mutation that are preserved between TR and VR. DGR template and variable sites are typically identified by the mismatches that correspond to TR adenines. Although DGR-RT predominantly misincorporates bases at template adenines during cDNA synthesis, other mutations can arise. As such, the user should expect that some DGR TR-VR pairs will not be identified, if the number of non-adenine TR mismatches exceeds the threshold (default is set to 80% and a minimum of 5 TR-A mismatches). 

For suspected DGRs that are not found (possible false negatives), we recommend looking at the output file “RT_yourfile_summary_table.csv” and then manually inspecting the RT loci for near repeats.

The DGRpy tool uses several resources that were developed by others:

an HMM profile of RT representatives,  produced by Roux (et al. 2021):
https://doi.org/10.1038/s41467-021-23402-7
 
Prodigal for prediction of open reading frames:
https://doi.org/10.1186/1471-2105-11-119

HMMER v 3.3.2:
https://doi.org/10.1371/journal.pcbi.1002195
http://hmmer.org/


Requirements

For easier installation, it is recommended to use a conda virtual environment to install the recommended dependencies. The conda installation process is shown here. 

conda create -n <environment_name>
conda activate <environment_name>
conda install -c bioconda hmmer blast prodigal cd-hit biopython
conda install pandas

To leave the conda environment, use this command:

conda deactivate

Installation

Within your conda environment, install the DGRpy package using the following command. 

python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade DGR-package-anu

Use

Prior to running a genome file or a folder of genome files, download the Custom_DGR_RT.hmm file (linked here) in the same directory you are running the call to the python package in. This same directory is where the output files will be generated. The accepted file formats are .fasta and .fa. 

In your preferred directory, enter the python environment. This can be done by typing python or python3 into your terminal window. At the python prompt enter the following commands:

import DGR_package
from DGR_package import run_module

Next, run the following to search for DGRs/RTs in a single genome fasta file :
run_module.run_file_path("single_genome_filename.fasta")

*** Note: if running the single file command do not combine assemblies of more than one organism (see directory command below for multiple genomes)

*OR* Run the following command to search a set of genomes within a directory (genomes should be stored as separate fasta files in the directory):
run_module.run_folder_path("/path_to_genome_folder")

When done using the python environment, you can type exit() and hit enter. 

Reading the Output:
The primary DGR search results can be found in the folder named “$yourfile_output”. This folder should contain five files, including:

1) Nucleotide sequence file of all RTs identified by DGRpy (both DGR and non-DGR RTs) 
2) Nucleotide sequence file of all template repeats (TRs)
3) Nucleotide sequence file of all variable repeats (VRs)
4) “RTs_$yourfile_summary_table.csv” coordinates and summary of all RTs identified
5) “TR_VR_RT_$yourfile_summary_table.csv” coordinates and summary of DGR features RT, TR, VR

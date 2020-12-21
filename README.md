# summarytable
**real time data processing result summary at NSLS-II MX beamlines**</br>
D. Kreitler, 18Dec2020

summarytable is a bash shell script that summarizes results from within mx data directories created by LSDC.

The script does the following:
* parses fast_dp.xml or autoPROC.xml files from auto processing pipelines
* prints the results to console in real time as results are available
* Concurrently updates result summaries to a file called "fast_dp.summary.txt"

# Set-up
This script is meant to be run on a node within the NSLS-II controls network that has access to GPFS.</br>
Add the following command to your .bashrc file:</br>

export PATH=$PATH:/GPFS/CENTRAL/xf17id2/dkreitler/projects/summarytable/bin</br>

# Usage
Multiple users can monitor data directories in real time.</br>
In your mx data directory, cd to the fast_dp_dir directory</br>

run:</br>
summarytable

# Output
Summary table of results will be updated in a file named fast_dp.summary.txt in the working directory<\br>
This file can be opened in Microsoft Excel or LibreOffice using spaces as a delimiter.



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
Summary table of results will be updated in a file named fast_dp.summary.txt in the working directory</br>
This file can be opened in Microsoft Excel or LibreOffice using spaces as a delimiter.
```
/GPFS/CENTRAL/xf17id2/inhouse/Startup-2020-03/mx305000-69
                             |---------------Overall------------------||-------------Outer-Shell----------------|
                  Sample Path     Hi     Lo  R_mrg   cc12   comp   mult     Hi     Lo  R_mrg   cc12   comp   mult        symm      a      b      c  alpha   beta  gamma
             Mpro-oil-apo-2/4   2.44  28.00  0.112   0.98  98.50   3.50   2.44   2.50  0.498   0.73  96.20   3.60     C 1 2 1  114.2   54.0   44.8   90.0  101.3   90.0
             Mpro-oil-apo-3/3   2.47  27.70  0.097   0.99  99.60   3.50   2.47   2.53  0.664   0.72  97.70   3.50     C 1 2 1  113.2   53.6   44.6   90.0  101.9   90.0
             Mpro-oil-apo-4/4   2.54  27.58  0.100   0.99  99.40   3.50   2.54   2.61  0.546   0.66  95.00   3.40     C 1 2 1  112.8   53.5   44.7   90.0  102.0   90.0
             Mpro-oil-apo-6/3   2.70  27.80  0.099   0.99  99.60   3.50   2.70   2.77  0.830   0.56  98.60   3.60     C 1 2 1  113.5   53.8   44.7   90.0  101.7   90.0
             Mpro-oil-apo-7/4   2.27  27.96  0.087   0.99  99.60   3.50   2.27   2.33  0.688   0.52  97.80   3.30     C 1 2 1  114.1   53.9   44.8   90.0  101.5   90.0
            Mpro-oil-apo-10/3   2.06  28.06  0.057   1.00  99.30   3.50   2.06   2.11  0.724   0.61  94.30   3.40     C 1 2 1  114.5   54.0   44.9   90.0  101.4   90.0
```

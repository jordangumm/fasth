# FAST Heuristics for querying fasta/fastq files

### Estimating number of reads
Sometimes an estimate of total reads is good enough.  By taking the first n (default=1000000) reads and creating a temporary file we can extrapolate how many reads exist in the full file based on file size difference.

Initial tests show near instantaneous read count estimation with an error of less than +/- 1%

## Install
`$ pip install https://github.com/jordangumm/fasth/archive/0.1.2.tar.gz`

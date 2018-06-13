# FAST Heuristics for querying fasta/fastq files

## Estimating number of reads
Sometimes an estimate of total reads is good enough.  By taking the first n (default=1000) reads and creating a temporary file we can extrapolate how many reads exist in the full file base on file size difference.

Initial tests show near instantaneous read count estimation with an error of +/- ?% 

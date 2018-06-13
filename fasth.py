import click
import screed
import tempfile
import sys
import os

from Bio import SeqIO


def estimate_num_reads(input_file, num_reads, lines_per_read):
    """ Return int estimate of reads"""
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            with open(input_file) as fasta:
                for i, line in enumerate(fasta):
                    tmp.write(line)
                    if i >= num_reads*lines_per_read:
                        break
                if i < num_reads*lines_per_read:
                    sys.exit('Not enough reads to meet num_reads requirement')
        tmp_file_size = os.path.getsize(path)
    finally:
        os.remove(path)

    return (os.path.getsize(input_file) / tmp_file_size) * num_reads


@click.command()
@click.argument('input_file')
@click.option('-n', '--num_reads', default=1000)
@click.option('--test/--no_test', default=False)
def estimate_reads(input_file, num_reads, test):
    tmp = open(input_file)
    tmp = tmp.readline()[0]
    if '>' == tmp:
        input_format = 'fasta'
        lines_per_read = 2
    elif '@' == tmp:
        input_format = 'fastq'
        lines_per_read = 4
    else:
        sys.exit('File does not appear to be fasa or fastq')

    read_estimate = estimate_num_reads(input_file, num_reads, lines_per_read)

    if test:
        read_truth = 0
        for record in SeqIO.parse(input_file, input_format):
            read_truth += 1
        print 'true number of reads:      {}'.format(read_truth)
        print 'estimated number of reads: {}'.format(read_estimate)

    return read_estimate


if __name__ == "__main__":
    estimate_reads()
    

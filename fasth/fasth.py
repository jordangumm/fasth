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

    return int((float(os.path.getsize(input_file)) / float(tmp_file_size)) * float(num_reads))


def query_num_reads(input_file, lines_per_read):
    with open(input_file) as fasta:
        for i, line in enumerate(fasta):
            pass
        return (i+1)/lines_per_read


def get_lines_per_read(input_file):
    tmp = open(input_file)
    tmp = tmp.readline()[0]
    if '>' == tmp:
        return 2
    elif '@' == tmp:
        return 4
    else:
        sys.exit('File does not appear to be fasa or fastq')


def estimate_reads(input_file, num_reads=1000000):
    lines_per_read = get_lines_per_read(input_file)
    return estimate_num_reads(input_file, num_reads, lines_per_read) 


@click.command()
@click.argument('input_file')
@click.option('-n', '--num_reads', default=1000000)
@click.option('--test/--no_test', default=False)
def run_experiment(input_file, num_reads, test):
    lines_per_read = get_lines_per_read(input_file)
    read_estimate = estimate_num_reads(input_file, num_reads, lines_per_read)
    print('true number of reads:      {}'.format(read_truth))

    if test:
        read_truth = query_num_reads(input_file, lines_per_read)
        print('estimated number of reads: {}'.format(read_estimate))

    return None 


if __name__ == "__main__":
    run_experiment()
    

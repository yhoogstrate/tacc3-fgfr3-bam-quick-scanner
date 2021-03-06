#!/usr/bin/env python

"""
    tacc3-fgf3-quick-bam-scanner scans for reads aligned to both TACC3
         and FGFR3, directly from BAM files.
    Copyright (C) 2021  Youri Hoogstrate

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import click
import pysam
import tqdm
import os

regions = {
    'hg38': {
        'TACC3': ['chr4', 1712615, 1751158],
        'FGFR3': ['chr4', 1790606, 1811467]},
    'hg19': {
        'TACC3': ['chr4', 1714342, 1752885],
        'FGFR3': ['chr4', 1792333, 1813194]}
}



@click.command()
@click.option("--reference-build", "-r", required=True, type=click.Choice(['hg19', 'hg38']), help="Used reference genome (needed for precise TACC3 & FGFR3 coordinates)")
@click.argument('bam_files', type=click.Path(exists=True), nargs=-1)
def tacc_fgf3_quick_bam_scan(reference_build, bam_files):
    print("%s\t%s\t%s\t%s" % ( "BAM file", "Read count TACC3", "Read count FGFR3", "Read count appearing in both" ))

    for bam_file in tqdm.tqdm(bam_files):
        
        reads_tacc3 = set([])
        reads_fgfr3 = set([])
        idx = {}
        
        with pysam.AlignmentFile(bam_file, "rb") as fh:
            header = fh.header
            
            for read in fh.fetch(regions[reference_build]['TACC3'][0], regions[reference_build]['TACC3'][1], regions[reference_build]['TACC3'][2]):
                if read.is_secondary == False and read.get_overlap(regions[reference_build]['TACC3'][1], regions[reference_build]['TACC3'][2]) > 0:
                    reads_tacc3.add(read.qname)

                    if read.qname not in idx:
                        idx[read.qname] = set()
                    idx[read.qname].add(read)

            for read in fh.fetch(regions[reference_build]['FGFR3'][0], regions[reference_build]['FGFR3'][1], regions[reference_build]['FGFR3'][2]):
                if read.is_secondary == False and read.get_overlap(regions[reference_build]['FGFR3'][1], regions[reference_build]['FGFR3'][2]) > 0:
                    reads_fgfr3.add(read.qname)

                    if read.qname not in idx:
                        idx[read.qname] = set()
                    idx[read.qname].add(read)

        combined = reads_tacc3.intersection(reads_fgfr3)
        # Export bam files - for manual curation
        #if len(combined) > 0:
            #
            #sid = bam_file.split("/")[-2]
            #sid = os.path.basename(bam_file)
            #fn = "/tmp/" + sid + ".unsorted.bam"
            #print("\n"+"/tmp/" + sid + ".sorted.bam"+"\n")
            #with pysam.AlignmentFile(fn, "wb", header=header) as fh:
            #    for _ in combined:
            #        for __ in idx[_]:
            #            fh.write(__)
            #
            #pysam.sort("-o", "/tmp/" + sid + ".sorted.bam", "/tmp/" + sid + ".unsorted.bam")
            #pysam.index("/tmp/" + sid + ".sorted.bam")
            
        
        
        print("%s\t%d\t%d\t%d" % ( bam_file, len(reads_tacc3), len(reads_fgfr3), len(combined) ))



if __name__ == '__main__':
    tacc_fgf3_quick_bam_scan()



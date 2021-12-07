
# tacc3-fgfr3-quick-bam-scanner

Scans for reads mapped to both TACC3 and FGFR3, directly from BAM files


## What it does

It counts reads that are aligned to both TACC3 and FGFR3. Secondary alignments are excluded.

## tacc3-fgfr3-bam-quick-scanner Manuscript ##

If you like to read more about the application of tacc3-fgfr3-bam-quick-scanner or when using this package for scientific purposes, please read/cite the following manuscript:

[10.1093/neuonc/noab231](https://doi.org/10.1093/neuonc/noab231)

```
Youri Hoogstrate, Santoesha A Ghisai, Maurice de Wit, Iris de Heer,
Kaspar Draaisma, Job van Riet, Harmen J G van de Werken, Vincent Bours,
Jan Buter, Isabelle Vanden Bempt, Marica Eoli, Enrico Franceschi,
Jean-Sebastien Frenel, Thierry Gorlia, Monique C Hanse, Ann Hoeben,
Melissa Kerkhof, Johan M Kros, Sieger Leenstra, Giuseppe Lombardi,
Slávka Lukacova, Pierre A Robe, Juan M Sepulveda, Walter Taal,
Martin Taphoorn, René M Vernhout, Annemiek M E Walenkamp, Colin Watts,
Michael Weller, Filip Y F de Vos, Guido W Jenster, Martin van den Bent,
Pim J French.

The EGFRvIII transcriptome in glioblastoma, a meta-omics analysis,

Neuro-Oncology, 2021; noab231,
https://doi.org/10.1093/neuonc/noab231
```

This will indirectly help me further maintaining this software package.

Thank you in advance, Youri


## Usage

```
git clone https://github.com/yhoogstrate/tacc3-fgfr3-bam-quick-scanner.git
cd tacc3-fgfr3-bam-quick-scanner

virtualenv -p python3 .venv
source .venv/bin/activate
pip install click
pip install pysam
pip install tqdm


./tacc3-fgfr3-bam-quick-scanner.py
```

```
Usage: tacc3-fgfr3-quick-bam-scanner.py [OPTIONS] [BAM_FILES]...

Options:
  -r, --reference-build [hg19|hg38]
                                  Used reference genome (needed for precise
                                  TACC3 & FGFR3 coordinates)  [required]

  --help                          Show this message and exit.

```

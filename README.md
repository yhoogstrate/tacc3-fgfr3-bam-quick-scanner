
# tacc3-fgfr3-quick-bam-scanner: Scans for reads mapped to both TACC3 and FGFR3

## What it does

It counts reads that are aligned to both TACC3 and FGFR3. Secondary alignments are excluded.

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

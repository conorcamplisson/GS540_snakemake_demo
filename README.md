# UWGS Genome 540 Snakemake Demo

[![Conda](./docs/img/conda.svg)](https://docs.conda.io/en/latest/miniconda.html)

Example Snakemake pipeline for the [Genome 540 course](http://bozeman.mbt.washington.edu/compbio/mbt599/) at [UW Genome Sciences](https://www.gs.washington.edu/)

## Installation

1. Make sure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed. 

2. Install Mamba to facilitate snakemake installation, as recommended in the [Snakemake docs](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#installation-via-conda-mamba).

```
$ conda install -n base -c conda-forge mamba
```

3. Clone this repo:

```
$ git clone https://github.com/conorcamplisson/GS540_snakemake_demo.git
```

4. Create the provided [environment](./environment.yml) using Mamba:

```
$ cd GS540_snakemake_demo/ && mamba env create -f environment.yml
```

5. Activate the new conda environment:

```
$ conda activate 540_pipeline_env
```

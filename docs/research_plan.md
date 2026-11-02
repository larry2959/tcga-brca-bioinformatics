# Research plan

## Question
Which genes differ between breast cancer and normal breast tissue, and can expression profiles separate the two?

## Objectives
1. Retrieve open-access TCGA-BRCA RNA-seq data.
2. Preprocess counts, perform QC and exploratory analysis.
3. Test gene-level differences with multiple-testing correction.
4. Train and evaluate tumour-vs-normal classifiers.
5. Interpret results cautiously and document limitations.

## Hypothesis
Tumour and normal breast tissue have distinguishable expression profiles, with a subset of genes showing statistically significant differences after multiple-testing correction.

## Scope and caution
Exploratory analysis of available samples; association does not establish causality. Model performance on a held-out subset does not establish clinical utility.

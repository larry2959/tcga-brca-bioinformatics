# TCGA-BRCA Bioinformatics Group Project

**Research question:** Which genes differ between breast cancer and normal breast tissue, and can expression profiles separate the two?

This repository analyzes open-access TCGA-BRCA RNA-seq STAR gene-expression counts from the NCI Genomic Data Commons (GDC). The project is exploratory; it is not a clinical diagnostic tool.

## Current project evidence
- Cohort described in the current presentation: 119 samples (60 primary tumour, 59 solid-tissue normal).
- Starting matrix: 60,660 genes; 4,604 all-zero genes removed; 56,056 retained.
- Exploratory differential expression: Mann–Whitney U per gene and Benjamini–Hochberg FDR.
- Classification: Logistic Regression and Random Forest, stratified holdout evaluation.
- Caveat: validate the notebook's outputs against the presentation before submission. Keep claims tied to saved outputs.

## Repository structure
- `notebooks/`: final notebook, run top-to-bottom in Google Colab and save outputs.
- `src/`: reusable code modules owned by members.
- `docs/`: research plan, data dictionary, validation log, presentation/reflection guidance.
- `member_work/`: contribution files and member-specific instructions.
- `data/`: keep raw/large downloaded data out of Git; see `.gitignore`.
- `results/`: export plots/tables used in presentation (only reproducible outputs).

## Reproducibility
1. Open the notebook in Google Colab.
2. Run cells in order; ensure the cohort/data counts are documented.
3. Save notebook with outputs.
4. Export required tables/figures and cite GDC dataset and relevant gene annotation resources.
5. Check that no raw patient-level data, credentials, or local paths are committed.

## Team workflow
Use branches and pull requests. Each member owns a task file/module and records a truthful contribution in `docs/contribution_log.csv`. No fabricated commits or contributions. The lead integrates, reviews and runs the final notebook.

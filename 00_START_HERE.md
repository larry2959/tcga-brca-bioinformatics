# TCGA-BRCA Complete Member Work Pack

This pack is based on the group's existing project: Breast Cancer Gene Expression Analysis, tumour vs normal tissue, TCGA-BRCA. The main analysis is the current Colab/Jupyter notebook.

## How to use
1. The lead uploads this pack's folders to the existing GitHub repository.
2. Each member opens their named folder and reads `INSTRUCTIONS.md` from top to bottom.
3. Each member creates the listed files, pastes/adapts the provided code, runs checks, and commits only their assigned files.
4. Member scripts are functions/modules; the central notebook must call them with the project's current variables. Never claim code ran until tested.
5. Member opens a pull request. Lead reviews, merges, then runs the full notebook in Colab.

## Project facts from current slide deck (must be revalidated against notebook outputs)
119 samples (60 tumour, 59 normal), 60,660 starting genes, 4,604 all-zero genes removed, 56,056 retained; exploratory Mann–Whitney + BH FDR; reported 20,300 FDR<0.05; ML reported 93.3% accuracy and ROC-AUC ~0.996. These are reported values, not guaranteed reproducible until the notebook is rerun.

## Shared rules
- No patient-level raw data, credentials, tokens, or large downloads in Git.
- Keep class labels, sample IDs and gene IDs aligned.
- Never fit transformations or select features using test data.
- Cite GDC and any gene/pathway annotation sources.
- Interpret association, not causality; this is not a clinical diagnostic model.
- Do not fabricate commits, results, contribution, or reflections.

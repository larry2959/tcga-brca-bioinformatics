# Timothy Muigai — Individual Project Instructions

## Role
Gene-level differential expression, BH FDR and volcano plot

## Project context
Our research question: **Which genes differ between breast cancer and normal breast tissue, and can expression profiles separate the two?** Data: open-access TCGA-BRCA RNA-seq STAR counts via NCI GDC. The central notebook is `notebooks/TCGA_BRCA_analysis.ipynb`.

## What you must do
Use the existing exploratory Mann–Whitney method. State its limitations and don't call results causal. Do not change method without discussing with Larry.

## Files you own
src/differential_expression.py; member_work/timothy/de_interpretation.md; results/differential_expression_results.csv (curated result)

## Procedure
1. Read this file and inspect the corresponding section of the existing notebook.
2. Create your assigned file(s) on your branch. Use the code file in this folder as a starting point when present.
3. Test using the real variables/data in the notebook or a small clearly labeled test fixture. Don't invent output.
4. Add a short interpretation file using observed output: method, result, meaning, limitations.
5. Commit only your assigned files and open a pull request.
6. In your PR, state what changed, how you checked it, and what remains incomplete.
7. Be ready to explain your method and result orally.

## Definition of done
- [ ] Assigned files exist and contain your own completed work.
- [ ] Code has been run or is clearly marked as untested.
- [ ] Outputs/claims match the current notebook.
- [ ] No raw data, secrets or local machine paths committed.
- [ ] PR opened and reviewed by Larry.
- [ ] Personal reflection accurately describes your own contribution.

## GitHub footprint

## GitHub footprint (do this for your own task)
1. Open the repository; select branch dropdown → View all branches → New branch.
2. Name it `work/timothy-contribution` (replace slug with your name).
3. Add/edit only your assigned files.
4. In GitHub, commit with the message below (or use the command-line workflow).
5. Open **Compare & pull request**, base `main`, compare your branch. Describe work and tests.
6. Ask Larry to review. Do not merge your own PR unless Larry has explicitly agreed.
7. After merge, update your local copy / start future work from current `main`.

Command-line alternative:
```bash
git checkout main
git pull
git checkout -b work/timothy-contribution
git add src/differential_expression.py; member_work/timothy/de_interpretation.md; results/differential_expression_results.csv (curated result)
git commit -m "feat: implement differential expression and FDR analysis"
git push -u origin work/timothy-contribution
```


**Suggested commit message:** `feat: implement differential expression and FDR analysis`

## Reflection
Use the individual reflection template in your folder. Maximum 1 page per project brief; write it yourself from actual experience.

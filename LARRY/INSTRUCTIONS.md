# Larry Seme — Individual Project Instructions

## Role
Research framing, source record, project lead integration

## Project context
Our research question: **Which genes differ between breast cancer and normal breast tissue, and can expression profiles separate the two?** Data: open-access TCGA-BRCA RNA-seq STAR counts via NCI GDC. The central notebook is `notebooks/TCGA_BRCA_analysis.ipynb`.

## What you must do
You own framing and integration. Review all member work and the current notebook; don't rewrite or claim their analysis as yours.

## Files you own
docs/research_plan.md; docs/data_source_record.md; docs/lead_review_checklist.md

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
2. Name it `work/larry-contribution` (replace slug with your name).
3. Add/edit only your assigned files.
4. In GitHub, commit with the message below (or use the command-line workflow).
5. Open **Compare & pull request**, base `main`, compare your branch. Describe work and tests.
6. Ask Larry to review. Do not merge your own PR unless Larry has explicitly agreed.
7. After merge, update your local copy / start future work from current `main`.

Command-line alternative:
```bash
git checkout main
git pull
git checkout -b work/larry-contribution
git add docs/research_plan.md; docs/data_source_record.md; docs/lead_review_checklist.md
git commit -m "docs: finalize research plan and data source record"
git push -u origin work/larry-contribution
```


**Suggested commit message:** `docs: finalize research plan and data source record`

## Reflection
Use the individual reflection template in your folder. Maximum 1 page per project brief; write it yourself from actual experience.

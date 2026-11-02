# Larry — Lead Master Guide

## Your responsibility
Own project framing, approvals, repository hygiene, review, integration, notebook execution, submission checks and coordination. Do not do all four members' technical work.

## Exact workflow
1. Upload this pack to repository `tcga-brca-bioinformatics`.
2. Send each member only their own folder path and ask them to read `INSTRUCTIONS.md`.
3. Confirm their invitation accepted and branch/PR opened.
4. Review each PR against the definition of done. Check code and output—not just commits.
5. Merge one PR at a time. Resolve conflicts by preserving the tested implementation.
6. Integrate modules into the central Colab notebook; ensure variables passed are `counts`, `labels`, `log_cpm`, and `gene_names` as applicable.
7. Run notebook from a clean Colab runtime top-to-bottom. Save outputs.
8. Compare numbers in slides/talking points with actual notebook outputs. Update all materials if values differ.
9. Confirm each member submits an individual reflection PDF (max one page).
10. Share final GitHub link and prepare presentation/Q&A.

## Lead review questions
- Can the member explain their own code?
- Does code run on actual project inputs?
- Are sample and gene IDs aligned?
- Are plots and statistics reproducible?
- Does the ML feature selection use training data only?
- Are limitations and biological claims honest?
- Is the contribution log truthful?

## Integration note
The supplied member modules are reusable functions. They are not automatically called by the notebook. After a member PR is merged, add an import/call in the notebook, or keep the existing notebook code if it is already correct and tested. Avoid duplicate calculations.

# GitHub setup (lead + all members)

## Lead
1. Sign in to GitHub and create a repository, e.g. `tcga-brca-bioinformatics`.
2. Choose **Private** while working (or Public if course rules require it); add README and Python `.gitignore`.
3. Upload/commit this starter pack, or push it from a local folder.
4. Go to Settings → Collaborators (or Manage access) → invite the other four GitHub usernames.
5. Protect `main` if available: require pull request review before merge.
6. Share the repository URL and agree on file ownership.

## Each member
1. Accept the repository invitation.
2. Install Git, then clone the repository, or use GitHub Desktop.
3. Create a branch: `work/<yourname>-task`.
4. Edit only assigned files; save.
5. Commit with a meaningful message, e.g. `docs: record GDC cohort selection`.
6. Push branch and open a pull request into `main`.
7. Request a review; fix feedback; merge only after lead approval.

## Command-line example
```bash
git clone https://github.com/ORG_OR_USERNAME/tcga-brca-bioinformatics.git
cd tcga-brca-bioinformatics
git checkout -b work/yourname-task
git add path/to/your-file
git commit -m "docs: document my project contribution"
git push -u origin work/yourname-task
```
Replace the URL and file path with actual values. Do not share passwords or tokens. GitHub commit history must reflect real work; never manufacture footprints.

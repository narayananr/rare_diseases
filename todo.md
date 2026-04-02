# Rare Disease Gene Dataset - Project Log

## Summary

Educational project providing datasets linking rare diseases to their associated genes, with interactive learning materials for high school students.

## Project Structure

```
rare_diseases/
├── data/                               # Datasets
│   ├── rare_gene_disease_dataset.csv
│   └── ensembl_genes.csv
├── scripts/                            # Data generation scripts
│   ├── fetch_rare_disease_genes.py
│   └── fetch_ensembl_genes.py
├── notebooks/                          # Course notebooks
│   ├── Rare_Disease_Genes_Class_1.ipynb   # Class 1 (Mar 27)
│   ├── Rare_Disease_Genes_HW1.ipynb       # Homework 1 (due Apr 3)
│   ├── Rare_Disease_Genes_Class_2.ipynb   # Class 2 (Apr 3)
│   ├── Rare_Disease_Genes_HW2.ipynb       # Homework 2 (due Apr 10) — portfolio setup
│   └── learn_data_analysis.ipynb          # Original combined notebook
├── .claude/agents/
│   └── notebook-reviewer.md           # Claude agent for reviewing notebooks
├── index.html                          # GitHub Pages website
└── README.md
```

## Completed Tasks

- [x] Set up GitHub repository and Pages
- [x] Create rare disease gene dataset from Orphadata
- [x] Create Ensembl gene annotations dataset
- [x] Write Python scripts with educational comments
- [x] Create interactive Jupyter notebook for learning
- [x] Organize project into clear directory structure
- [x] Split notebook into Class 1, HW1, and Class 2
- [x] Add step-by-step visualization section to HW1
- [x] Review and fix all notebooks for student clarity and code correctness
- [x] Add course schedule with Colab links to README

## Data Sources

- **Orphadata**: https://www.orphadata.com/genes/
- **Ensembl**: https://www.ensembl.org/biomart/

## Live Site

https://narayananr.github.io/rare_diseases/

---

## Upcoming

- [ ] Class 2 — April 3, 2026 (Rare_Disease_Genes_Class_2.ipynb)
- [ ] Assign HW2 in Class 2 — due April 10, 2026
- [ ] Collect HW1 submissions

## Future Goal: Student Portfolio on GitHub

Each student creates and maintains their own GitHub repo as a portfolio containing:
- Code (notebooks, scripts)
- Analysis (findings, explorations)
- Results (charts, outputs)
- Report (written summary)

### Portfolio Repo Name Decision
- Repo name: `rare-disease-genomics`
- README title: *"Computational Analysis of Tissue Specificity of Rare Disease Genes"*
- Scientific question: where in the body do rare disease genes act?
- Future: integrate GTEx gene expression data to map rare disease genes to tissue-specific expression patterns

### What needs to be built
- [x] HW2 notebook — step-by-step guide to creating a GitHub portfolio repo (Apr 3)
- [x] Example portfolio repo created locally at `~/Projects/rare-disease-portfolio-example`
  - README with full scientific title and project roadmap
  - Completed HW1 notebook (epilepsy keyword analysis)
  - results/findings.md with example written report
- [ ] Push example portfolio to GitHub as `rare-disease-genomics` and mark as template repo
  - Create repo on GitHub: github.com/narayananr/rare-disease-genomics
  - Push local repo: `cd ~/Projects/rare-disease-portfolio-example && git remote add origin git@github.com:narayananr/rare-disease-genomics.git && git push -u origin main`
  - Go to repo Settings → check "Template repository"
  - Share link with students — they click "Use this template", name it `rare-disease-genomics`, clone and replace content with their own
- [ ] Update HW2 notebook to use template workflow instead of create-from-scratch
- [ ] Guide: basic git workflow cheat sheet for students
- [ ] Guide: how to write a results/report section in a notebook
- [ ] Future project: integrate GTEx gene expression data

---

## Session Log: March 27, 2026

### Changes Made

- [x] **Fixed Colab compatibility** - Updated CSV file paths to use raw GitHub URLs so the notebook loads data directly from the repo when opened in Google Colab

- [x] **Added disease search suggestions** - Added keyword tables to Exercise 2 with suggestions for exploring the dataset:
  - Organ/system keywords: kidney, liver, eye, brain, muscle, lung
  - Condition type keywords: cancer, dystrophy, epilepsy, anemia, deafness, ataxia

- [x] **Cleared exercise cells** - Reset all exercise cells to placeholder comments so the notebook is ready for fresh use

### Files Modified

- `notebooks/learn_data_analysis.ipynb`

### Commits

1. `4befbd2` - Use GitHub raw URLs for CSV files (Colab compatibility)
2. `023bd04` - Add disease search suggestions and clear exercise cells

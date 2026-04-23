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

---

## Plan: HW3 — Visualization with Merged Datasets

**Goal:** Create `Rare_Disease_Genes_HW3.ipynb` — a visualization-focused homework using the merged rare disease + ensembl datasets. Students apply their merge skills from Class 2 and learn new chart types.

### Exercises

- [ ] **Setup cell** — Load both CSVs, merge them (quick recap, code provided)
- [ ] **Exercise 1: Rare Disease Genes by Chromosome** — Bar chart showing which chromosomes have the most rare disease genes (sorted chromosome order). Students adapt the template.
- [ ] **Exercise 2: Pie Chart — Gene Biotypes** — Introduce pie charts. Show biotype breakdown of rare disease genes vs all genes. Students create their own pie chart.
- [ ] **Exercise 3: Gene Length Comparison** — Calculate gene length (`end - start`). Compare average length of rare disease genes vs all genes using a grouped bar chart. New concept: grouped bars.
- [ ] **Exercise 4: Scatter Plot — Genes vs Disease Genes** — Introduce scatter plots. Plot total genes per chromosome vs rare disease genes per chromosome. Students interpret the correlation.
- [ ] **Exercise 5: Disease Category Chromosome Hotspots** — Pick a disease keyword, filter merged data, chart which chromosomes have the most genes for that category. Student choice of keyword.
- [ ] **Exercise 6: Student Investigation** — Open-ended: pick a question, analyze, visualize, write summary.
- [ ] **Extension: Stacked Bar Chart** — Optional challenge: stacked bar showing multiple disease categories across chromosomes.

### Style
- Same scaffolded format as HW1 (templates, hints, keyword tables)
- Step-by-step chart tutorials for new chart types (pie, scatter)
- Written reflection questions after each visualization
- Quick reference table for new chart functions

### Files to create
- [ ] `notebooks/Rare_Disease_Genes_HW3.ipynb`

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
- [ ] Update HW2 notebook to use template workflow instead of create-from-scratch ⚠️ DO NOT do this until template repo is live on GitHub and tested
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

---

## Session Log: April 12, 2026

### Topics Discussed

- **Reviewed HW2** — Confirmed `Rare_Disease_Genes_HW2.ipynb` is a GitHub portfolio setup assignment (due April 10). Students create a public repo, add their HW1 notebook, write a README and findings.md, and push to GitHub.

- **Python chaining syntax** — When chaining pandas methods across lines, the dot goes at the **start** of the next line (not end of the previous line), wrapped in parentheses:
  ```python
  avg_length = (
      genes
      .groupby('chromosome')['length']
      .mean()
  )
  ```

- **Visualization ideas** — Discussed additional plots beyond what's in the notebooks:
  1. Top diseases by gene count (horizontal bar)
  2. Gene biotype pie chart
  3. Gene length by biotype (box plot, log scale)
  4. Diseases per chromosome (bar chart from merged data)
  5. Scatter plot: total genes vs disease links per chromosome
  6. Heatmap: disease categories by chromosome

### No Files Modified

This was a discussion/review session — no code changes were made.

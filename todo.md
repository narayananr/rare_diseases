# Rare Disease Gene Dataset - Project Log

## Summary

Educational project providing datasets linking rare diseases to their associated genes, with interactive learning materials for high school students.

## Project Structure

```
rare_diseases/
├── data/                           # Datasets
│   ├── rare_gene_disease_dataset.csv
│   └── ensembl_genes.csv
├── scripts/                        # Data generation scripts
│   ├── fetch_rare_disease_genes.py
│   └── fetch_ensembl_genes.py
├── notebooks/                      # Learning materials
│   └── learn_data_analysis.ipynb
├── index.html                      # GitHub Pages website
└── README.md
```

## Completed Tasks

- [x] Set up GitHub repository and Pages
- [x] Create rare disease gene dataset from Orphadata
- [x] Create Ensembl gene annotations dataset
- [x] Write Python scripts with educational comments
- [x] Create interactive Jupyter notebook for learning
- [x] Organize project into clear directory structure

## Data Sources

- **Orphadata**: https://www.orphadata.com/genes/
- **Ensembl**: https://www.ensembl.org/biomart/

## Live Site

https://narayananr.github.io/rare_diseases/

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

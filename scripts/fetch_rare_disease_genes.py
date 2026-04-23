"""
Parse rare disease gene associations from Orphadata XML.

WHAT IS THIS SCRIPT?
--------------------
This script extracts disease-gene relationships from Orphadata,
a database of rare diseases maintained by Orphanet.

WHAT IS A RARE DISEASE?
-----------------------
A rare disease affects a small percentage of the population.
In the US, a disease is considered rare if it affects fewer than
200,000 people. Examples include cystic fibrosis, Huntington's
disease, and muscular dystrophy.

WHAT IS ORPHADATA?
------------------
Orphadata (www.orphadata.com) provides free datasets about rare
diseases. This script uses "Product 6" which lists genes associated
with each rare disease.

HOW TO GET THE DATA:
--------------------
1. Download en_product6.xml from: https://www.orphadata.com/genes/
2. Place it in the project root directory
3. Run: python scripts/fetch_rare_disease_genes.py
"""

# ============================================================
# STEP 1: Import the tools (libraries) we need
# ============================================================

# 'xml.etree.ElementTree' parses XML files (built into Python)
import xml.etree.ElementTree as ET

# 'csv' helps us write CSV files
import csv

# 'os' lets us check if files exist
import os

from datetime import datetime


# ============================================================
# STEP 2: Configuration
# ============================================================

# Get the project root directory (parent of scripts/)
import pathlib
PROJECT_ROOT = pathlib.Path(__file__).parent.parent

# Input XML file from Orphadata (in project root)
INPUT_FILE = PROJECT_ROOT / "en_product6.xml"

# Output CSV file (in data/ directory)
OUTPUT_FILE = PROJECT_ROOT / "data" / "rare_gene_disease_dataset.csv"


# ============================================================
# STEP 3: Define our functions
# ============================================================

def parse_xml(filepath):
    """
    Parse the Orphadata XML file and extract disease-gene pairs.

    The XML structure looks like this:
    <Disorder>
        <Name>Disease Name</Name>
        <DisorderGeneAssociationList>
            <DisorderGeneAssociation>
                <Gene>
                    <Symbol>GENE1</Symbol>
                    <Name>Gene 1 full name</Name>
                </Gene>
            </DisorderGeneAssociation>
        </DisorderGeneAssociationList>
    </Disorder>

    We extract each disease name and its associated genes.
    """
    print(f"Parsing {filepath}...")

    # Parse the XML file into a tree structure
    tree = ET.parse(filepath)
    root = tree.getroot()

    # List to store all disease-gene pairs
    results = []

    # Find all Disorder elements in the XML
    disorders = root.findall(".//Disorder")
    print(f"Found {len(disorders)} disorders")

    for disorder in disorders:
        # Get the disease name
        name_elem = disorder.find("Name")
        disease_name = name_elem.text if name_elem is not None else ""

        # Find all genes associated with this disorder
        genes = disorder.findall(".//Gene")

        for gene in genes:
            # Get the gene symbol (short name like "BRCA1")
            symbol_elem = gene.find("Symbol")
            gene_symbol = symbol_elem.text if symbol_elem is not None else ""

            # Get the full gene name
            gene_name_elem = gene.find("Name")
            gene_name = gene_name_elem.text if gene_name_elem is not None else ""

            # Add this disease-gene pair to our results
            if disease_name and gene_symbol:
                results.append({
                    "disease": disease_name,
                    "gene_symbol": gene_symbol,
                    "gene_full_name": gene_name
                })

    return results


def save_csv(data, filepath):
    """
    Save the disease-gene pairs to a CSV file.
    """
    print(f"Saving to {filepath}...")

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["disease", "gene_symbol", "gene_full_name"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} disease-gene associations")


# ============================================================
# STEP 4: Run the script
# ============================================================

if __name__ == "__main__":
    # Check if input file exists
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found!")
        print(f"Download it from: https://www.orphadata.com/genes/")
        exit(1)

    # Parse the XML and extract disease-gene pairs
    data = parse_xml(INPUT_FILE)

    # Save to CSV
    save_csv(data, OUTPUT_FILE)

    # Print summary
    unique_diseases = len(set(row["disease"] for row in data))
    unique_genes = len(set(row["gene_symbol"] for row in data))

    print(f"\n--- Summary ---")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Unique Diseases: {unique_diseases:,}")
    print(f"Unique Genes: {unique_genes:,}")
    print(f"Total Associations: {len(data):,}")

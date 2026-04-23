"""
Fetch basic human gene annotations from Ensembl BioMart.

WHAT IS THIS SCRIPT?
--------------------
This script downloads information about all human genes from Ensembl,
a database that scientists use to study genes and genomes.

WHAT IS A GENE?
---------------
A gene is a section of DNA that contains instructions for making proteins.
Humans have about 20,000 protein-coding genes. Each gene has:
- A unique ID (like ENSG00000141510)
- A name (like TP53, which is a famous cancer-related gene)
- A location on a chromosome (humans have 23 pairs of chromosomes)

WHAT IS ENSEMBL?
----------------
Ensembl (www.ensembl.org) is a free scientific database that stores
information about genes from many species. BioMart is their tool
for downloading data.
"""

# ============================================================
# STEP 1: Import the tools (libraries) we need
# ============================================================

# 'requests' lets us download data from websites
import requests

# 'csv' helps us write data to CSV files (like Excel spreadsheets)
import csv

# 'datetime' lets us get today's date
from datetime import datetime

# 'pathlib' helps us work with file paths
import pathlib


# ============================================================
# STEP 2: Set up the connection to Ensembl
# ============================================================

# Get the project root directory (parent of scripts/)
PROJECT_ROOT = pathlib.Path(__file__).parent.parent

# Output CSV file (in data/ directory)
OUTPUT_FILE = PROJECT_ROOT / "data" / "ensembl_genes.csv"

# This is the web address where we'll send our data request
BIOMART_URL = "https://www.ensembl.org/biomart/martservice"

# This is our "order form" telling Ensembl what data we want.
# It's written in XML format (a way to structure data).
# We're asking for these pieces of information about each gene:
#   - ensembl_gene_id: The unique identifier (like a barcode)
#   - external_gene_name: The gene's common name (like BRCA1)
#   - chromosome_name: Which chromosome the gene is on (1-22, X, Y, or MT)
#   - start_position: Where the gene starts on the chromosome
#   - end_position: Where the gene ends on the chromosome
#   - strand: Which direction the gene is read (forward=1, reverse=-1)
#   - gene_biotype: What type of gene it is (protein_coding, etc.)
#   - description: A brief description of what the gene does

QUERY = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Query>
<Query virtualSchemaName="default" formatter="TSV" header="1" uniqueRows="1">
    <Dataset name="hsapiens_gene_ensembl" interface="default">
        <Attribute name="ensembl_gene_id"/>
        <Attribute name="external_gene_name"/>
        <Attribute name="chromosome_name"/>
        <Attribute name="start_position"/>
        <Attribute name="end_position"/>
        <Attribute name="strand"/>
        <Attribute name="gene_biotype"/>
        <Attribute name="description"/>
    </Dataset>
</Query>"""


# ============================================================
# STEP 3: Define our functions (reusable blocks of code)
# ============================================================

def fetch_genes():
    """
    Download gene data from Ensembl.

    This function sends our query to the Ensembl website and
    returns the data as text.
    """
    print("Fetching gene data from Ensembl BioMart...")

    # Send the request to Ensembl (like submitting a form online)
    response = requests.get(BIOMART_URL, params={"query": QUERY})

    # Check if something went wrong (like if the website is down)
    response.raise_for_status()

    # Check if Ensembl returned an error message instead of data
    if response.text.startswith("Query ERROR"):
        raise Exception(f"Ensembl BioMart error: {response.text[:200]}")

    # Return the text data we received
    return response.text


def parse_and_save(data, output_file=OUTPUT_FILE):
    """
    Process the raw data and save it as a CSV file.

    The data comes as tab-separated text. We clean it up and
    save it as a CSV file that can be opened in Excel.
    """
    # Split the data into individual lines
    lines = data.strip().split("\n")

    # The first line contains column headers
    header = lines[0].split("\t")

    # Rename the headers to be simpler and cleaner
    header_map = {
        "Gene stable ID": "ensembl_gene_id",
        "Gene name": "gene_symbol",
        "Chromosome/scaffold name": "chromosome",
        "Gene start (bp)": "start",      # bp = base pairs (units of DNA)
        "Gene end (bp)": "end",
        "Strand": "strand",
        "Gene type": "biotype",
        "Gene description": "description"
    }
    header = [header_map.get(h, h) for h in header]

    # Open a new CSV file to write our data
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)

        # Write the header row first
        writer.writerow(header)

        # Process each gene (skip the header, start from line 2)
        count = 0
        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                # Split the line into individual fields
                fields = line.split("\t")

                # Get the chromosome value
                chrom = fields[2] if len(fields) > 2 else ""

                # Only keep genes on standard chromosomes:
                # - Chromosomes 1-22 (autosomes)
                # - X and Y (sex chromosomes)
                # - MT (mitochondrial DNA)
                # We skip scaffolds and patches (incomplete chromosome pieces)
                valid_chromosomes = [str(i) for i in range(1, 23)] + ["X", "Y", "MT"]

                if chrom in valid_chromosomes:
                    writer.writerow(fields)
                    count += 1

    print(f"Saved {count} genes to {output_file}")
    return count


# ============================================================
# STEP 4: Run the script
# ============================================================

# This block only runs when you execute this file directly
# (not when importing it as a module)
if __name__ == "__main__":
    # Download the gene data from Ensembl
    data = fetch_genes()

    # Process and save to CSV
    count = parse_and_save(data)

    # Print summary information
    print(f"\nDownload Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Total Genes: {count}")


from flask import Flask, render_template, request, jsonify
import os
import itertools as it

app = Flask(__name__)

# Function to translate DNA into protein.
def dna_to_protein(seq):
    # Makes input uppercase and removing spaces.
    seq = seq.upper().strip().replace(" ", "")
    seq = seq.replace("\n", "").replace("\r", "")

    # Check that something was entered.
    if len(seq) == 0:
        return "Error: Please enter a dna sequence."

    # Check that the sequences contains only A, C, G, and T.
    for base in seq:
        if base not in "ACGT":
            return "Error: DNA can only contain A, C, G, and T."

    # Codon dictionary
    # Each codon has a matching amino acid.
    codon_dictionary = {
    # A
    "AAA": "K", "AAC": "N", "AAG": "K", "AAT": "N",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AGA": "R", "AGC": "S", "AGG": "R", "AGT": "S",
    "ATA": "I", "ATC": "I", "ATG": "M", "ATT": "I",

    # C
    "CAA": "Q", "CAC": "H", "CAG": "Q", "CAT": "H",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",

    # G
    "GAA": "E", "GAC": "D", "GAG": "E", "GAT": "D",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",

    # T
    "TAA": "_", "TAC": "Y", "TAG": "_", "TAT": "Y",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TGA": "_", "TGC": "C", "TGG": "W", "TGT": "C",
    "TTA": "L", "TTC": "F", "TTG": "L", "TTT": "F"
    }

    # Find (ATG) start codon.
    start_position = seq.find("ATG")

    if start_position == -1:
        return "Error: No start codon (ATG) was found."

    # Storing the amino acid in an empty list.
    protein_chain = []

    # Reading the DNA 3 bases at a time.
    for i in range(start_position, len(seq) - 2, 3):

        # Get the current codon from the sequence.
        codon = seq[i:i + 3]

        # Find the amino acid for this codon.
        amino_acid = codon_dictionary[codon]

        # Stop translating at a stop codon.
        if amino_acid == "_":
            break

        # Add amino acid to the protein chain.
        protein_chain.append(amino_acid)

    # Check that a protein was made.
    if len(protein_chain) == 0:
        return "Error: No complete protein was found."

    # Join the amino acids together.
    return "-".join(protein_chain)

# Function to translate Protein into DNA.
def back_translate_to_dna(aa_sequence: str) -> list:

        # List of protein to dna possibilities.
        back_translate_code = {
            'A': ['GCA', 'GCC', 'GCG', 'GCT'],
            'C': ['TGT', 'TGC'],
            'D': ['GAC', 'GAT'],
            'E': ['GAG', 'GAA'],
            'F': ['TTT', 'TTC'],
            'G': ['GGT', 'GGG', 'GGA', 'GGC'],
            'H': ['CAT', 'CAC'],
            'I': ['ATC', 'ATA', 'ATT'],
            'K': ['AAG', 'AAA'],
            'L': ['CTT', 'CTG', 'CTA', 'CTC', 'TTA', 'TTG'],
            'M': ['ATG'],
            'N': ['AAC', 'AAT'],
            'P': ['CCT', 'CCG', 'CCA', 'CCC'],
            'Q': ['CAA', 'CAG'],
            'R': ['AGG', 'AGA', 'CGA', 'CGC', 'CGG', 'CGT'],
            'S': ['AGC', 'AGT', 'TCT', 'TCG', 'TCC', 'TCA'],
            'T': ['ACA', 'ACG', 'ACT', 'ACC'],
            'V': ['GTA', 'GTC', 'GTG', 'GTT'],
            'W': ['TGG'],
            'Y': ['TAT', 'TAC'],
            '_': ['TAA', 'TGA', 'TAG']
        }

        list_of_list_of_codons = [back_translate_code[aa] for aa in aa_sequence]

        list_of_combinations = [
        ''.join(combination)
        for combination in it.product(*list_of_list_of_codons)
        ]

        return list_of_combinations


# Flask pages:

# Home page route.
@app.route("/")
def index():
    # Name used on page title.
    user_name = "Rayan"
    return render_template("index.html", user_name=user_name)

# Testing page route
# Opens the page and POST sends dna or protein sequence.
@app.route("/testing", methods=["GET", "POST"])
def testing():
    # These are empty until user submits the dna or protein.
    protein_result = None
    dna_result = None
    submitted_dna_seq = ""
    submitted_protein_seq = ""

    # Check if the DNA sequence was submitted.
    if request.method == "POST":

        # Get the DNA or protein from the  form.
        submitted_dna_seq = request.form.get("dna_sequence", "")
        submitted_protein_seq = request.form.get("protein_sequence", "")

        # Send the submitted DNA sequence to the translator.
        protein_result = dna_to_protein(submitted_dna_seq)

        # Send the submitted protein sequence to the translator.
        dna_result = back_translate_to_dna(submitted_protein_seq)

    user_name = "Rayan"

    # Send the user input and result to the testing.html.
    return render_template(
        "testing.html",
        user_name=user_name,
        dna_sequence=submitted_dna_seq,
        protein_sequence=submitted_protein_seq,
        protein_result=protein_result,
        dna_result=dna_result
        )

# Github pages api routes:
# It gets dna from javascript and send to python result.
@app.route("/api/translate", methods=["POST"])
def translate_api():

    # Get the DNA sent from website.
    submitted_seq = request.form.get("dna_sequence", "")

    # Translate using the python function.
    protein_result = dna_to_protein(submitted_seq)

    # Send result back as JSON.
    response = jsonify({"protein_result": protein_result})

    # Allow GitHub Pages to access the api.
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response

# It gets protein from javascript and send to python result.
@app.route("/api/back-translate", methods=["POST"])
def back_translate_api():

    # Get protein sent from website.
    submitted_protein = request.form.get("protein_sequence", "")

    # Translates using python function.
    dna_result = back_translate_to_dna(submitted_protein)

    # Send result back as JSON.
    dna_response = jsonify({"dna_result": dna_result})

    # Allow GitHub Pages to access the api.
    dna_response.headers["Access-Control-Allow-Origin"] = "*"

    return dna_response

if __name__ == "__main__":
    # Run live server on port 8080.
    app.run(host="0.0.0.0", port=8080, debug=True)


from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Function for the DNA to protein translator
def dna_to_protein(seq):
    # Makes input uppercase and removing space
    seq = seq.upper().strip().replace(" ", "")

    # Check for user input
    if len(seq) == 0:
        return "Error: Please enter a dna sequence."

    # Check that the sequences contaisn only A, C, G, and T
    for base in seq:
        if base not in "ACGT":
            return "Error: DNA can only contain A, C, G, and T."

    # Genetic codon list
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
    "TAA": "STOP", "TAC": "Y", "TAG": "STOP", "TAT": "Y",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TGA": "STOP", "TGC": "C", "TGG": "W", "TGT": "C",
    "TTA": "L", "TTC": "F", "TTG": "L", "TTT": "F"
    }

    # Find the start codon
    start_position = seq.find("ATG")

    if start_position == -1:
        return "Error: No start codon (ATG) was found."

    # Storing the amino acid
    protein_chain = []

    # Reading the DNA three letters at a time
    for i in range(start_position, len(seq) - 2, 3):

        # Get the next codon
        codon = seq[i:i + 3]

        # Find the amino acid for that codon
        amino_acid = codon_dictionary[codon]

        # Stop translating at a stop codon
        if amino_acid == "STOP":
            break

        # Add amino acid to the protein
        protein_chain.append(amino_acid)

    # Make sure a protein was created
    if len(protein_chain) == 0:
        return "Error: No complete protein was found."

    # Join the amino acids together
    return "-".join(protein_chain)

# Normal flask pages:

# The main Home Page
@app.route("/")
def index():
    user_name = "Rayan"
    return render_template(
        "index.html", user_name=user_name
    )

# The testing page route
@app.route("/testing", methods=["GET", "POST"])
def testing():
    protein_result = None
    submitted_seq = ""

    # Check if the DNA sequence was submitted
    if request.method == "POST":

        # Get the DNA sequence from the form
        submitted_seq = request.form.get(
            "dna_sequence",
            ""
        )

        # Translate the DNA sequence
        protein_result = dna_to_protein(
            submitted_seq
        )

    user_name = "Rayan"
    return render_template(
        "testing.html",
        user_name=user_name,
        sequence=submitted_seq,
        protein_result=protein_result
    )

# Github pages api

@app.route("/api/translate", methods=["POST"])
def translate_api():

    submitted_seq = request.form.get(
        "dna_sequence",
        ""
    )

    protein_result = dna_to_protein(
        submitted_seq
    )

    response = jsonify({
        "protein_result": protein_result
    })

    # Allow GitHub Pages to communicate with Flask
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response

if __name__ == "__main__":
    # Run live server on port 8080
    app.run(
        debug=True, port=8080
    )

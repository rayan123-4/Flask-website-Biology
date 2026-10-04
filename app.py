
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Function to translate DNA into protein.
def dna_to_protein(seq):
    # Makes input uppercase and removing spaces.
    seq = seq.upper().strip().replace(" ", "")

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
    "TAA": "STOP", "TAC": "Y", "TAG": "STOP", "TAT": "Y",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TGA": "STOP", "TGC": "C", "TGG": "W", "TGT": "C",
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
        if amino_acid == "STOP":
            break

        # Add amino acid to the protein chain.
        protein_chain.append(amino_acid)

    # Check that a protein was made.
    if len(protein_chain) == 0:
        return "Error: No complete protein was found."

    # Join the amino acids together.
    return "-".join(protein_chain)

# Flask pages:

# Home page route.
@app.route("/")
def index():
    # Name used on page title.
    user_name = "Rayan"
    return render_template(
        "index.html", user_name=user_name
    )

# Testing page route
# Opens the page and POST sends dna sequence.
@app.route("/testing", methods=["GET", "POST"])
def testing():
    # These are empty until user submits the dna.
    protein_result = None
    submitted_seq = ""

    # Check if the DNA sequence was submitted.
    if request.method == "POST":

        # Get the DNA from the  form.
        # dna_sequence same as html name.
        submitted_seq = request.form.get(
            "dna_sequence",
            ""
        )

        # Send the submitted DNA sequence to the translator.
        protein_result = dna_to_protein(
            submitted_seq
        )

    user_name = "Rayan"

    # Send the user input and result to the testing.html.
    return render_template(
        "testing.html",
        user_name=user_name,
        sequence=submitted_seq,
        protein_result=protein_result
    )

# Github pages api route.
# It gets dna from Javascirpt and send to Python result.
@app.route("/api/translate", methods=["POST"])
def translate_api():

    # Get the DNA sent from website.
    submitted_seq = request.form.get(
        "dna_sequence",
        ""
    )

    # Translate using the python function.
    protein_result = dna_to_protein(
        submitted_seq
    )

    # Send result back as JSON
    response = jsonify({
        "protein_result": protein_result
    })

    # Allow GitHub Pages to access the api.
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response

if __name__ == "__main__":
    # Run live server on port 8080.
    app.run(host="0.0.0.0", port=8080, debug=True)

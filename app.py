
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Main Function that takes a DNA sequence and translates it into a protein.
def dna_to_protein(seq):
    # Makes input uppercase and removing space, so the input it easier to process.
    seq = seq.upper().strip().replace(" ", "")

    # Check that user entered a DNA sequence
    if len(seq) == 0:
        return "Error: Please enter a dna sequence."

    # Check that the sequences is valid and contains only A, C, G, and T
    for base in seq:
        if base not in "ACGT":
            return "Error: DNA can only contain A, C, G, and T."

    # Genetic codon list
    # Each group of three DNA bases (a codon) has a matching amino acid,
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

    # Find the position of the starting codon (ATG).
    # Once found begin translating from that point.
    start_position = seq.find("ATG")

    if start_position == -1:
        return "Error: No start codon (ATG) was found."

    # Storing the amino acid in an empty list.
    protein_chain = []

    # Reading the DNA three bases at a time because each codon contains three bases.
    for i in range(start_position, len(seq) - 2, 3):

        # Get the current three base codon from the DNA sequence.
        codon = seq[i:i + 3]

        # Find the amino acid for that specific codon, through the codon dictionary list.
        amino_acid = codon_dictionary[codon]

        # Stop translating at a stop codon.
        if amino_acid == "STOP":
            break

        # Add amino acid to the protein chain.
        protein_chain.append(amino_acid)

    # Make sure at least one amino acid was produced.
    if len(protein_chain) == 0:
        return "Error: No complete protein was found."

    # Join the amino acids together with hyphens, so that it is easy for the user to read it.
    return "-".join(protein_chain)

# Normal flask pages:

# The route for the main Home Page
@app.route("/")
def index():
    # Name displayed on the website.
    user_name = "Rayan"
    return render_template(
        "index.html", user_name=user_name
    )

# The route for the testing page route.
# It accepts a POST (dna result) and when the testing page is opened.
@app.route("/testing", methods=["GET", "POST"])
def testing():
    # These are empty until user submitted their sequence.
    protein_result = None
    submitted_seq = ""

    # Check if the DNA sequence was submitted.
    if request.method == "POST":

        # Get the DNA sequence from the form.
        # Name matches the html input field.
        submitted_seq = request.form.get(
            "dna_sequence",
            ""
        )

        # Send the submitted DNA sequence to Python, to translate it.
        protein_result = dna_to_protein(
            submitted_seq
        )

    user_name = "Rayan"

    # Send the user input and protein result back to the testing.html
    return render_template(
        "testing.html",
        user_name=user_name,
        sequence=submitted_seq,
        protein_result=protein_result
    )

# Github pages api route.
# It recieves DNA from Javascript and returns the result from the Python translator.
@app.route("/api/translate", methods=["POST"])
def translate_api():

    # Get the DNA sequence from the frontend
    submitted_seq = request.form.get(
        "dna_sequence",
        ""
    )

    # Use the same Python function to translate the DNA sequence.
    protein_result = dna_to_protein(
        submitted_seq
    )

    # Creates a JSON response containing the translated result.
    response = jsonify({
        "protein_result": protein_result
    })

    # Allow GitHub Pages to communicate with Flask backend.
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response

if __name__ == "__main__":
    # Run live server on port 8080.
    app.run(
        host="0.0.0.0", port=8080, debug=True
        )

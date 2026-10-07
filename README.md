# Flask-website-Biology
This is  my first flask website that I have using **HTML**, **CSS**, and **Python**.
- It's a website that takes DNA and translates it into proteins.
- It also translates proteins into DNA.
- All you have to do it put a DNA sequence in the result box and press submit and wait for it to translate.
- Or the other way around if your doing the protein to DNA.
- This website is made for the Stardance challenge by hack club.
- (note: it used to be for Phantom, but I decided to change it for Stardance. I didn't get any rewards from the Phantom, and I didn't ship the project. I did not double dip.)
<img width="1365" height="767" alt="Screenshot 2026-10-07 20 48 49" src="https://github.com/user-attachments/assets/ecb600e4-14eb-49c7-9d76-1baa8e6c1351" />


## Try it here:
https://bio.rayan123-4.hackclub.app/

## Features
 ## DNA to Protein
 - It will only accept DNA sequences that contain the letters A, C, G, and T. Also it must start with ATG.
 - It will automatically remove the spaces in the sequence and convert the input to uppercase.
 - It will find the start codon (ATG).
 - It Reads DNA three bases at a time as codons.
 - It translates codons into amino acids.
 - It Stops translation at a STOP codon.
 - It will give an error message for invalid DNA sequences.

 ## Protein to DNA
 - It will only accept valid Protein letters.
 - It will automatically remove the spaces in the sequence and convert the input to uppercase.
 - It translates amino acids into codons.
- It Stops translation at a STOP codon.
 - - It will give an error message for invalid Protein Chains.

 ## Clone the repository
 ```bash
 git clone https://github.com/rayan123-4/Flask-website-Biology
```

## Some resources I used:
 - https://pixabay.com/vectors/dna-helix-circles-4043148/
 - https://www.geeksforgeeks.org/python/dna-protein-python-3/
 - https://stackoverflow.com/questions/63610337/conversion-of-protein-sequence-to-dna-using-python

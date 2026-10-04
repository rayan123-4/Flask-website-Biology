# Flask-website-Biology
This is  my first flask website that I have using **HTML**, **CSS**, and **Python**.
- It's a web app that takes a DNA sequence and translates it into a protein sequence using the genetic code.
- This website is made for the Stardance challenge by hack club.
- (note: it used to be for Phantom, but I decided to change it for Stardance. I didn't get any rewards from the Phantom, and I didn't ship the project. I did not double dip.)
<img width="1365" height="658" alt="Screenshot 2026-10-03 16 27 37" src="https://github.com/user-attachments/assets/9150a999-214e-4632-9a2a-35716261ae71" />

## Try it here:
https://bio.rayan123-4.hackclub.app/

## Features

 - Accepts DNA sequences containing A, C, G and T, while it has to contain ATG to start the protein sequence
 -  Automatically removes spaces in the sequence and converts input to uppercase
 - Automatically find the start codon (ATG)
 - Reads DNA three bases at a time as codons
 - Translates codons into amino acids
 - Stops translation at a STOP codon
 - Gives error message for invalid DNA sequences

 ## Clone the repository
 ```bash
 git clone https://github.com/rayan123-4/Flask-website-Biology
```

## Some resources I used to help me start:
 - https://www.geeksforgeeks.org/python/dna-protein-python-3/

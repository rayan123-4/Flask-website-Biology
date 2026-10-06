# Flask-website-Biology
This is  my first flask website that I have using **HTML**, **CSS**, and **Python**.
- It's a website that takes DNA and translates it into proteins.
- All you have to do it put a DNA sequence in the result box and press submit and wait for it to translate.
- This website is made for the Stardance challenge by hack club.
- (note: it used to be for Phantom, but I decided to change it for Stardance. I didn't get any rewards from the Phantom, and I didn't ship the project. I did not double dip.)
<img width="1365" height="658" alt="Screenshot 2026-10-03 16 27 37" src="https://github.com/user-attachments/assets/9150a999-214e-4632-9a2a-35716261ae71" />

## Try it here:
https://bio.rayan123-4.hackclub.app/

## Features

 - It will only accept DNA sequences that contain the letters A, C, G, and T. Also it must start with ATG.
 - It will automatically removes the spaces in the sequence and convert the input to uppercase
 - It will find the start codon (ATG)
 - It Reads DNA three bases at a time as codons
 - It translates codons into amino acids
 - It Stops translation at a STOP codon
 - It will give an error message for invalid DNA sequences

 ## Clone the repository
 ```bash
 git clone https://github.com/rayan123-4/Flask-website-Biology
```

## Some resources I used:
 - https://pixabay.com/vectors/dna-helix-circles-4043148/
 - https://www.geeksforgeeks.org/python/dna-protein-python-3/

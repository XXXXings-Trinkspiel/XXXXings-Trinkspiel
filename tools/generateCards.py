#!/usr/local/bin/python
# coding: utf-8

import gnupg
import os
import sys
import argparse
import re
import codecs

# Parse Arguments
parser = argparse.ArgumentParser(description='Decodes the PGP-encoded files and produces printable cards.')
parser.add_argument('-i','--inputfolder', help='Folder in which (only) the encoded files reside.', required=True)
parser.add_argument('--gpgfolder', help='Folder into which the gpg-config is written', default='./gpg/')
parser.add_argument('--privatekey', help='The private key for decoding', default=r"C:\Users\Sebastian Becking\tmp\Trinkspiel\gpg-secret-key.pgp")
parser.add_argument( '-n', '--name', help='The kind of generated Card-deck (Alkoholkarte/Gruppenkarte/Regelkarte). Will be printed on resulting Cards.', default='[generische Karte]')
parser.add_argument( '-o', '--output', help='The name and path of the generated output file.', default='./out.tex')
args = parser.parse_args()

# Import PGP key 
gpg = gnupg.GPG(gnupghome=args.gpgfolder)
key_data = open(args.privatekey).read()
gpg.import_keys(key_data)

# Decrypt and decode files
cards = list()
for file in os.listdir(args.inputfolder):
	print("Decrypting "+file+"...")
	try:
		encryptedString = open(args.inputfolder+'/'+file).read()
	except:
		print('Error reading File: '+args.inputfolder+'/'+file)
		
	decryptedString = gpg.decrypt(encryptedString)
	
	# Trying different encodings till one is good.)
	encodings = ['utf-8', 'latin_1', 'latin2', 'ascii', 'mac_latin2', 'cp273', 'cp850', 'cp500', 'cp858', 'cp1252', 'cp65001']
	encodings.reverse()
	
	encodingWrong = True
	while encodingWrong:
		try:
			cards.append(decryptedString.data.decode(encodings.pop()).rstrip())
			encodingWrong = False
		except:
			print('nope..')
			pass			

# Generate LaTeX File
latexHeader = r'''\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\documentclass[myown,fronts]{flashcards}
\usepackage{ngerman}
\usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}
\cardfrontstyle[\slshape]{headings}
\cardbackstyle{empty}
\setlength{\cardmargin}{1.2cm}
\begin{document}'''
latexFooter = r'''\end{document}
\endinput'''

# Helper function to  escape TeX-Literals
def tex_escape(text):
	conv = {
		'&': r'\&',
		'%': r'\%',
		'$': r'\$',
		'#': r'\#',
		'_': r'\_',
		'{': r'\{',
		'}': r'\}',
		'~': r'\textasciitilde{}',
		'^': r'\^{}',
		'\\': r'\textbackslash{}',
		'<': r'\textless',
		'>': r'\textgreater',
		'ß': r'"s',
		'ä': r'"a',
		'ü': r'"u',
		'ö': r'"o',
		'Ä': r'"A',
		'Ü': r'"U',
		'Ö': r'"O',
		'"': r"\textquotedbl ",
		'„': r"\textquotedbl ",
		'“': r"\textquotedbl ",
	}
	
	rx = re.compile('|'.join(map(re.escape, conv)))
	def one_xlat(match):
		return conv[match.group(0)]
		
	return rx.sub(one_xlat, text)

# Generate and write LaTeX-File
print("Generating and Writing LaTeX-File...")

outputfile = open(args.output, mode = 'w', encoding = 'utf-8')
outputfile.write(latexHeader)
outputfile.write('\cardfrontfoot{'+args.name+"}\n\n")

for card in cards:
	#card = codecs.encode(card, 'rot_13') # for testing purposes (looking for encoding errors or non-compiling LaTeX)
	if (len(card) <= 250):
		outputfile.write(r"\begin{flashcard}[]{"+tex_escape(card)+r"}\end{flashcard}"+"\n")
	elif (len(card) <= 350):
		outputfile.write(r"\begin{flashcard}[]{\small{"+tex_escape(card)+r"}}\end{flashcard}"+"\n")
	elif (len(card) <= 1400):
		outputfile.write(r"\begin{flashcard}[]{\tiny{"+tex_escape(card)+r"}}\end{flashcard}"+"\n")
	else:
		print("Content of card is too long! Skipped. Must manually add card. ROT13: "+codecs.encode(card, 'rot_13'))
outputfile.write(latexFooter)
outputfile.close()

print("Unused spaces on sheet: " + str(8-(len(cards)%8)))
print("Generating PDF from LaTeX-File...")
# Generating PDF
os.system("pdflatex -quiet "+args.output)
print("Done!")
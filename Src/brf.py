import argparse
import os
import sys
import bfInterpreter as bf

# input file handling

def validate_txt_file(file_path):
    if not file_path.endswith('.brf'):
        raise argparse.ArgumentTypeError("Only .brf files are allowed.")
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError("File does not exist.")
    return file_path

parser = argparse.ArgumentParser(description="Only accept a .brf file.")
parser.add_argument('input_file', type=validate_txt_file, help='Path to a .brf file')

args = parser.parse_args()

# rest is the converter

open("temp.bf", "w").close()

with open(args.input_file, "r")as file:
  with open("temp.bf", "a")as tempFile:
    tempFile.write
    keysymbols = ["+", "-", "<", ">", ".", ",", "[", "]"]
    keywords = ["rizz", "fanumtax", "aura", "sigma", "yap", "lethimcook", "goon", "edge"]
    for line in file:
      for word in line.split():
        if word in keywords:
          for i in range(len(keywords)):
            if word == keywords[i]:
              tempFile.write(keysymbols[i])
              break
        else:
          tempFile.write(word)

with open("temp.bf", "r")as file:
    bfCode = file.read()
    bf.evaluate(bfCode)
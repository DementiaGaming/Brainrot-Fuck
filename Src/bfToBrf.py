import argparse
import os
import sys

# input file handling

def validate_txt_file(file_path):
    if not file_path.endswith('.bf'):
        raise argparse.ArgumentTypeError("Only .bf files are allowed.")
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError("File does not exist.")
    return file_path

parser = argparse.ArgumentParser(description="Only accept a .bf file.")
parser.add_argument('input_file', type=validate_txt_file, help='Path to a .bf file')

args = parser.parse_args()

# rest is the converter

open("temp.brf", "w").close()

with open(args.input_file, "r")as file:
  with open("temp.brf", "a")as tempFile:
    tempFile.write
    bfkeywords = ["+", "-", "<", ">", ".", ",", "[", "]"]
    brfkeywords = ["rizz", "fanumtax", "aura", "sigma", "yap", "lethimcook", "goon", "edge"]
    for line in file:
      for word in line:
        if word in bfkeywords:
          for i in range(len(bfkeywords)):
            if word == bfkeywords[i]:
              tempFile.write(f"{brfkeywords[i]} " )
              break
        else:
          tempFile.write(word)
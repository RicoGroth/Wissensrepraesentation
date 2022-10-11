#!/usr/bin/python -tt

"""Mimic pyquick exercise"""


# Read in the file specified on the command line.
# Do a simple split() on whitespace to obtain all the words in the file.
# Rather than read the file line by line, it's easier to read
# it into one giant string and split it once.

def file_to_list(filename):
  res = []
  with open(filename) as file:
    for line in file:
      res.extend(line.split())
  return res


# Build a "mimic" dict that maps each word that appears in the file
# to a list of all the words that immediately follow that word in the file.
# The list of words can be be in any order and should include
# duplicates. So for example the key "and" might have the list
# ["then", "best", "then", "after", ...] listing
# all the words which came after "and" in the text.
# We'll say that the empty string is what comes before
# the first word in the file.

def build_mimic_dict(wordlist):
  d = {}
  for i in range(len(wordlist)):
    d[wordlist[i]] = []
    for j in range(len(wordlist[i + 1:])):
      d[wordlist[i]].extend(wordlist[j])
  return d

# With the mimic dict, it's fairly easy to emit random
# text that mimics the original. Print a word, then look
# up what words might come next and pick one at random as
# the next work.
# Use the empty string as the first word to prime things.
# If we ever get stuck with a word that is not in the dict,
# go back to the empty string to keep things moving.

# Note: the standard python module 'random' includes a
# random.choice(list) method which picks a random element
# from a non-empty list.

# For fun, feed your program to itself as input.
# Could work on getting it to put in linebreaks around 70
# columns, so the output looks better.

import random
import sys

def file_to_list(filename):
  wordlist = []
  with open(filename) as file:
    for line in file:
      wordlist.extend(line.split())
  return wordlist

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  wordlist = file_to_list(filename)
  mimic = {'': [wordlist[0]], wordlist[-1]: ['']}
  for i, word in enumerate(wordlist):
    if i < len(wordlist) - 1:
      try:
        mimic[word].append(wordlist[i + 1])
      except:
        mimic[word] = [wordlist[i + 1]]
  return mimic


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  for i in range(200):
    value_list = mimic_dict[word]
    if type(value_list) != list:
      value_list = [value_list]
    word = random.choice(value_list)
    print(word)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()

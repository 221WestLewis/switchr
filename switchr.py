import itertools
import argparse

def switcheroo(phrase,englishThreshold = 0.5):
  f = open('words.txt')
  words = []
  for line in f:
    words.append(line.strip().lower())
  dictionary = set(words)

  firstLetters = []
  wordBodies = []
  for word in phrase.split():
    firstLetters.append(word[0])
    wordBodies.append(word[1:])

  print str(len(list(itertools.permutations(firstLetters)))) + " combinations found"

  for perm in itertools.permutations(firstLetters):
    curStr = ""
    englishWords = 0.0
    for index,firstLetter in enumerate(perm):
      newWord = firstLetter + wordBodies[index]
      if newWord in dictionary:
        englishWords += 1
      curStr += newWord + " "
    if englishWords/len(perm) >= englishThreshold:
      print curStr

parser = argparse.ArgumentParser()
parser.add_argument("input",type=str,help="Input text")
parser.add_argument("threshold",type=float,help="English Threshold")
args = parser.parse_args()

switcheroo(args.input,args.threshold)

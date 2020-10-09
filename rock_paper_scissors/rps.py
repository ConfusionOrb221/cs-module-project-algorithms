#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  plays = ['rock', 'paper', 'scissors']
  result = []

  def outcomes(playsSoFar, roundsLeft):
    if roundsLeft == 0:
      result.append(playsSoFar)
    else:
      for i in range(3):
        outcomes(playsSoFar + [plays[i]], roundsLeft - 1)
  outcomes([], n)
  return result
  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
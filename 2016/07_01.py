"""advent of code 2016 day 7 part 1"""
import re


regex_repeats = re.compile(r'([a-z])\1{3,}')
regex_brackets = re.compile(r'\[[a-z ]*([a-z])([a-z])\2\1[a-z ]*\]')
regex = re.compile(r'([a-z])([a-z])\2\1')

data = open('input').read().splitlines()


data = [regex_repeats.sub('\1 \1', d) for d in data]
data = [d for d in data if len(regex_brackets.findall(d)) == 0]
data = [d for d in data if len(regex.findall(d)) > 0]
print(len(data))

"""advent of code 2016 day 7 part 2"""
import re

# check for ABA outside and BAB inside

regex_repeats = re.compile(r'([a-z])\1{2,}')
aba_before = re.compile(r'([a-z])([a-z])\1.*\[[a-z ]*\2\1\2[a-z ]*\]')
not_before = re.compile(r'\[[a-z ]*([a-z])([a-z])\1[a-z ]*\].*\[[a-z ]*\2\1\2[a-z ]*\]')
aba_after = re.compile(r'\[[a-z ]*([a-z])([a-z])\1[a-z ]*\].*\2\1\2')
not_after = re.compile(r'\[[a-z ]*([a-z])([a-z])\1[a-z ]*\].*\[[a-z ]*\2\1\2[a-z ]*\]')

data = open('input').read().splitlines()


data = [regex_repeats.sub(r'\1 \1', d) for d in data]
before = [d for d in data if len(aba_before.findall(d)) > 0
          and len(not_before.findall(d)) == 0]
after = [d for d in data if len(aba_after.findall(d)) > 0
         and len(not_after.findall(d)) == 0]
final = set(before).union(set(after))
print(len(final))

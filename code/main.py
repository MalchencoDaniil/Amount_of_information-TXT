from math import *
import codecs

text = codecs.open(r'data\text.txt', 'r', 'utf_8_sig').read().lower()
text = text.replace(' ', '')
text = text.replace('\n', '')

c = {}
for i in text:
    c[i] = c.get(i, 0) + 1

symbols = 0
for i in c:
    symbols += c[i]

all_summa  = 0

all_count = len(text)
m = {}
for i in c:
    m[i] = m.get(i, log2(1/(c[i]/ all_count)))
    all_summa += m[i]

print(len(c) * all_summa)
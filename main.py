
import multiprocessing
import re
import collections
import pickle

ignored_chars = {'$', '(', ',', '.', ':', ';', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\\', '`', '\'',
                 '+', '-', '*', '/', '<', '>', '^', '%', '=', '?', '!', '[', ']', '{', '}', '_', '\n', '"', '&', '~'}
CHUNK_SIZE = 1000


def base_forms(line):
    tokens = unicode(line, "utf-8").lower().split(", ")
    forms_map = dict()
    for el in tokens:
        forms_map[el] = tokens[0]
    return forms_map


def normalize_text(text):
    text = unicode(text, "utf-8").lower()
    for pattern in ignored_chars:
        text = re.sub(re.escape(pattern), '', text)
    return text.split()


def to_base(args):
    (word_list, base_form) = args
    counter = collections.Counter()
    for word in word_list:
        try:
            counter[base_form[word]] += 1
        except KeyError:
            counter[word] += 1
    return counter

pool = multiprocessing.Pool()

# read odm
base_form = {}
with open("lab6/odm_utf8.txt") as file:
    odm_lines = file.readlines()
base_form_maps = pool.map(base_forms, odm_lines, CHUNK_SIZE)
for dct in base_form_maps:
    base_form.update(dct)

# read potop
with open("lab6/potop.txt") as file:
    potop_lines = file.readlines()
potop_lines = pool.map(normalize_text, potop_lines, CHUNK_SIZE)
potop_counters = pool.map(to_base, zip(potop_lines, [base_form] * len(potop_lines)), CHUNK_SIZE)
potop_counter = collections.Counter()
for cnt in potop_counters:
    potop_counter = potop_counter + cnt

pickle.dump(potop_counter.items(), open("statistics", "wbx"))
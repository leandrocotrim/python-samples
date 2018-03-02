import re
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

my_regex = re.compile('[0-9]+', re.I)
lookup = defaultdict(int)
my_counter = Counter()

print('Carregou modulos...')
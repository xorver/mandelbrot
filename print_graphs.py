import pickle
import collections
import plot

# load statistics
cout_list = pickle.load(open("statistics", "rb"))
statistics = collections.Counter(dict(cout_list))
stat_sorted = statistics.most_common()

for (elem, count) in statistics.most_common():
    print(elem + u' ' + str(count))
import pickle
import collections

# load statistics
cout_list = pickle.load(open("statistics", "rb"))
statistics = collections.Counter(dict(cout_list))
stat_sorted = statistics.most_common()

# print whole list
i = 1
for (elem, count) in stat_sorted:
    print(elem + u',' + str(i) + u',' + str(count))
    i += 1

# calculate stats
forms_count = len(statistics)
all = 0
proc50 = 0
proc50_count = 0
hapax_legomena = 0
for (elem, count) in stat_sorted:
    all += count
while proc50 < all/2:
    (elem, count) = stat_sorted[proc50_count]
    proc50 += count
    proc50_count += 1
for (elem, count) in stat_sorted:
    if count == 1:
        hapax_legomena += 1

# print stats
print()
print("forms_count: " + str(forms_count))
print("all: " + str(all))
print("5o%: " + str(proc50_count))
print("hapax_legomena: " + str(hapax_legomena))

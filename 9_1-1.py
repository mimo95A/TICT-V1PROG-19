bruin= {'best', 'beukenlaan', 'helmond_houd','helmond','helmond_brouwhuis', 'deuren'}
groen={'best','beukenlaan','geeldorp','heeze', 'weert'}
def set(bruin,groen):
    s=bruin.intersection(groen)
    return  s
print(set({'best', 'beukenlaan', 'helmond_houd','helmond','helmond_brouwhuis', 'deuren'},{'best','beukenlaan','geeldorp','heeze', 'weert'}))
def set(bruin,groen):
    f = bruin.difference(groen)
    return f
print(set({'best', 'beukenlaan', 'helmond_houd','helmond','helmond_brouwhuis', 'deuren'},{'best','beukenlaan','geeldorp','heeze', 'weert'}))
def set(bruin,groen):
    m = bruin.union(groen)
    return m

print(set({'best', 'beukenlaan', 'helmond_houd','helmond','helmond_brouwhuis', 'deuren'},{'best','beukenlaan','geeldorp','heeze', 'weert'}))


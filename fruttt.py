f = open('input.txt')
#N = f.readline()
d = {}
for line in f:
    words = line.strip().split(' - ')
    en = words[0]
    lat = words[1].split(', ')
    for key in lat:
        if key in d:
            d[key].append(en)
        else:
            d[key] = [en]
f.close()

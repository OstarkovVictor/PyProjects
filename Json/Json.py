import json
import sys



first_in = (sys.stdin.readline().strip())
first_in = int(first_in)

in_data = sys.stdin.readline().strip()
offers_standart = json.loads(in_data)

for i in range(first_in - 1):
    in_data = sys.stdin.readline().strip()
    offers_to_append = json.loads(in_data)
    offers_to_append = (offers_to_append['offers'])

    for i1 in range(len(offers_to_append)):
        offer = offers_to_append[i1]

        offers_standart['offers'].append(offer)

offers_standart['offers'] = sorted(offers_standart['offers'], key=lambda k: (k['price'], k['offer_id']))

print(json.dumps(offers_standart))


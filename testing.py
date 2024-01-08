import json
from urllib.request import urlopen

with urlopen("https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON?response_type=display") as response:
    source = response.read()

data = json.loads(source)

print(type(data))

big_list = []
small_dict = {}

name_list = ["atomic_number", "symbol", "name", "atomic_mass", "hex_color", "electron_config", "electronegativity", "atomic_radius", "ionization_energy", "electron_affinity", "oxidation_states", "standard_state", "melting_point", "boiling_point", "density", "group_block", "year_discovered"]


for item in data["Table"]["Row"]:
    i = 0
    small_dict = {}
    for thing in item['Cell']:
        small_dict[name_list[i]] = thing
        i += 1
    big_list.append(small_dict)

print(big_list)
json_list = json.dumps(big_list)
print(json_list)
f = open("tester.json", "w")
f.write(json_list)



"""
version control -> get profile.
Github: tokens
Share project on github

goldbook.iupac.org
"""

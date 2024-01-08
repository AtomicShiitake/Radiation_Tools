# Author: Paul Lim
# Date: 02/27/2023
# This program is to understand how the ARMI Nuclide and Element packages work and
# the possible uses for them in future projects


from armi.nucDirectory import nuclideBases
from armi.nucDirectory import elements

# These libraries give the attributes for every listed nuclide from:
# Atomic weight, natural abundance, Atomic number(Z), Mass number, (A), Half-life, neutron yield from spontaneous fission, and decay modes


# The following function will list off the current number of elements that are defined in the framerork and the nuclides associated with each one

#import collections

#print(f"Number of elements defined in the framework: {len(elements.byZ.values())}")
#print("")
#print(f"Number of nuclides defined in the framework: {len(nuclideBases.instances)}")
#nucsByType = collections.defaultdict(list)
#for n in nuclideBases.instances:
#    nucsByType[type(n)].append(n)

#for typ, nucs in nucsByType.items():
#    print(f"   - Number of nuclides of type `{typ}`: {len(nucs)}")

# Currently at the time of trying this out there are
# 120 elements defined in the framework
# 4706 nuclides defined in the framework

# This section will be used to look up the attributes of a U-235 nuclide and print them out

# Here we define u235 and search for the specific nuclide in the nuclideBases library using the .byName function
#u235 = nuclideBases.byName['U235']

#print(u235)
# This will print out the following: <NuclideBase U235:  Z:92, A:235, S:0, W:2.350439e+02, Label:U235>, HL:2.22160758861e+16, Abund:7.204000e-03>

# For more speficic information about the nuclide we can use the other attributes of the nuclideBases library for example in terms of weight:
#print(f"Atomic Weight: {u235.weight} amu")

# The other attributes are Natural abundance, spontaneous fission neutron yield, half-life, and other ocurring nuclides 
#print(f"Natural Abundance: {u235.abundance}")
#print(f"Spontaneous Fission Neutron Yield: {u235.nuSF}")
#print(f"Half-life: {u235.halflife} seconds")
#rint("")
#print(f"Other nuclides for {elements.byZ[u235.z].name}:")
#for n in elements.byZ[u235.z].nuclides:
#    print(f"    - {n}")


# The tutorial continues with looking up the nuclide and elemental data for Li-7, but here I wanted give a look at something like Cf-252

#cf252 = nuclideBases.byName['CF252']
#print(cf252)
#print(f"Atomic Weight: {cf252.weight} amu")
#print(f"Natural Abundance: {cf252.abundance}")
#print(f"Spontaneous Fission Neutron Yield: {cf252.nuSF}")
#print(f"Half-life: {cf252.halflife} seconds")
#print("")
#print(f"Other nuclides for {elements.byZ[cf252.z].name}:")
#for n in elements.byZ[cf252.z].nuclides:
#    print(f"    - {n}")

# Here we follow exploring elemental data

# When printed it pulls the elemental data from the elements library to check from the Average Atomic weight, 
# is this element naturally occuring and is this considered a heavy metal atom
#cfElement = elements.bySymbol['CF']

#print(cfElement)
#print("")
#print(f"Average Atomic weight: {cfElement.standardWeight}")
#print(f"Is Naturally Occurring?: {cfElement.isNaturallyOccurring()}")
#print(f"Is a Heavy Metal Atom?: {cfElement.isHeavyMetal()}")


# Plotting the chart of the Nuclides
import matplotlib.pyplot as plt
from matplotlib import colors

xyc = []

for name, base in nuclideBases.byName.items():
    if not base.a:
        continue
    xyc.append((base.a-base.z, base.z, base.abundance or 0.5))
x,y,c = zip(*xyc)
plt.figure(figsize=(12,8))
plt.scatter(x,y,c=c, marker = 's', s=6)
plt.title('Chart of the nuclides')
plt.xlabel('Number of neutrons (N)')
plt.ylabel('Number of protons (Z)')
plt.show()
# Geology Research
The following is a collection of scripts used while conducting research under Dr.
Andrew Hawkins. We are trying to find the bias -- if any -- of the dissolution of
calcite and aragonite species.

week of 4/1
1. create a Nx1 matrix where each row corresponds to a collecting locality and
the value is equal to 1+number of redundant sites
redundant sites are those that have the same calcitic taxa present

2. plot Nx1 matrix

week of 4/7
iterate through all sites
if site redundant then randomly assign it a taxon (bivalve, brachipod, gastropod)

week of 4/11
count number of other sites within distance for each site/occurrence
average this value among all other occurrences
list the sites that bivalves occur
list the sites that gasts occur
list the sites that brachs occur
add up number of sites in each taxa and average the value among all three

calculate geographic distance between latitude and longitude for each site
using dummy variables first

week of 4/20
iterate tasks from 4/11 100 times

week of 4/25
Calculate distance using jaccard coefficient of two sites. distance will be measured in difference of the taxonomic
composition of two sites
for example:
brachipod and gastropod is found at site 76

week of 5/5
tweeked jaccard coefficient
created lists for distances and average values of sites in each taxa


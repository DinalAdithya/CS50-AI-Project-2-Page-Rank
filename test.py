pagerank = {}
j = 2
for i in range(10):

    pagerank.update({i: j})
    pagerank[i] = j + 1 # testing whether it works when dic key got with these []s
    j += 1
    print(pagerank.get(i))

print(pagerank)
"""
if person in have_trait:
    if gene_count[person] == 2:
        geneP = PROBS["trait"][2]

    elif gene_count[person] == 1:
        geneP = PROBS["trait"][1]
    else:
        geneP = PROBS["trait"][0]

else:
    geneP = PROBS["gene"]

if mother is not None and father is not None:  # parants listed
# mutation logic

"""
## for given motifs we can construct a count matrix (counting no. of occurence of each nucleotide in each column
## of motif matrix


Motifs = ["TCGGGGGTTTTT","CCGGTGACTTAC","ACGGGGATTTTC","TTGGGGACTTTT","AAGGGGACTTCC","TTGGGGACTTCC","TCGGGGATTCAT","TCGGGGATTCCT","TAGGGGAACTAC","TCGGGTATAACC"]
def Count(Motifs):
    count = {} # initializing the count matrix represented as dictionary
    k = len(Motifs[0]) # get the length of each motifs
# range over all nucleotides symbol and create a list of zeroes for corresponding symbol
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs) # get the number of motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
print(Count(Motifs))
print(Count(["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]))

def profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for i in profile:
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile
print (profile(Motifs))

## consensus motif finding from count motif ##
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
print (Consensus(Motifs))

def Score(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    score = 0
    consensus = Consensus(Motifs)
    for i in range (t):
        for j in range(k):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score
print (Score(Motifs))

def Entropy(Motifs):
    profiles = profile(Motifs)
    n = len(profiles["A"])
    profile_value=[]
    for j in range(n):
        for symbol in "ACGT":
            m = 0
            if profiles[symbol][j]>m:
                m = profiles[symbol][j]
                profile_value.append(m)
    import math
    results=0
    for i in range(len(profile_value)):
        results-=profile_value[i]*math.log(profile_value[i],2)
    return results


#### code given below is from comment section of course and i modified it because there mistake in profile value calculation, i.e compare the below code from above for entropy ####
##def Entropy(Motifs):
##    profiles = profile(Motifs)
##    n = len(Motifs[0])
##    profile_value=[]
##    for j in range(n):
##        m = 0
##        for symbol in "ATCG":
##            if profiles[symbol][j]>m:
##                m = profiles[symbol][j]
##        profile_value.append(m)
##    print ( profile_value)
##    import math
##    results=0
##    for i in range(n):
##        results-=profile_value[i]*math.log(profile_value[i],2)
##    return results
print (Entropy(["TCGGGGGTTTTT","CCGGTGACTTAC","ACGGGGATTTTC","TTGGGGACTTTT","AAGGGGACTTCC","TTGGGGACTTCC","TCGGGGATTCAT","TCGGGGATTCCT","TAGGGGAACTAC","TCGGGTATAACC"]))

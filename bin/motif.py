


def Count(Motifs):
    """
    Given a list of DNA motifs (strings), this script constructs a count matrix.
    The count matrix records the number of occurrences of each nucleotide (A, C, G, T)
    in each column of the motifs.
    Constructs a count matrix for a given list of motifs.

    Parameters:
        motifs (list of str): A list of DNA sequences (motifs) of equal length.

    Returns:
        dict: A dictionary with nucleotides 'A', 'C', 'G', 'T' as keys, 
              and lists representing the count of each nucleotide at each position.
    """
    
    count = {} # initializing the count matrix as a dictionary
    k = len(Motifs[0]) # length of motif (assuming all same length)

    # Initialize count lists with 0s for each nucleotide at each position
    for symbol in "ACGT":
        count[symbol] = [0]*k

    #Fill in the count matrix
    t = len(Motifs) # get the number of motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
            
    return count

#Motifs = ["TCGGGGGTTTTT","CCGGTGACTTAC","ACGGGGATTTTC","TTGGGGACTTTT","AAGGGGACTTCC","TTGGGGACTTCC","TCGGGGATTCAT","TCGGGGATTCCT","TAGGGGAACTAC","TCGGGTATAACC"]
#print(Count(Motifs))
#print(Count(["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]))

def Profile(Motifs):
    """
    Computes the profile matrix for a list of DNA motifs.
    
    The profile matrix contains the frequency (proportion) of each nucleotide (A, C, G, T)
    at every position across all motifs.
    """
    t = len(Motifs) # Number of motifs
    k = len(Motifs[0]) #Length of each motif (assumed equal)
    profile = Count(Motifs) # Get the count matrix
    
    # Convert counts to frequencies
    for i in "AGCT":
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

#print (Profile(Motifs))

# consensus motif finding from count motif
def Consensus(Motifs):
    """
    Computes the consensus string from a list of motifs.

    The consensus string is formed by selecting the most common nucleotide
    at each position across all motifs.
    """
    
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""

    
    for j in range(k):
        # Get the nucleotide with the highest count at position j
        m = 0
        frequent_symbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus

#print (Consensus(Motifs))

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
#print (Score(Motifs))

def Entropy(Motifs):
    profiles = Profile(Motifs)
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
#print (Entropy(["TCGGGGGTTTTT","CCGGTGACTTAC","ACGGGGATTTTC","TTGGGGACTTTT","AAGGGGACTTCC","TTGGGGACTTCC","TCGGGGATTCAT","TCGGGGATTCCT","TAGGGGAACTAC","TCGGGTATAACC"]))

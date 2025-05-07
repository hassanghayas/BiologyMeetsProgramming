
# for counting number pattern (i.e. motifs) in DNA fragment (i.e. genome)
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
Pattern = "CGCG"
print (PatternCount(Text, Pattern))

Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATCACCG"
Pattern = "ACCG"
print (PatternCount(Text, Pattern))

# for finding position of any pattern in genome
def PositionMatching(Text, Pattern):
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions
Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
Pattern = "CGCG"
print (PositionMatching(Text, Pattern))

Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"
count1 = PatternCount(Text, "AATTT")
count2 = PatternCount(Text, "GCG")
print (count1)
print(count2)
print (count1 + count2)


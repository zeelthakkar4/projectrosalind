s = '''CCGTTTTGGCGATTGCTACTCGTGGTAATGCTGCACCTCAACTCCCCTGCCTCTCGCTGCTACCAGATCCCCGGAACATGGGAGGAGTTGCAACTTGAGTACCTCTCCGTCAACAAATTTACAAATAGCGGTTCAACAGCGTCCAATTAAGTCACGTGTGTTGATTCGCGAAGTCAAACGGCCTGTTCTCGGGTGTCGCGATAGTATGGGCTCACCCCTCCTCAGAGCAGATGTATGGCCGTTTCTTCTGAATACCGATAACAGCCCACGTGCCGGCTTTCCTGTAGAAATCCTAACAGAGGACGGAAGTATGTCAAATCCGATGCGCTTTTATCGGCTCTGTGCACTGAAAGATCGGTGATATCGGTACGGTACAAAGAGCCCAAGTACGGGGGCCGCGCTGTGTCCCGCAACAAGCCCTCATAATCAATGGTTTAACAGTGAACCCCAAGGTCCGGGGGCCCTCTTAGGGTTCCGGGTACTCTGAGTCCCTTACGCGTGGCTACGCCATTCAGTCCTTACGTGCTCACCTACCTCTGGTGTCCGCAGAGGACCACTGATCGAGTCTAACGGCAGTGGTCCCCCTCTGAATGATGTTTTTAGAATAATCCGTAATTATACGTGACTTTTAAGACTTATACTGCCCACTATATATCAGCGGGACAAGGGGTGATTTGGGTCCTTTGAGGTCTACTCCAGCAGATGGTAGTTCGCCAGACCCAGCGGGGATCACGACGCGTCAGGCACATTGGTTTACGAGAACATGTCGTGCTAGAGTCCTGAACAGCCTGGGTTTACCACCTCTGGAGACACATAGGCTTGTCCGATAAGGATACAGCCCCCAGTTATGCATCTGCGACCACGAGCTTCTACGTTCCTGTTATTCTCCCTACCCTGGTAGTCAAACCTCATACAGTTGTCCCAAAGAGGTGCCAGTGCCA
'''

def ans(s):
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	return (str(a)+" " +str(c)+" "+str(g)+ " "+str(t))
test = ans(s)
print(test)
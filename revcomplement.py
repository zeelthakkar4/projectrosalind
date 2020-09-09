s = """CTGACGTTGGGTAAAGGAGCTATGCCTCACTAGGCTCTCTATCTGAGAACTCCGTCAATCTAAACCTCAAGCGGCAGTATAAAGTCTGTTACCCAAGGGTATCTAGCGAATAAGTGGTCAGAATGATGGCCCATCCACGATATTGGATTACCTATATACAATGGAAGTAATCATGGGCTGCGGACTATGGTTCCCGACACATTTCGCTTTATGTGGACGATGCGACGCGACGACGTCCAAGCGGTCGAGCTGAATCTGTATCCCATGCACGGCTTTTACACACACTCATCCAAAAGGCGTAAAGGCAAGACGGACACACTTCAGCTAGACACTTCAGGTATGACGATGTCGTGCCGAATACCCAAGGATATTACTTTATAAGTACGACTCGCCGCTCTCTCACTACCAGGGGCGTCCATGAGGCATAACGTATGAAGGGTAAACTCAGGCTGGGCCCGCTGGCCATAGAGATAATTCGGTGATCGGAGTAAAGGTCTTCGACTAGTCTCGCGCAGGCTACAGTGGGGTAGGCACGGACGGGCGGAACAGGCACTGCTCCCGCGCAAAGAGCAACAGACGTACCTGTAGCGCTCTGCAGATATGCTCCTTAGAAAGTGGTATTGCCATGAAGAGACAGTTGCCCCCCTTTCCTGAGGGCCTTTTGACGTACGGAGTAAACTTTAGGACAGTTATTCTAATGTTACCACTCTGCTGAATAGTCGTAAGTTCGAATAGGAGAAGGTTTAATCCTTTCGCTTAGAAAATTGATTCTCTTGTCCAATATTATCAGTGCGGGGGCGTAGATGTTTTATCAGTAATGGTATCTGTTGGG"""
def rever(str): #returns the reverse complement of a given DNA string str
	i=0 #counter
	rev = "" #reverse of DNA string
	j=0 #counter2
	comp="" #complement of DNA string
	while i<len(str): #iterates through each character of given DNA string
	 	rev=str[i:i+1]+rev #reverses the DNA string
	 	i+=1
	while j<len(str): #iterates through each character of the string
		if rev[j:j+1]=="A": #adds the complement of adenine to comp if the character of the reverse string is A
			comp+="T"
		elif rev[j:j+1]=="C": #adds the complement of cytosine to comp if the character of the reverse string is C
			comp+="G"
		elif rev[j:j+1]=="G": #adds the complement of guanine to comp if the character of the reverse string is G
			comp+="C"
		else:
			comp+="A" #adds the complement of thymine to comp if the character of the reverse string is T
		j+=1
	return comp #returns reverse complement of str
test = rever(s)
print(test)


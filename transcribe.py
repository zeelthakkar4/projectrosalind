s = "TTCCAATATAAGGAGTGGCCGGCATACTTTCGTCACTCCATGCACGAGCTCGCGCATTACTTGCAGCGCGAGATGCATAAGAGGTCGGTCCTGAGTGCTGCTGTGCAGTACAGGTTCACGCAACGCAAGACGGTCGGCAGCATGAGTGCAACTTCCGCGTGATGCATGAAGAAAAGGGACAGCGACAATATGCCCGTATTGGTGTCAAGAGTGGCTGTCGAGAGTGGTGATTAAATCAATCCATCTTCCGAGGTACGAATACACCCTCTCATTGTTAATCTCCACGGACAGTGTATCCCCGTAACCCCTTTCTCGCCTAGCCGCCCGGGTAGTAGAGACACTACAAACCGCATAATTCCAATCTAATTTTCCTGCTTTTGCTTCGGTAACGCTTTGTCAGTTATCGCTTAGGATTCTTTTGAAGCGTTATAGGACGCAATGACCGACTACGAAAGAACCCCCCTGCGCAGCACGTTCGGCAGGTCAGAGGGTCCATTCCAGTCGTGAGGAAAGTTCTATGGCTGCGCTCGGGCGTTACAACCTCAATACCGACCGCTATAATAAGTAAGTTTAACTAGAGGGTTGTCCAACTATGTTTTTGCCCATAGTCACTTTAATAGTCATCCAGATCGGTGCATCATTCATTTTTCGGGTAGAGCTGTATACCACAATACTGCATGTATACTCACGGTCATTTCTCCGCTGAACGAGGGATAAGAAGTCTAAAGACACGCACGTACACGCTTCAGGCTTCGGTTCATTAATACCCTTGCACGCCCAAGGACTATTAGGTCAACGTAGCGTTGGGCTGATCTAATTTCGGAACCCTCTGCCGCGAACTCACCTTGTCACCCTGGGGGCCCCTTAATAAACTGAACAGGGACTAGAAAAAGCGTTACGGGCCTTCTTACATGGATGCGATCATCTCAGCGG"
def transcribe(str):
	i=0
	ans=""
	while i<len(str):
		if str[i]=="T":
			ans+="U"
		else:
			ans+=str[i]
		i+=1
	return ans

test = transcribe(s)
print(test)
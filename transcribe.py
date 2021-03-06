s = """CGATGGTTGACAGCATAAGGGAGGTCCGCCTACTATGGCGTAAATAATTCATAGCGTCGCGTGTGTAGAAGGGCTCCTGTAGAAGGTCGGGGTGATCGCCTTTCTCACGTCTCGGCGCAATAACCCCTTACTTGCATCGACGCGCGTCGTAGTGAGCTAGGAATAAGCCTGGAGCACACATAGCCTTAAGCGATAGGTTTCTCCCCTGTGGTTCTTTCTTATGCCGTACGTTCGTATTACGGGATTATAGATGCGAGCCCTCAGACAAATTAGTCTCTCAGACAACCCGACGGAGCTGATCGGTCCATGTCCGCCTCAAGGCGTCTGCACCTATTAGCACGAAAATTATGCACGTGGTATCGCCATAAACTGAGCCCTTAACGCCCGAAAAAGTTGTGAAGCGGACTACACGGGAATCTAGGTCGAGGGGTGGTATTCTGCCAGGTTGGCTTGCAGCTGGCAGGAGTATTAACTTGCATTTCAAGAAATTACTTCCTAGTGAGGCGAAGGACTCTCCTCGCTTACTTATCTGGGATGATTTTAAACGGGTCGATTCTCGGGTGACCATAAATTCAAAACGAAACTTAGCTCCTCAACTGACTACGCTCATCCGTGGTATATCAGTTCAGGGTGATATGCATTAAATGATTGCCGCCTAAGTAATCGCCCAGTGTTAAGCTCGGATTTAGTACCCTCTTTTAGGCCGACCCCCTGGGATACCGGACTATCCTGTAAGTTTCTGGGGTACGATGCAACCTTCGCATACTGTCATACACACTTATCGTTACCCCTCTAAAGACACCAGCTTGGAGGTTATGTTATCCAGATGACGGTGAACATCTGAGCAGATTATTGCGAATCCGTACAGGATTGGCGTAGACCCAAGTCGACCAGAGCTGTTTGCAGGCATAACCGCCGTGACCGCAATACTTTCTGGTAAAAGTCAA
"""
def transcribe(str): #returns the transcribed RNA string of a given DNA string str
	i=0 #counter
	ans=""
	while i<len(str): #iterates through each character in DNA string
		if str[i]=="T": #converts T to U to transcribe to RNA
			ans+="U"
		else:
			ans+=str[i] #transcribes other characters to RNA
		i+=1
	return ans #returns RNA string

test = transcribe(s)
print(test)

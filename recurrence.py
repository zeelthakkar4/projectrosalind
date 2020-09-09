def rabbits(n,k): #returns the number of rabbits present after n months if each reproduction-age rabbit produces k pairs of offspring
	ans = 1 #rabbit pairs after 1 month
	if n==1 or n==2: #base case: returns rabbit pairs after 1 or 2 months
		return ans
	else: #recursive case: returns rabbit pairs if n>2 months according to the function Fn=Fn-1+Fn-2
		ans = rabbits(n-1,k) + k*rabbits(n-2,k)
		return ans

print(str(rabbits(35,2))+" pairs")

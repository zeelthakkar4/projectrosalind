def rabbits(n,k):
	ans = 1
	if n==1 or n==2:
		return ans
	else:
		ans = rabbits(n-1,k) + k*rabbits(n-2,k)
		return ans

print(str(rabbits(35,2))+" pairs")

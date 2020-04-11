class Mat:
	def __init__(self, arr, m, n):
		# there are m rows and n columns
		self.dim = (m, n)
		self.mat = []
		for i in range(m):
			temp = []
			for j in range(n):
				temp.append(arr[i*n + j])
			self.mat.append(temp)

	def __str__(self):
		for i in range(self.dim[0]):
			for j in range(self.dim[1]):
				print(self.mat[i][j], end=' ')



def fun(arr, n):
	pass

t = int(input())

for _ in range(t):
	n = int(input())
	
        # for integer input array
        arr = list(map(int, input().split()))
        
        # for string input array
        arr = input().split()
	
        ans = fun(arr, n)

        print(ans)

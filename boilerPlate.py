# def make_mat(arr, m, n):
# 	# there are m rows and n columns
# 	mat = []
# 	for i in range(m):
# 		temp = []
# 		for j in range(n):
# 			temp.append(arr[i*n + j])
# 		mat.append(temp)
# 	return mat


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

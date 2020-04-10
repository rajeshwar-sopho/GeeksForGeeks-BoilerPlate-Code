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

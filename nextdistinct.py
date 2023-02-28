def nextdistinct(y):

	nums = [] #store each digit from x

	while (y != 0):
		nums.append(y%10) #Takes the units digit of x and appends it to nums
		y = y // 10

	#Sort nums
	nums.sort()

	for i in range(1,len(nums),1):
		if (nums[i] == nums[i -1]):
			return False

	return True

num = int(input())
num = num + 1 #I am looking for the next distinct digit

distinct = nextdistinct(num)

#loop until we find a distinct number
while(distinct == False):
	num = num + 1
	distinct = nextdistinct(num)

print(num)




















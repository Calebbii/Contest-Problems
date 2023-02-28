You might be surprised to know that 2013 is the first year since 1987 with distinct digits the years 2014 ,2015 ,2016, 2017 ,2018 2019 each have distinct digits. 2012 does not have distinct digits since the digit 2 is repeated Given a year what is the next year with distinct digits
Write a function Named nextdistinct that receives one integer Y (0 ≤ Y ≤ 10000), representing the starting year and returns single integer D, which is the next year after Y with distinct digits.

## BDD
2013 is the first year since 1987 with distinct digits
Years 2014 ,2015 ,2016, 2017 ,2018 2019 each have distinct digits.
2012 does not have distinct digits since the digit 2 is repeated
Writing a function Named nextdistinct that receives one integer Y (0 ≤ Y ≤ 10000)

## Pseudocode


	y = 3445

	nums = [5,4,3]

	345%10 = 5
	345//10 =34

	34%10 = 4
	34//10 = 3

	3%10 = 3
	3//10 = 0

	nums = [3,4,4,5]



return True if y has distinct digits
return False if y does not have distinct digits

nextdistinct(1987) --> True
nextdistinct(999) --> False
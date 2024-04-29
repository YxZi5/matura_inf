#!/usr/bin/python3

def jest_wesola(num):
	num_s = str(num)
	score = 0
	first_score = 0

	if len(num_s) == 1:
		score += num**2
		first_score = score
	else:
		for i in range(0, len(num_s)):
			cyfra = num_s[i]
			score += int(cyfra)**2

		first_score = score

	if score == 1:
		return True

	while True:
		if score == first_score:
			return False
		score_s = str(score)
		score = 0

		for i in range(0, len(score_s)):
			cyfra = int(score_s[i])
			score += cyfra**2

		if score == 1:
			return True

	return False

print(jest_wesola(85))

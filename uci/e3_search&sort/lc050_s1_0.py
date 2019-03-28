__author__ = 'wangqc'

# https://leetcode.com/problems/powx-n/discuss/257455/Python-Divide-and-Conquer

def myPow(x, n):
	if n < 0: x, n = 1/x, -n
	return x * myPow(x, n-1) if n & 1 else myPow(x*x, n>>1) if n else 1
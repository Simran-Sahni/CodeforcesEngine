import time
from query import query
import random, string
from random_word import RandomWords

def test(text,queries):
	start_time = time.time()
	query(text,queries)
	end_time = time.time()
	return end_time-start_time


def testing():
	r = RandomWords()
	text = r.get_random_word()
	print("Testing using the word - " + text + "\n")
	for i in range(5,25,5):
		print(str(i) + " queries - " + str(test(text,i)) + " seconds")
	print("\n")

def tester():
	for i in range(10):
		testing()
if __name__ == '__main__':
    tester()


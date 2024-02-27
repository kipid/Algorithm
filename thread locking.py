#Thread Locking
#Avoiding the dreaded race conditions and deadlocks.
#Race condition: same resource modified by multiple threads.
#Deadlock: multiple threads waiting on the same resource.

"""
https://wiki.python.org/moin/GlobalInterpreterLock
"""

#Imports and globals
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0

#Test function
def test(count):
	global counter
	threadname = threading.current_thread().name
	logging.info(f"Starting: {threadname}")

	for x in range(count):
		logging.info(f"Count: {threadname} += {count}")

		#The global interpreter lock (GIL) in action
		# counter += 1
		# print(f"Counter: {counter}")

		#Locking
		# lock = threading.Lock()
		# lock.acquire()
		# # lock.acquire() # Deadlock - waiting on resources
		# try:
		# 	counter += 1
		# 	print(f"Counter: {counter}")
		# finally:
		# 	lock.release()

		#Locking Simplified
		lock = threading.Lock()
		with lock:
			logging.info(f"Locked: {threadname}")
			counter += 1
			logging.info(f"Counter: {counter}")
			time.sleep(2)

	logging.info(f"Completed: {threadname}")

#Main function
def main():
	logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt="%H:%M:%S", level=logging.DEBUG)
	logging.info("App Start")

	workers = 2
	with ThreadPoolExecutor(max_workers=workers) as ex:
		for x in range(workers*2):
			v = random.randrange(1,5)
			ex.submit(test, v)

	logging.info("App Finished")

if __name__ == "__main__":
	main()

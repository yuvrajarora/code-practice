# implement a job scheduler which takes in a function f and an integer n, and calls f after n

from threading import Thread 
import time

def job_scheduler():

	def delayed_execution(fs,ms):
		time.sleep(ms)
		return fs()

	def hello(name):
		print('Hello: {}'.format(name))

	job = Thread(target=delayed_execution, args = (lambda: hello('from thread'),0.4))
	job.start()

	print('Before')
	time.sleep(0.5)
	print('After')

if __name__ == '__main__':
	job_scheduler()
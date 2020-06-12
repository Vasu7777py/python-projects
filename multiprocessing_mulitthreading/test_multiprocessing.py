from multiprocessing import Process
from threading import Thread
from time import sleep

def info(name:str):
	print(name)
	for i in range(10):
		print(name, i)
		sleep(1)

def main():
	names = ["vasu", "Bindu"]
	"""
	T = []
	for name in names:
		thread = Thread(target=info, args=(name,))
		T.append(thread)
		thread.start()

	for thread in T:
		thread.join()
	
	p = []
	for name in names:
		process = Process(target = info, args = (name,))
		p.append(process)
		process.start()
	
	for process in p:
		process.join()
	"""
	for name in names:
		info(name)
	
if __name__ == "__main__":
	main()

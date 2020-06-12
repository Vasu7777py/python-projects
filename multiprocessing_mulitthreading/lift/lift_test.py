from threading import Thread
from time import sleep

Total_floors = 20

class Lift:
	Total_lifts = 4
	running = []

	def __init__(self, lift_number:int, present_floor_number:int, max_people = 25):
		self.lift_number = lift_number
		self.present_floor_number = present_floor_number
		self.max_people = max_people
		self.pick_up_requst = []

		self.speed = 1
		self.wait = 4

	def present_floor(self):
		return self.present_floor_number

	def pick_up(self):
		for floor in self.pick_up_requst:
			if floor <= Total_floors:
				self.start(floor)

	def start(self, travel_to):
		if (self.present_floor_number < travel_to):
			direction = 1
		elif (self.present_floor_number > travel_to):
			direction = -1
		else:
			direction = 0
		floor = self.present_floor()
		if (direction == 0):
			sleep(4)
			print(floor)
		else:
			for _ in range(abs(self.present_floor_number - travel_to)):
				floor += direction
				sleep(1)
				detalis = f"({floor}, {self.lift_number})\t"
				print(detalis)
			sleep(4)
		self.present_floor_number = floor
		print("\n")

def main():
	lift1 = Lift(1, 0)
	lift1.pick_up_requst = [3, 5, 1, 7, 1, 9, 0, 3]
	lift1_thread = Thread(target=lift1.pick_up)

	lift2 = Lift(2 ,4)
	lift2.pick_up_requst = [1, 5, 9, 10, 0, 4, 7]
	lift2_thread = Thread(target=lift2.pick_up)


	lift1_thread.start()
	lift2_thread.start()
	lift1_thread.join()
	lift2_thread.join()

if __name__ == "__main__":
	main()

# Base class
class Vehicle:
	def __init__(self, brand, speed):
		# your code
		self.brand = brand
		self.speed = speed
	
	def move(self):
        	# your code
		return f"Vehicle is moving at {self.speed} kmph"
	
	def __str__(self):
		# your code
		return f"Vehicle[{self.brand}] → {self.speed} kmph"

# Child classes
class Car(Vehicle):
	def __init__(self, brand, speed, doors):
		# your code — reuse Vehicle using super()!
		super().__init__(brand, speed)
		self.doors = doors
	
	def move(self):
		# override — "Car is driving at X kmph"
		return f"Car is driving at {self.speed} kmph"
	        
	def __str__(self):
                # your code
                return f"Vehicle[{self.brand}] → {self.speed} kmph | Doors : {self.doors}"	

class Bike(Vehicle):
	def __init__(self, brand, speed):
		# your code
		super().__init__(brand, speed)

	def move(self):
		# override — "Bike is riding at X kmph"
		return f"Bike is riding at {self.speed} kmph"

class Boat(Vehicle):
	def __init__(self, brand, speed):
		# your code
		super().__init__(brand, speed)
	
	def move(self):
		# override — "Boat is sailing at X kmph"
		return f"Boat is sailing a {self.speed} kmph"

class StudentRegistry:
	def __init__(self) :
		self.students = {}

	def add_student(self, id, name, score):
		if id in self.students:         # already exists?
			raise ValueError(f"❌ Error: Student {id} already exists!")       # yes → raise!
		self.students[id] = {"name" : name, "score" : score}    # no → add it
		print(f"✅ Added {name} ({id})")
		
	def get_student(self, id):
		if id not in self.students:     # doesn't exist?
			raise ValueError(f"❌ Error: Student {id} not found!")       # yes → raise!
		return self.students[id]        # no → return it
	
	def update_score(self, id, score) :
		try :
			student_details = self.get_student(id)
			self.students[id]["score"] = score
			print(f"✅ Updated {student_details['name']}'s score to {score}")
		except ValueError as e:
			print(e)
	
	def display_all(self) :
		for key, value in self.students.items() :
			print(f"{key} → {value['name']}   score: {value['score']}")

if __name__ == "__main__" :
	vehicles = [
		Car("Toyota", 120, 4),
		Bike("Yamaha", 80),
		Boat("Yamaha", 40),
	]
	for v in vehicles:
    		print(v)
    		print(v.move())

	try : 
		registry = StudentRegistry()
		registry.add_student("S001", "Alice", 85)
		registry.add_student("S002", "Bob", 72)
		registry.add_student("S001", "Carol", 90)  # ❌ duplicate ID!
		registry.get_student("S003")               # ❌ not found!
		registry.update_score("S002", 95)
		registry.display_all()
	except ValueError as e:
		print(e)

#Bug 1 — Typo in Boat.move()
#Bug 2 — get_student("S003") raises unhandled exception

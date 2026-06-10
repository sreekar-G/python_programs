
#From Day11
#for rotating etta * no.ofrooms * (actual_price - predicted price)
#for translating etta * (actual_price - predicted price)
def square_trick(base_price, no_of_rooms, price_per_room, price, learning_rate) :
        predicted_price = base_price + no_of_rooms * price_per_room
        base_price = learning_rate * (price - predicted_price)
        price_per_room = learning_rate * no_of_rooms * (price - predicted_price)
        return base_price, price_per_room


#p^ = m'r + b'
def absolute_trick(base_price, no_of_rooms, price_per_room, price, learning_rate) :
        predicted_price = base_price + no_of_rooms * price_per_room
        if (price > predicted_price) :
                price_per_room += learning_rate * no_of_rooms
                base_price += learning_rate
        else :
                price_per_room -= learning_rate * no_of_rooms
                base_price -= learning_rate
        return price_per_room, base_price


class Book:
    # attributes: book_id, title, author, is_available(default True)
    # methods: __str__()
	def __init__(self, book_id, title, author, is_available=True) :
		self.book_id = book_id
		self.title = title
		self.author = author
		self.is_available = is_available
	def __str__(self) :
		#print(f"{self.book_id} with {self.title} by {self.author}")
		availability = "✅ Available" if self.is_available else "❌ Not Available"
		return f"{self.book_id} → {self.title} by {self.author}  {availability}"


class Library:
    # attributes: name, books (dict)
    # methods:
    #   add_book(book)
    #   borrow_book(book_id, member_name)
    #   return_book(book_id)
    #   display_available()
    #   display_all()
	#def __init__(self, name, books={}) :
	def __init__(self, name):
		self.name = name
		#self.books = books
		self.books = {}

	def add_book(self, book) :
		if book.book_id in self.books.keys() :
			raise ValueError(f"❌ Error: Book {book.book_id} already exists!")
		self.books[book.book_id] = book
		print(f"✅ Added '{book.title}' ({book.book_id})")
	
	def borrow_book(self, book_id, member_name) :
		if book_id not in self.books.keys() :
			raise ValueError(f"❌ Error: Book {book_id} not found!")
		elif not self.books[book_id].is_available :
			raise ValueError(f"❌ Error: '{self.books[book_id].title}' is not available!")
		book = self.books[book_id]
		book.is_available = False
		print(f"✅ {member_name} borrowed '{book.title}'")

	def return_book(self, book_id) :
		if book_id not in self.books.keys() :
			raise ValueError(f"❌ Error: Book {book_id} not found!")
		elif self.books[book_id].is_available :
			raise ValueError(f"❌ Error: '{self.books[book_id].title}' is already available!")
		book = self.books[book_id]
		book.is_available = True
		print(f"✅ {book.title} returned successfully")

	def display_available(self) :
		print(f"Available Books:")
		for book_id, book_details in self.books.items() :
			if book_details.is_available :
				print(f"	{book_id}  → {book_details.title} by {book_details.author}")
	
	def display_all(self) :
		print(f"All Books:") 
		#for book_id, book_details in self.books.items() : 
			#availability = ""
			#if not book_details.is_available :
			#	availability = "❌ Not Available"
			#else :
			#	availability = "✅ Available"
			#print(f"book.details.book_id} → {book_details.title} by {book_details.author}  {availability})
		for id, book in self.books.items() :
			print(f"  {book}")	
if __name__ == "__main__" :
	#y^ = 2x + 3 for (x,y) > (5,15) with learning_rate = η = 0.01
	print(absolute_trick(3, 2, 5, 15, 0.01))
	print(square_trick(3, 2, 5, 15, 0.01))
	try : 
		library = Library("City Library")
		library.add_book(Book("B001", "Python Crash Course", "Eric Matthes"))
		library.add_book(Book("B002", "Clean Code", "Robert Martin"))
		library.add_book(Book("B003", "Deep Learning", "Ian Goodfellow"))
		#library.add_book(Book("B001", "Duplicate", "Someone"))  # ❌ duplicate!

		try:
			library.add_book(Book("B001", "Duplicate", "Someone"))  # ❌ duplicate!
		except ValueError as e:
        		print(e)
	
		library.borrow_book("B002", "Sreekar")
				
		#library.borrow_book("B002", "Alice")    # ❌ already borrowed!
		#library.borrow_book("B999", "Bob")      # ❌ not found!
		
		try:
			library.borrow_book("B002", "Alice")    # ❌ already borrowed!
		except ValueError as e:
			print(e)
		
		try:
			library.borrow_book("B999", "Bob")      # ❌ not found!
		except ValueError as e:
			print(e)
		
		library.return_book("B002")
		library.display_available()
		library.display_all()
	except ValueError as error: 
		print(error)

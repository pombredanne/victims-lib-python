import sys

class HelloWorldGenerator():
	
	def __init__(self):
		print("HelloWorld")
		self.str = "Hello World"
	
	def sayHello(self,string:'wow_an_annotation'):
		print(self.str)

def main():
	hwg = HelloWorldGenerator()
	hwg.sayHello()
	
if __name__ == '__main__':
	main()
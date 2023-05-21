class Device1(object):
	def __init__(self):
		self.attri = "Router1"
		print("Router1 is enabled")
		
class Device2(object):
	def __init__(self):
		self.attri2 = "Router2"
		print("Router2 is enabled")
		
class Derieved_Device(Device1,Device2):
	def __init__(self):
	
		Device1.__init__(self)
		Device2.__init__(self)
		print("Derieved")
		
	def printDevices(self):
		print(self.attri, self.attri2)
		

Xior = Derieved_Device()
Xior.printDevices()

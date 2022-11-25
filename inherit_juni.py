#testing
import logging

class DeviceRouter(object):

    def __init__(self,router_name,router_id):
        self.router_name = router_name
        self.router_id = router_id

    def display(self):
        logging.info(f"Name of router is {self.router_name} and router id of the router is {self.router_id}")
        print(self.router_name, self.router_id)

class DeviceCore(DeviceRouter):
    def Print(self):
        logging.info("Printing device core functionality")

Switch = DeviceCore("Rubrix",48328)
Switch.display()
Switch.Print()
# Driver code
Cisoc = DeviceRouter("Junos234", 1342) # An Object of Router
Cisoc.display()

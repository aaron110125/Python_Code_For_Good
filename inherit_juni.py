#testing
import logging

class DeviceSwitch:
    def __init__(self,device_model,device_id):
        self.device_model  = device_model
        self.device_id = device_id

    def device_info(self):
        print(f"Name of router model is {self.device_model} and device id is {self.device_id}")

    def device_display(self):
        print("These are the device models")

class Vxlan(object):

    def __init__(self,vxlan_name):
        self.vxlan_name = vxlan_name

    def get_vxlan_name(self):
        return self.vxlan_name

    def is_same_network(self):
        return False

class EVxlan(Vxlan):
    def is_same_network(self):
        return True

class Pointer_Image(object):
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

    def image_distance(self):
        """ Find distance from the origin """
        return (self.x**2 + self.y**2) ** 0.5

#Driver code
vxlan1 = Vxlan("1004")
print(vxlan1.get_vxlan_name(),vxlan1.is_same_network())
vxlan2 = Vxlan("1005")
print(vxlan2.get_vxlan_name(),vxlan2.is_same_network())

p1 = Pointer_Image(5,12)
print("Image distance from the origin is {} m".format(p1.image_distance()))

device1 = DeviceSwitch("Nokia","ID-3XS")
device2 = DeviceSwitch("Juniper","Junos3553")
print(device1.device_info())
print(device2.device_display())
#logging.info("Printing device core functionality")

# Adapters allow incompatible objects to be used together. 
# Following the Open-Closed principle, we can extend class behaviour without modifying the class itself. 
# If a MicroUsbCable class is initially incompatible with UsbPort, we can create a wrapper class (i.e. an Adapter), which makes 
# them compatible. In this case, a MicroToUsbAdapter makes them compatible, similar to how we use adapters in the real-world.

class UsbCable:
    def __init__(self):
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True

class UsbPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False

# UsbCables can plug directly into Usb ports
usbCable = UsbCable()
usbPort1 = UsbPort()

usbPort1.plug(usbCable)

class MicroUsbCable:
    def __init__(self) -> None:
        self.isPlugged = False
    
    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()

# MicroUsbCables can plug into Usb ports via an adapter
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)

# Source: NeetCode

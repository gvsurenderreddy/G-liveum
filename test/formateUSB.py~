import dbus
import gobject
        
   
   
   
def popen(cmd):
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
	stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	res = process.communicate()
	return process, res
	
def _filter():
        #device_obj = bus.get_object ("org.freedesktop.Hal", udi)
        #device = dbus.Interface(device_obj, "org.freedesktop.Hal.Device")

        #if device.QueryCapability("volume"):
        	#print "works!!"
	devices = hal_manager.FindDeviceByCapability('storage')
	for device in devices:
		#print device
		dev_obj = bus.get_object('org.freedesktop.Hal', device)
		d = dbus.Interface(dev_obj, 'org.freedesktop.Hal.Device')
		if d.GetProperty('storage.drive_type') != 'disk':
			continue
		if d.GetProperty('storage.bus') == 'usb' and \
            d.GetProperty('storage.removable'):
			#if d.GetProperty('block.is_volume'):
				#if d.GetProperty('volume.fstype') == 'vfat':
			print "works"
            
	            
if __name__ == '__main__':


	from dbus.mainloop.glib import DBusGMainLoop
	DBusGMainLoop(set_as_default=True)
	#bus = dbus.Bus(dbus.Bus.TYPE_SYSTEM)
	#loop = gobject.MainLoop()
	bus = dbus.SystemBus()
	hal_manager_obj = bus.get_object("org.freedesktop.Hal","/org/freedesktop/Hal/Manager")
	hal_manager = dbus.Interface(hal_manager_obj,"org.freedesktop.Hal.Manager")
	_filter()
	#hal_manager.connect_to_signal("DeviceAdded", _filter)
	#loop.run()
    
	


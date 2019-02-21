from sense_hat import SenseHat
from time import sleep
s = SenseHat()


x_values = []
z_values = []
t=1

for i in range(100):
    raw = s.get_accelerometer_raw()

    x_values.append(raw['x'])
    z_values.append(raw['z'])
    
    print(t)
    sleep(0.2)
    t=t+1


xvalue = max(x_values)-min(x_values)
zvalue = max(z_values)-min(z_values)
print('x value is ' + str(xvalue))
print('z value is ' + str(zvalue))


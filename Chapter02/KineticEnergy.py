# Clacluate Kinetic Energy

print("This program calculates th kinetic energy of a moving object.")

m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)

v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)

e = 0.5 * m * v * v

print("The object has " + str(e) + " jouls of energy.")
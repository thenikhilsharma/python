import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
if not ser.isOpen():
    ser.open()

def led_on_off():
    user_input = input("\n Type on / off / quit : ")
    if user_input =="on":
        print("LED is on...")
        time.sleep(0.1) 
        ser.write(b'H') 
        led_on_off()
    elif user_input =="off":
        print("LED is off...")
        time.sleep(0.1)
        ser.write(b'L')
        led_on_off()
    elif user_input =="quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.close()
    else:
        print("Invalid input. Type on / off / quit.")
        led_on_off()

time.sleep(2)

led_on_off()
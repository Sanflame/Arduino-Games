import serial
import serial.tools.list_ports
import pyautogui
values=serial.tools.list_ports.comports()
listserial=list()

for port in sorted(values):
    listserial.append(port.device)


ser=serial.Serial(listserial[0])
ser.baudrate=9600

while(1):
    s = int(ser.readline())
    if(s==1):
        pyautogui.press('space')

#!/usr/bin/env python3
#############################################################################
# Fichero     : Motor.py
# Description : Control Motor with L293D
# Autor       : Antonio2709
# modificacion: 12/04/2020
########################################################################
import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
# define los pines conectados a L293D 
motoRPin1 = 13
motoRPin2 = 11
enablePin = 15

def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value
    
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)  

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)   
    GPIO.setup(motoRPin1,GPIO.OUT)   # poner pines en modo output
    GPIO.setup(motoRPin2,GPIO.OUT)
    GPIO.setup(enablePin,GPIO.OUT)
        
    p = GPIO.PWM(enablePin,1000) # crear PWM y poner Frequence a 1KHz
    p.start(0)

# funcion mapNUM : asigna el valor de un rango a otro rango 
def mapNUM(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    
# funcion motor: determina la direccion y velocidad del motor en acuerdo de el valor ADC
def motor(ADC):
    value = ADC -128
    if (value > 0):  # make motor turn forward
        GPIO.output(motoRPin1,GPIO.HIGH)  # motoRPin1 salida alta nivel
        GPIO.output(motoRPin2,GPIO.LOW)   # motoRPin2 salida bajo nivel
        print ('gira a derechas...')
    elif (value < 0): # motor gira a izquierdas
        GPIO.output(motoRPin1,GPIO.LOW)
        GPIO.output(motoRPin2,GPIO.HIGH)
        print ('gira a izquierdas...')
    else :
        GPIO.output(motoRPin1,GPIO.LOW)
        GPIO.output(motoRPin2,GPIO.LOW)
        print ('Motor Parado...')
    p.start(mapNUM(abs(value),0,128,0,100))
    print ('El ciclo de trabajo PWM es %d%%\n'%(abs(value)*100/127))   # imprime valor PWM.

def loop():
    while True:
        value = analogRead(0) # leer valor ADC
        print ('ADC Value : %d'%(value))
        motor(value)
        time.sleep(1)

def destroy():
    bus.close()
    GPIO.cleanup()
    
if __name__ == '__main__':  
    print ('El programa esta arrancado ... ')
    print ('Presiona control + C para finalizar el programa')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Presiona control + C para finalizar el programa
        destroy()


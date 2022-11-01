import machine
import utime
pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)
def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Motion detected. Intruder alert!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
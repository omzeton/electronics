import machine
import utime

p1 = machine.Pin(16, machine.Pin.OUT)
p2 = machine.Pin(17, machine.Pin.OUT)
p3 = machine.Pin(18, machine.Pin.OUT)
p4 = machine.Pin(19, machine.Pin.OUT)
p5 = machine.Pin(20, machine.Pin.OUT)

led_array_1 = [
    [p1],
    [p2],
    [p3],
    [p4],
    [p5],
]
led_array_2 = [
    [p1],
    [p1, p2],
    [p2, p3],
    [p3, p4],
    [p4, p5],
    [p5],
]
led_array_3 =[
    [p1],
    [p1, p2],
    [p1, p2, p3],
    [p2, p3, p4],
    [p3, p4, p5],
    [p4, p5],
    [p5],
]
led_array_4 =[
    [p1],
    [p1, p2],
    [p1, p2, p3],
    [p1, p2, p3, p4],
    [p2, p3, p4, p5],
    [p3, p4, p5],
    [p4, p5],
    [p5],
]
led_array_5 =[
    [p1],
    [p1, p2],
    [p1, p2, p3],
    [p1, p2, p3, p4],
    [p1, p2, p3, p4, p5],
    [p2, p3, p4, p5],
    [p3, p4, p5],
    [p4, p5],
    [p5],
]
mother_array = [
    led_array_1,
    led_array_2,
    led_array_3,
    led_array_4,
    led_array_5,
    led_array_4,
    led_array_3,
    led_array_2,
]

while True:
    for array in mother_array:
        for i in range(0, 5):
            for led_pin_subarray in array:
                for led_pin in led_pin_subarray:
                    led_pin.value(1)
                utime.sleep(0.1)
                for led_pin in led_pin_subarray:
                    led_pin.value(0)  

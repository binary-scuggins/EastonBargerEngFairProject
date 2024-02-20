from machine import Pin
import time
import utime

button_pin = Pin(8, Pin.IN, Pin.PULL_DOWN)
buzzer_pin = Pin(11, Pin.OUT)
led_pin = Pin(13, Pin.OUT)
led3_pin = Pin(12, Pin.OUT)
led4_pin = Pin(16, Pin.OUT)
naruto9 = Pin(14, Pin.OUT)
sasuke9 = Pin(15, Pin.OUT)
naruto10 = Pin(13, Pin.OUT)
sasuke10 = Pin(12, Pin.OUT)
display_running = False
button_pressed = False


def play_tone(freq, duration):
    period = 1 / freq
    cycles = int(duration * freq)
    for i in range(cycles):
        buzzer_pin.value(1)
        utime.sleep(period / 2)  # Turn buzzer on for half of the period
        buzzer_pin.value(0)
        utime.sleep(period / 2)  # Turn buzzer off for half of the period

while True:
    if button_pin.value() == 1 and not button_pressed:  # Check if button is pressed
        button_pressed = True
        if not display_running:
            display_running = True
            while display_running:
                while True:
                    
                    led_pin.value(1)  # Turn LED on
                    utime.sleep(0.5)# Wait for 0.5 second
    
                    led_pin.value(0)# Turn LED off
                    led3_pin.value(1)
                    utime.sleep(1)
                    play_tone(264, 1)
    
                    led3_pin.value(0)
                    play_tone(264, 1)
                    led4_pin.value(0.5)
                    led4_pin.value(0)
                    led4_pin.value(0.5)
    
    
                    utime.sleep(1)
    
                    play_tone(264, 1)
                    play_tone(294, 2)
                    play_tone(225, 3)

                    play_tone(264, 1)
                    play_tone(294, 1)
                    play_tone(225, 1)
                    while True:
                        naruto9.value(1)
                        sasuke9.value(0)
                        print("Before sleep")
                        utime.sleep(1)
                        print("After sleep")
                        naruto10.value(1)
                        sasuke10.value(0)
                        print("Before sleep")
                        utime.sleep(1)
                        print("After sleep")
                        
                        # Reverse
                        naruto9.value(0)
                        sasuke9.value(1)
                        utime.sleep(1)
                        naruto10.value(0)
                        sasuke10.value(1)
                        utime.sleep(1)
                        
                        # Stop
                        naruto9.value(1)
                        sasuke9.value(1)
                        utime.sleep(1)
                        naruto10.value(1)
                        sasuke10.value(1)
                        utime.sleep(1)
                    
                        if button_pin.value() == 1 and button_pressed:
                            display_running = False
                            break #stops when pressed again
                    if button_pin.value() == 1 and button_pressed:
                            display_running = False
                            break #stops when pressed again
        else:
            display_running = False  # Stop the display
            button_pressed = False
    elif button_pin.value() == 0:
        button_pressed = False
        if display_running:  # Check if display is running
            display_running = False  # Stop the display
            

from microbit import * # Imports the MicroPython libraries for the micro:bit
import radio # Imports the radio module

# Configure the radio
radio.on()  # Turn on the radio
radio.config(group=23)  # Set a radio group (0-255). Only micro:bits in the same group can communicate.
radio.config(power=7) # Set the radio transmit power (0-7). Higher power equals longer range but more energy consumption.


while True:
    # Send messages
    if button_a.was_pressed():
        radio.send('hello')  # Send the string "hello" when button A is pressed.
        display.show(Image.YES) # Show a "happy" face when the message is sent.
        sleep(200) # Pause for 200 milliseconds
        display.clear() # Clear the display

    if button_b.was_pressed():
        radio.send('bye')  # Send the string "bye" when button B is pressed.
        display.show(Image.SAD) # Show a "sad" face when the message is sent.
        sleep(200) # Pause for 200 milliseconds
        display.clear() # Clear the display

    # Receive messages
    message = radio.receive()  # Check for incoming messages.

    if message is not None:  # If a message is received (not empty).
        if message == 'hello':
            display.scroll("Hello received!")  # Scroll the message if it's "hello".
            sleep(500) # Pause for 500 milliseconds
            display.clear() # Clear the display
        elif message == 'bye':
            display.scroll("Goodbye received!") # Scroll the message if it's "bye"
            sleep(500) # Pause for 500 milliseconds
            display.clear() # Clear the display
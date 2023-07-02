from XRPLib.defaults import *
from machine import Pin
import time

imu.reset_pitch()
imu.reset_yaw()
imu.reset_roll()

def log_imu_heading():
    # Set to true to log the IMU heading forever
    while True:
        print(imu.get_yaw())
        time.sleep(0.1)

def log_encoder_position():
    while True:
        print(drivetrain.left_motor.get_position(), drivetrain.right_motor.get_position())
        time.sleep(0.1)

def benchmark_encoder_isr():
    print("start benchmark")
    N = 100000
    a = time.time()
    for i in range(N):
        drivetrain.left_motor._encoder.isr()
    b = time.time()
    
    # Print benchmark
    print(f"Time for {N} calls: {b-a}s")
    print(f"Time per call: {(b-a)/N}s") # ~0.06 ms per call

def test_turns():
    drivetrain.turn(45, 0.5)
    time.sleep(1)
    drivetrain.turn(-45, 0.75)
    time.sleep(1)

    drivetrain.turn(90, 0.5)
    time.sleep(1)
    drivetrain.turn(-90, 0.75)
    time.sleep(1)


    # Turns 360 slow and fast, then turns 180 slow and fast
    drivetrain.turn(360, 0.5)
    time.sleep(1)
    drivetrain.turn(-360, 0.75)
    time.sleep(1)

def test_straight():
    drivetrain.straight(30, 0.2)

def test_set_effort():
    drivetrain.set_effort(0.3, 0.3)
    time.sleep(2)
    drivetrain.stop()

def test_led():
    led.blink(5)
    time.sleep(3)
    led.off()

def test_button():
    button.set_callback(trigger=Pin.IRQ_RISING, callback=lambda p: led.change_state())

def test_rangefinder():
    while True:
        print(f"{rangefinder.distance()}")
        time.sleep(0.25)

test_rangefinder()
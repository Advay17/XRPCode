from machine import Pin, Timer

class LED:

    """
    A very simple class for using the LED onboard the Raspberry Pi Pico
    Uses a virtual timer to allow for flexible blinking control
    Default pin on the XRP Controller is Pin 25
    """

    _DEFAULT_LED_INSTANCE = None

    @classmethod
    def get_default_led(cls):
        """
        Get the default XRP v2 LED instance. This is a singleton, so only one instance of the LED will ever exist.
        """
        if cls._DEFAULT_LED_INSTANCE is None:
            cls._DEFAULT_LED_INSTANCE = cls()
        return cls._DEFAULT_LED_INSTANCE

    def __init__(self, ledPin="LED"):
        self._led = Pin(ledPin, Pin.OUT)
        # A timer ID of -1 is a virtual timer.
        # Leaves the hardware timers for more important uses
        self._virt_timer = Timer(-1)
        self.is_blinking = False

    def blink(self, frequency: int):
        """
        Blinks the LED at a given frequency

        : param frequency: The frequency to blink the LED at (in Hz)
        : type frequency: int
        """
        if self.is_blinking:
            # disable the old timer so we can reinitialize it
            self._virt_timer.deinit()
        # We set it to twice in input frequency so that
        # the led flashes on and off frequency times per second
        self._virt_timer.init(freq=frequency*2, mode=Timer.PERIODIC,
            callback=lambda t:self.change_state())
        self.is_blinking = True

    def change_state(self):
        """
        Changes the state of the LED
        """
        self._led.toggle()

    def off(self):
        """
        Turns the LED off
        Stops the blinking timer if it is running
        """
        self.is_blinking = False
        self._led.off()
        self._virt_timer.deinit()

    def on(self):
        """
        Turns the LED on
        Stops the blinking timer if it is running
        """
        self.is_blinking = False
        self._led.on()
        self._virt_timer.deinit()
def on_forever():
    while True:
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(5000)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
basic.forever(on_forever)

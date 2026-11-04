class SmartDevice:
    def turn_on(self):
        print("Device is ON.")

    def turn_off(self):
        print("Device is OFF.")


class Light(SmartDevice):
    def turn_on(self):
        print("Light: Bulb glows, room is bright.")

    def turn_off(self):
        print("Light: Bulb switched off, room is dark.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan: Blades start rotating.")

    def turn_off(self):
        print("Fan: Blades slow down and stop.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC: Compressor starts, room begins to cool.")

    def turn_off(self):
        print("AC: Compressor stops, cooling ends.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV: Screen lights up and channels load.")

    def turn_off(self):
        print("TV: Screen goes blank, standby mode.")


devices = [Light(), Fan(), AC(), TV()]

print("--- Turning all devices ON ---")
for d in devices:
    d.turn_on()

print("\n--- Turning all devices OFF ---")
for d in devices:
    d.turn_off()

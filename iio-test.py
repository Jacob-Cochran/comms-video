import iio

### This Script is just to verify IIO can see the Pluto device ###


ctx = iio.Context("ip:192.168.2.1")  # Use Pluto's IP here

# Get a list of available devices
devices = ctx.devices

for dev in devices:
    print(f"Device found: {dev}")

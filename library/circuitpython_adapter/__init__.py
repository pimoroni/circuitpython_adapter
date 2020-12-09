class not_SMBus:
    """not_SMBus

    :param *args: Unused, only exists to prevent errors when used as a drop in for SMBus

    :param ~microcontroller.pin SCL: The pin the i2c SCL line is connected to. If not defined, defaults to board.SCL

    :param ~microcontroller.pin SDA: The pin the i2c SDA line is connected to. If not defined, defaults to board.SDA

    :param I2C: An I2C instance. If not defined, defaults to creating a new I2C instance
    """
    def __init__(self, *args, SCL=None, SDA=None, I2C=None):
        import board
        import busio

        if I2C is None:
            if SCL is None:
                SCL = board.SCL
            
            if SDA is None:
                SDA = board.SDA
            
            self.i2c = busio.I2C(SCL, SDA)
        else:
            self.i2c = I2C

    def write_i2c_block_data(self, i2c_address, register, values):
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(i2c_address, bytes([register] + values))
            
        finally:
            self.i2c.unlock()

    def read_i2c_block_data(self, i2c_address, register, bit_width):
        while not self.i2c.try_lock():
            pass
        try:
            buffer = bytearray(bit_width)
            self.i2c.writeto_then_readfrom(i2c_address, bytes([register]), buffer)
            return list(buffer)

        finally:
            self.i2c.unlock()

    def readfrom_mem(self, i2c_address, register, num_bytes):
        return self.read_i2c_block_data(i2c_address, register, num_bytes)

    def write_byte_data(self, i2c_address, register, value):
        return self.write_i2c_block_data(i2c_address, register, [value])
    
    def read_byte_data(self, i2c_address, register):
        return self.read_i2c_block_data(i2c_address, register, 1)[0]

import wiringpi2 as wiringpi

class McpHardware:
    """
    MCP Control Class
    """
    def __init__(self):
        """
        Setup ports and pins
        """
        self.wiringpi = wiringpi
        self.pinBase = 65
        self.i2cAddr = 0x20
        self.HIGH = 1
        self.LOW = 0
        self.IN = 0
        self.OUT = 1
        self.LED1 = self.pinBase 
        self.leds = [self.LED1]
        self.ROW1 = self.pinBase + 8
        self.rows = [self.ROW1]
        self.wiringpi.wiringPiSetup()
        self.wiringpi.mcp23017Setup(self.pinBase,self.i2cAddr)
        self.wiringpi.pinMode(self.LED1,self.OUT)
        self.wiringpi.pinMode(self.ROW1,self.OUT)
        print("MCP Initilized...")

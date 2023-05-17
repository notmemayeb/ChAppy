class ArduinoNotConnectedError(Exception):
	def __init__(self):
		self.message = "Arduino not found"
		super().__init__(self.message)

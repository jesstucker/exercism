class BufferFullException(Exception):
	pass

class BufferEmptyException(Exception):
	pass

class CircularBuffer(object):
	def __init__(self,buffer_size,read_position=0,write_position=0):
		self.buffer_size = buffer_size
		self.listo = [None] * buffer_size
		self.read_position = read_position
		self.write_position = write_position

	def read(self):
		if self.read_position + 1 > self.buffer_size:
			self.read_position = 0
		current = self.listo[self.read_position]
		if current == None:
			raise BufferEmptyException()

		self.listo[self.read_position] = None
		self.read_position += 1

		return current

	def write(self, element):
		if None not in self.listo:
			raise BufferFullException()
		if self.write_position + 1 > self.buffer_size:
			self.write_position = 0
		self.listo[self.write_position] = element
		self.write_position += 1

	def overwrite(self,element):
		if self.write_position + 1 > self.buffer_size:
			self.write_position = 0
		self.listo[self.write_position] = element
		self.write_position += 1
		self.read_position += 1

	def clear(self):
		self.listo = [None] * self.buffer_size
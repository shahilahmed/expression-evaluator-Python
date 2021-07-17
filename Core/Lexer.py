import copy


class Lexer:	
	
	def __init__(self,source = ""):
		self.source = copy.deepcopy(source) + '\n'
		self.pos    = 0
		
	def is_eof(self):
		return False if self.pos < len(self.source) else True
		
	def next(self):
		if not self.is_eof():
			self.pos = self.pos + 1
		else:
			self.pos = None
			
	def char(self):
		if not self.is_eof():
			return self.source[self.pos]
		else:
			return None
	
	def is_digit(self):
		if self.char() >= '0' and self.char() <= '9':
			return True
		else:
			return False
	
	def is_identifier(self):
		if self.char() >= 'A' and self.char() <= 'Z':
			return True
		elif self.char() >= 'a' and self.char() <= 'z':
			return True
		elif self.char() == '_':
			return True
		else:
			return False
	
	def is_ws(self):
		if self.char() == ' ':
			return True
		elif self.char() == '\n':
			return True
		elif self.char() == '\r':
			return True
		elif self.char() == '\t':
			return True
		else:
			return False
	
	def read_comment(self):
		self.next()
		if self.char() == '#':
			self.next()
			while self.char() != '\n':
				if self.is_eof():
					break
				self.next()
		elif self.char() == '*':
			self.next()
			while self.char() != '*':
				if self.is_eof():
					break
				self.next()
			self.next()
			if self.char() == '#':
				self.next()
	'''
	def read_string(self):
		str_data = ""
		self.next()
		while self.char() not in ["\""]:
			if self.is_eof():
				break
			if self.char() in ["\\"]:
				self.next()
				str_data = str_data + self.char()
				self.next()
			str_data = str_data + self.char()
			self.next()
		self.next()
		str_data = "\"{}\"".format(str_data)
		return str_data
	'''
	
	def read_number(self):
		str_data = ""
		while self.is_digit():
			if self.is_eof():
				break
			str_data = str_data + self.char()
			self.next()
		return int(str_data)
	
	def read_identifier(self):
		str_data = ""
		while self.is_identifier() or self.is_digit():
			if self.is_eof():
				break
			str_data = str_data + self.char()
			self.next()
		return str_data
		
	def tokenize(self):
		result = []
		while not self.is_eof():
			if self.is_ws():
				self.next()
			elif self.char() in ['#']:
				self.read_comment()
			elif self.char() in ['[','{','(',')','}',']',';',',']:
				str_data = self.char()
				result.append(str_data)
				self.next()
			elif self.char() in ['+','-','*','%','/','^','<','>','=','!','&','|']:
				str_data = self.char()
				if self.char() in ['=']:
					self.next()
					if self.char() in ['=']:
						str_data = str_data + self.char()
						self.next()
				elif self.char() in ['!']:
					self.next()
					if self.char() in ['=']:
						str_data = str_data + self.char()
						self.next()
				elif self.char() in ['<']:
					self.next()
					if self.char() in ['=']:
						str_data = str_data + self.char()
						self.next()
				elif self.char() in ['>']:
					self.next()
					if self.char() in ['=']:
						str_data = str_data + self.char()
						self.next()
				elif self.char() in ['&']:
					self.next()
					if self.char() in ['&']:
						str_data = str_data + self.char()
						self.next()
				elif self.char() in ['|']:
					self.next()
					if self.char() in ['|']:
						str_data = str_data + self.char()
						self.next()
				else:
					self.next()
				result.append(str_data)
				'''
				Shift + Tab
				Tab out ward <<<----
				elif self.char() in ["\""]:
					result.append(self.read_string())
				'''
			elif self.is_digit():
				result.append(self.read_number())
			elif self.is_identifier():
				result.append(self.read_identifier())
			else:
				raise Exception("Unknown Character: {}".format(self.char()))
		result.append('eof')
		return result

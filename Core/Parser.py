import copy


class Parser:	
	
	def __init__(self,tokens = []):
		self.tokens = copy.deepcopy(tokens)
		self.pos    = 0
		
	def is_eof(self):
		return False if self.pos < len(self.tokens) else True
		
	def token(self):
		if not self.is_eof():
			return self.tokens[self.pos]
		else:
			return None
	
	def next(self):
		if not self.is_eof():
			self.pos = self.pos + 1
		else:
			self.pos = None			

	def match(self,value = ""):
		if self.token() == value:
			self.next()
		else:
			raise Exception("Parse Error: Excepted: {} but got {}".format(value,self.token()))
	
	def error(self,where = ''):
		raise Exception("Parse Error at {}.".format(where))
	
	''' atom = number | identifier | ( exp ) '''
	def parse_atom(self):
		result = None
		token = self.token()
		if isinstance(token,int) or isinstance(token,float):
			result = token
			self.next()
		elif token == '-':
			token = self.token()
			self.match('-')
			result = [token,self.parse_atom()]
		elif token == '(':
			self.match('(')
			result = self.parse_exp()
			self.match(')')
		elif isinstance(token,str):
			result = token
			self.next()
		else:
			self.error("parse_atom Unknown Token: {}".format(token))
		return result
		
	''' term -> atom ((* | / | %) atom)* '''
	def parse_term(self):
		result = self.parse_atom()
		while self.token() in ['*','/','%']:
			token = self.token()
			self.match(token)
			result = [token,result,self.parse_atom()]
		return result
	
	''' exp -> term ((+ | -) term)* '''
	def parse_exp(self):
		result = self.parse_term()
		while self.token() in ['+','-']:
			token = self.token()
			self.match(token)
			result = [token,result,self.parse_term()]
		return result
	
	''' statement -> let identifier = exp | exp'''
	def parse_statement(self):
		result = None
		if self.token() == "let":
			self.match("let")
			token = self.token()
			if isinstance(self.token(),str):
				variable = token
				self.next()
				self.match("=")
				result = ["let",variable,self.parse_exp()]
			else:
				raise Exception("Required a identifier of type string.")
		else:
			result = self.parse_exp()
		return result
		
	def parse(self):
		result = self.parse_statement()
		self.match("eof")
		return result

import copy


class Evaluator:

	def __init__(self,env = {}):
		self.env   = {}
	
	def evaluate_exp(self,exp = []):
		result = None
		if isinstance(exp,list):
			symbol = exp[0]
			if symbol == "let":
				variable = exp[1]
				result   = self.evaluate_exp(exp[2])
				self.env[variable] = result
			elif symbol in ['+','-','*','/','%']:
				if len(exp) == 2:
					if symbol == '-':
						result = -self.evaluate_exp(exp[1])
				elif len(exp) == 3:
					result = self.evaluate_exp(exp[1])
					for arg in exp[2:]:
						if symbol == '+':
							result = result + self.evaluate_exp(arg)
						elif symbol == '-':
							result = result - self.evaluate_exp(arg)
						elif symbol == '*':
							result = result * self.evaluate_exp(arg)
						elif symbol == '/':
							result = result / self.evaluate_exp(arg)
						elif symbol == '%':
							result = result % self.evaluate_exp(arg)
		elif isinstance(exp,int) or isinstance(exp,float):
			result = exp
		elif isinstance(exp,str):
			if exp in self.env:
				result = self.env[exp]
			else:
				raise Exception("Variable: \"{}\" is not defined.".format(exp))
		else:
			return exp
		return result
	
	def evaluate(self,tree = []):
		tree = copy.deepcopy(tree)
		return self.evaluate_exp(tree)
	


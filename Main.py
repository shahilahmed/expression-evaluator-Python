from Core.Lexer     import *
from Core.Parser    import *
from Core.Evaluator import *
from datetime import datetime


NAME    = "Expression Evaluator"
VERSION = "v0.0.5"
AUTHOR  = "Md Shahil Ahmed"

def print_info():
	print()
	print("{} {} {}".format(NAME,VERSION,AUTHOR))
	print("Copyright {}".format(datetime.now().year))
	print("Type Mathematical Expression")
	print("let a = 1")
	print("a * 10")
	print()
	print()


def repl(prompt = "Eval>"):
	evaluator = Evaluator()
	while True:
		source = input(prompt)
		if source in ['exit','quit']:
			break
		try:
			tokens = Lexer(source).tokenize()
			tree   = Parser(tokens).parse()
			result = evaluator.evaluate(tree)
			if result != None:
				print(result)
		except Exception as e:
			print(e)
		print()
	print()
	print("Thanks for using.")
		

def main():
	print_info()	
	repl()
	'''
	evaluator = Evaluator()
	source = "9 * 9 * 9"
	evaluator = Evaluator()
	tokens = Lexer(source).tokenize()
	tree   = Parser(tokens).parse()
	result = evaluator.evaluate(tree)
	print()
	print(tree)
	print()
	print(result)
	'''
	
if __name__ == "__main__":
	main()



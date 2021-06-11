import ast
byte_str=b"{'one':1,'two':2}"
dict_str=byte_str.decode("UTF-8")
mydata=ast.literal_eval(dict_str)
print(repr(mydata['two']))

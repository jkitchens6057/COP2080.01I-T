# not_priv_fruit.py
class Fruit:
    def __init__(self, factor):
        self.__factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))
class Apple(Fruit): # subclass
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))
obj = Apple('red')
obj.op1() # Op1 with factor red...
obj.op2('green') # Op2 with factor green...
obj.op1() # This should be red, but isn't
print(obj.__dict__.keys())
class Form_X:
    def __init__(self, f_name):
        self._f_name = f_name
    @property
    def f_name(self):
        return self._f_name
    @f_name.setter
    def f_name(self, new_f_name):
        if not isinstance(new_f_name, str):
            raise ValueError("first name must be a string.")
        self._f_name = new_f_name
Form_X = Form_X("Sabine")
print(Form_X.f_name)
Form_X.f_name = "Hera"
print(Form_X.f_name)
Form_X.f_name = 2187


class Pycharm:
    def execute(self):
        print('compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('Spell check')
        print('Compiling')
        print('Running')

class computer:
    def code(self,ide):
        ide.execute()


ide = MyEditor() # Duck typing means calling method which is called by object
# it just find a method whatever it is
com1 = computer()
com1.code(ide)

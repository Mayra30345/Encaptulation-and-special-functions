class myClass:
    __privatevar=27

    def __privmeth(self):
        print("I am inside the class myClass")


    def hello(self):
        print("Private variable value: ",myClass.__privatevar)
foo=myClass()
foo.hello()
foo.__privMeth
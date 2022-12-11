class HelloWorld():
    def __init__(self,name='kamlesh'):
        self.name = name
    def __str__(self):
        message = "Hello " + self.name
        return self.message

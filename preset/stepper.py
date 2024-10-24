class stepper:
    def __getitem__(self, i):
        return self.data[i]
X = stepper() # X jest instancją klasy stepper
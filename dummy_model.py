from model import Model

class DummyModel(Model):
    def __init__(self, x, Y, batch_size=64):
        super().__init__()
        self.batch_size = batch_size
        self.x = x
        self.Y = Y
        self.k = 0

    def fit(self, x, Y):
        self.x = x
        self.Y = Y
        return 42

    def generate(self):
        return 42

    def evaluate(self):
        return 42

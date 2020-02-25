class Individ:
    def __init__(self, gen):
        self.gen = gen
        self.phenotype = gen - 10
        self.value = 67 + 3 * (gen - 10) - 66 * (gen - 10) ** 2 + (gen - 10) ** 3
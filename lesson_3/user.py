class User:
    def __init__(self,name, family):
        self.first_name = name
        self.last_name = family
    def name(self):
        print(self.first_name)
    def family(self):
        print(self.last_name)
    def lineage(self):
        print(f'{self.first_name} {self.last_name}')
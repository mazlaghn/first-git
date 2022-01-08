class PartyAnimal:
    x = 5

    def party(self):
        self.x = self.x + 2
        print("Sofar ", self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()
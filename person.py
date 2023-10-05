class Person:
    def __init__(self, navn, alder):
        self._navn=navn
        self._alder = alder
        self._hobbyer = []
    def legg_til_hobby(self, hobby):
        self._hobbyer.append(hobby)
    def skriv_ut_hobbyer(self):
        for hobby in self._hobbyer:
            print(hobby)
    def skriv_ut_person(self):
        print("Personen", self._navn, "er", self._alder, "gammel")
        self.skriv_ut_hobbyer()
    
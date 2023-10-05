from person import Person
navn = input("skriv et navn")
alder = int(input("skriv alder"))
person = Person(navn, alder)

svaret = input("Vil du oppgi hobbyer for personen. Hvis ja skriv <j>")
while svaret == "j":
    hobby = input("Oppgi hobbyen")
    person.legg_til_hobby(hobby)
    svaret = input("Vil du fortsette å oppgi andre hobbyer for personen. Hvis ja skriv <j>")
person.skriv_ut_person()

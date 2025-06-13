from src.Person import Person



#pers = Person.Person("gneto",40,"devops engineer")

def test_init():
    pers = Person("gneto", 40, "devops engineer")
    assert pers.name == "gneto"
    assert pers.age == 40
    assert pers.jobs == "devops engineer"


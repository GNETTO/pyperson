class Person:
    def __init__(self, name , age, jobs) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs


    @property
    def forename(self) -> str:
        return self.name.split(" ")[0]

    @property
    def surname(self) ->  str:
        return self.name.split(" ")[-1]
        #return name if name <> self.forename else None


    def celebrate_birthday(self) -> None:
        self.age += 1
        return self.age



    def add_job(self,title) -> None:
        self.jobs.append(title)


#p = Person("gneto",40,"devops engineer")

#print(p.celebrate_birthday)

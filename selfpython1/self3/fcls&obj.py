class person:
    name = "jagerna"
    job = "doctor"
    networth = 200
    def info(me):
        print(f'{me.name} is a {me.job}')
a = person()
a.name = "shrestha"
a.job = "engineer"
print(a.name, a.job)
a.info()
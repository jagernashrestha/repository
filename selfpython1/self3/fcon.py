class person:
    def __init__(me, name, job):
        print("hey i'm jagerna")
        me.name = name
        me.job = job
    def info(me):
        print(f'{me.name} is a {me.job}')
a = person("jagerna","developer")
b = person("arav", 'ha')

a.name = "shrestha"
a.job = "engineer"
print(a.name, a.job)
a.info()
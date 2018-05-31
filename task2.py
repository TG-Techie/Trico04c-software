
def examp_func(arg, times, flavor):
    for i in range(times):
        print(arg)

    if flavor:
        print("""he who wish to cross the bridge of death must andswer me these
questions three, ere the other side he C...  (++)""")


class task_list():

    
    def __init__(self):


class task():

    
    def __init__(self,func, arg_tup, priority):
        self.func = func
        self.arg_tup = arg_tup

    def perform(self):
        self.func( *self.arg_tup)




#make task list  
task_list = []

#making a task called shmurp
shmurp = task(examp_func,("hi",3,True))

#add shmurp task to task list
task_list.append(shmurp)

for i in task_list:
    i.perform()

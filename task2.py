
def examp_func(arg, times, flavor):
    for i in range(times):
        print(arg)

    if flavor:
        print("""he who wish to cross the bridge of death must andswer me these
questions three, ere the other side he C...  (++)""")

TEST_VAL = True

def test(x):
    if TEST_VAL:
        print(x)

class task_list():

    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.list3 = []
        
    def add_task(self,func, arg_tup, priority):
        if priority == 1:
            self.list1.append(task(func, arg_tup))
            print('1',self.list1)
        elif priority ==2 :
            self.list2.append(task(func, arg_tup))
            print('2',self.list2)
        else:
            self.list3.append(task(func, arg_tup))
            print('3',self.list3)

    def chug(self):
        for cur_list in (self.list1,self.list2,self.list3):
            test(cur_list)
            for i in cur_list:
                test(i.arg_tup)
                i.perform()


class task():

    
    def __init__(self,func, arg_tup):
        self.func = func
        # set arg_tup as a tup whether or not inputed as tup or not
        if type(arg_tup) == tuple:
            self.arg_tup = arg_tup
        else:
            self.arg_tup = (arg_tup,)

    def perform(self):
        self.func(*(self.arg_tup))


test('is test warking / on ?')

marp = task(print, 'must answer')
marp.perform()

blap = task_list()
blap.add_task(print,'he who wish to cross...',3)
blap.chug()'''

#make task list  
task_list = []

#making a task called shmurp
shmurp = task(examp_func,("hi",3,True))

#add shmurp task to task list
task_list.append(shmurp)

for i in task_list:
    i.perform()"""

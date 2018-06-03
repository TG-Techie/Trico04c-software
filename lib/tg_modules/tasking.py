#released under Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#
#see:https://creativecommons.org/licenses/by-nc/3.0/us/
#
#created by TG-Techie Jonah Yolles-Muprhy,
#
#version 1.0, date(us): 060118

'exapmle code:'
'''
#make a task called murp and then perform it
marp = task(print, 'must answer')
marp.perform()

#make thread_list, add an unnamed task
#(said task prints 'he who wish to cross...')
blap = thread_list()
blap.add_task(print,'he who wish to cross...',3)
blap.chug()

'''

class thread_list():

    def __init__(self, length = 3):
        self.thread_list = [[]]*(length+1)
        
    def add_task(self,func, arg_tup, priority=3):
        self.thread_list[priority].append(task(func, arg_tup))

    def chug(self):
        for cur_list in self.thread_list:
            while len(cur_list):
                cur_list[0].perform()
                cur_list.pop(0)
#            for i in cur_list:
#                i.perform()
                


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




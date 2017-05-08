# class Robot():
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def create(self):
#         print('(Initializing {})'.format(self.name))
#         print('Greetings, my master call me', self.name)
#         self.count += 1
#         print('We have {} robots.'.format(self.count))
#
#     def destroy(self):
#         print(self.name, 'is being destroyed!')
#         self.count -= 1
#         print('There is still {} robots working'.format(self.count))
#
#     def howmany(self):
#         pass
# # 实例化两个对象机器人
# r1 = Robot('R2-D2')
# r1.create()
# r2 = Robot('C-3PO')
# r2.create()
#
# print('\nRobots can do some work here.\n')
#
# print("Robots have finished their work. So let's destroy them.")
#
# r1.destroy()
# r2.destroy()

# 案例
class Robot:
    '''表示有一个带有名字的机器人'''

    # 一个类变量，用来技术机器人的数量
    population = 0

    def __init__(self, name):
        '''初始化数据'''
        self.name = name
        print('(Initializing {})'.format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        '''我挂了。'''
        print('{} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {} robots working.'.format(Robot.population))

    def say_hi(self):
        '''来自机器人的诚挚问候
        
        没问题，你做得到。'''
        print('Greetings, my masters call me {}.'.format(self.name))

    @classmethod
    def how_many(cls):
        '''打印出当前的人口数量'''
        print('We have {:d} robots'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

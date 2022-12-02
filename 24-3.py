import random


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu_memory(self):
        return self.__cpu
        return self.__memory

    @memory.setter
    def memory(self, velue):
        self.__memory = velue

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    def make_computations(self):
        return (self.memory + self.memory) / 2

    def __add__(self, other):
        return  self.memory + other.memory

    def __sub__(self, other):
        return self.memory - other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self,other):
        return self.memory > other.memory



    @classmethod
    def __str__(self):
        return f'cpu: {self.cpu}, memory:{self.memory}'


class Phone:
    def __init__(self, sim_csrd_list: list):
        self.__sim_card_list = sim_csrd_list

    @property
    def sim_csrd_list(self):
        return self.sim_csrd_list

    @sim_csrd_list.setter
    def sim_csrd_list(self, value: list):
        self.sim_csrd_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'идет вызов с номера "{call_to_number}" с сим карты {sim_card_number}'
              f'{self.__sim_csrd_list[sim_card_number]}'
        )


    @classmethod
    def __str__(self):
        return f' call: {self.sim_card_number}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list:list):
        Phone.__init__(self, sim_card_list)
        Computer.__init__(self, cpu, memory)
    @staticmethod
    def use_gps(location):
        print(f'машрут {location}, осталось{random.randint(1,20)}, km')

    @classmethod
    def __str__(self):
        return Computer.__str__(self)+''+Phone.__str__(self)

lenova = Computer(100, 10)
nokia = Phone(['Mega'])
samsung = SmartPhone(200, 30,[Mega])
iphon = SmartPhone(300,10,['O!'])

print(lenova)
print(nokia)
print(samsung)
print(iphon)

print (lenova > nokia)





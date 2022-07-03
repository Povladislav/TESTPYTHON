class Tomato:
    states = [1,2,3]
    def __init__(self,index = 0):
        self._index = index
        self._state = self.states[index]
    def grow(self):
        if self._index <= len(self.states)-1:
            self._index +=1
            self._state = self.states[self._index]
    def is_ripe(self):
        if self._index == len(self.states)-1:
            return True
        return False
class TomatoBush:
    def __init__(self,num_of_tomatos):
        self.tomatoes = []
        for i in range(num_of_tomatos):
            t = Tomato()
            self.tomatoes.append(t)
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe():
                continue
            else:
                return False
        return True
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    tomato_objects = []
    def __init__(self,name,tomato_object):
        self.name = name
        self._plant = tomato_object
        self.tomato_objects.append(self._plant)

    def work(self):
        if type(self._plant == TomatoBush):
            self._plant.grow_all()
        else:
            self._plant.grow()

    def harvest(self):
        if type(self._plant == TomatoBush):
            if self._plant.all_are_ripe():
                return True
            else:
                raise Exception("Не все томаты созрели!!!")
        else:

            for i in self.tomato_objects:
               if i.is_ripe():
                 continue
               else:
                 raise Exception("Не все томаты созрели!!!")
            return True

    @classmethod
    def knowledge_base(cls):
        print("СПРАВКА ПО САДОВОДСТВУ")

Gardener.knowledge_base()
tBush = TomatoBush(3)
gardener = Gardener('Vasya',tBush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()










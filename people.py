class character:
  def __init__(self,first,last,rank,size,health,attacking):
    self.first=first
    self.last=last
    self.rank=rank
    self.size=size
    self.health=health
    self.attack=attacking
  def __str__(self):
    return f"Name: {self.first} {self.last}\nHealth: {self.health}\nRank: {self.rank}"


class Hero(character):
  def __init__(self,first,last,rank,size,health,attacking,armor):
    character.__init__(self,first,last,rank,size,health,attacking)
    self.armor=armor #gives extra live
    #super().health+=armor

    
  def __str__(self):
    return f"{character.__str__(self)} \nArmor: {self.armor}"



class Troll(character):
  def __init__(self,first,last,rank,size,health,attacking,ability):
    super().__init__(first,last,rank,size,health,attacking)#another way to call parent class(self not inluded)
    self.ability=ability #reduces opponents live by a certain percentage

  def __str__(self):
    return f"{super().__str__()} \nAbility: {self.ability}"

class Super_Troll(Troll):
  def __init__(self,first,last,rank,size,health,attacking,armor,ability):
    Troll.__init__(self,first,last,rank,size,health,attacking,ability)
    self.armor=armor

  def __str__(self):
    return f"{super().__str__()}\nArmor: {self.armor}"

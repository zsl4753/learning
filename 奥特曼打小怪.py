from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass = ABCMeta):
    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name','_hp')
    def __init__(self,name,hp):
        self._name= name
        self._hp = hp
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @name.setter
    def name(self,name):
        self._name = name
    @hp.setter
    def hp(self,hp):
        self._hp = hp
    @abstractmethod
    def attack(self,other):
        pass

class AotMan(Fighter):
    __slots__ = ('_name','_hp','_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)#借助父类
        self._mp = mp
    def attack(self,other):
        other._hp -= randint(15,25)
    def huge_attack(self,other):
        '''
        究极必杀技
        打掉对方至少50 或者3/4血
        :param other: 
        :return: 
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp*3/4
            injury = injury if injury>= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    def magic_attack(self,others):
        '''魔法攻击'''
        if self._mp >=20:
            self._mp -= self._mp
            for temp in others:
               temp.hp -= randint(10,15)
            return True
        else:
            return False
    def resume(self):
        '''恢复魔法值'''
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point
    def __str__(self):
        return '~~~%s奥特曼~~~\n'%self._name+'生命值：%d\n'%self._hp+'魔法值：%d\n'%self._mp
class Monster(Fighter):
    __slots__ = ('_name','_hp')
    def attack(self,other):
        other.hp -= randint(10,20)
    def __str__(self):
        return '~~~%s小怪兽~~~\n'%(self._name)+'生命值：%d\n'%(self._hp)
def is_any_alive(monsters):
    '''判断有无活着的怪兽'''
    for monster in monsters:
        if monster.hp >0:
            return True
    return False

def select_alive_one(monsters):
    '''选中一只活着的小怪兽'''
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.hp >0:
            return monster
def display_info(aotman,monsters):
    '''显示怪兽和奥特曼的信息'''
    print(aotman)
    for monster in monsters:
        print(monster)

def main():
    u = AotMan('骆昊',1000,120)
    m1 = Monster('狄仁杰',250)
    m2 = Monster('白元芳',500)
    m3 = Monster('王大锤',750)
    ms = [m1,m2,m3]
    fight_round = 1
    while u.hp>0 and is_any_alive(ms):
        print('=======第%02d回合======='%(fight_round))
        m = select_alive_one(ms)
        skill = randint(1,10)#通过随机数选择使用那个技能
        if skill <= 6:#60%的概率使用普通攻击
            print('%s使用了普通攻击打了%s.'%(u.name,m.name))
            u.attack(m)
            print('%s的魔法回复了%s'%(u.name,u.resume()))
        elif skill <= 9:#30%的概率使用魔法攻击（魔法值不足失败）
            if u.magic_attack(ms):
                print('%s使用了魔法攻击'%u.name)
            else:
                print('%s使用魔法失败'%u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了究极必杀技虐了%s'%(u.name,m.name))
            else:
                print("%s使用普通攻击打了%s"%(u.name,m.name))
                print("%s的魔法值恢复了%d点"%(u.name,u.resume()))
        if m.hp>0:
            print("%s回击了%s"%(m.name,u.name))
            m.attack(u)
        display_info(u,ms)
        fight_round += 1
    print('\n************战斗结束！**********\n')
    if u.hp >0:
        print('%s奥特曼胜利'%u.name)
    else:
        print("小怪兽胜利")

if __name__ == '__main__':
    main()

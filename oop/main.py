from animals import Dog, Horse, Cat, Cow

if __name__ == '__main__':
    # Dog.speak()
    # print(Dog.legs_no)
    # print('\n')
    #
    # rex = Dog('Rex')
    # print(rex.name)
    # print(rex)
    # rex.speak()
    # print(rex.legs_no)
    #
    # print('\n')
    #
    # ben = Dog('Ben')
    # print(ben.name)
    # print(ben)
    # ben.speak()
    # print(ben.legs_no)
    #
    # # print('\n')
    # # l = [rex, ben]
    # # print(l)

    # print(Dog.legs_no)
    #
    # a = Dog('a')
    # print(a.legs_no)
    # # a.change_static_legs_no()
    # # print(a.legs_no)
    #
    # b = Dog('b')
    # print(b.legs_no)

    # a = Dog('a')
    # a._Dog__name = 'Rex'
    # print(a._Dog__name)
    # print(a)
    #
    # b = Dog('b')
    # b._Dog__name = 'Ben'
    # print(b._Dog__name)
    # print(b)

    # a = Dog('a')
    # a.__n = 'Rex'
    # print(a.__n)
    # print(a)
    #
    # b = Dog('b')
    # b.__n = 'Ben'
    # print(b.__n)
    # print(b)

    # a = Dog('a')
    # print(a.get_name())
    # a.set_name('Rex')
    # print(a.get_name())

    a = Dog('a', 'Maidanez')
    # print(a.name)
    # a.name = 'Rex'
    # print(a.name)
    # a.speak()

    # del a.name
    # print(a.name)

    my_horse = Horse('Dino', 'Pur sange arab')
    # my_horse.speak()

    cat = Cat('Julie', 'a')
    cow = Cat('Milka', 'a')

    l = [a, my_horse, cat, cow]

    for animal in l:
        animal.speak()
        print(animal.name_and_breed)

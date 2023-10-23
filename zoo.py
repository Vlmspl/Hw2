import random


class create_animal:

    def __init__(self, animal, name, canFly, canSwim):
        self.Animal = animal
        self.Name = name
        self.CanFly = canFly
        self.CanSwim = canSwim

    def move(self):
        Value = random.randint(1,2)
        if Value == 1:
            print(f"{self.Animal} {self.Name} went for a walk")
        elif Value == 2:
            if self.CanFly and not self.CanSwim:
                print(f"{self.Animal} {self.Name} went flying")
            elif self.CanSwim and not self.CanFly:
                print(f"{self.Animal} {self.Name} went swimming")
            elif self.CanSwim and self.CanFly:
                NewValue = random.randint(1,2)
                if NewValue == 1:
                    print(f"{self.Animal} {self.Name} went flying")
                if NewValue == 2:
                    print(f"{self.Animal} {self.Name} went swimming")
            else:
                print(f"{self.Animal} {self.Name} went for a walk")

    def sleep(self):
        print(f"{self.Animal} {self.Name} went sleeping")

    def live(self):
        self.move()
        self.sleep()
        self.move()
        self.sleep()


Tiger = create_animal("Tiger", "Tig", False, True)
Pigeon = create_animal("Pigeon", "Birdo", True, False)
Duck = create_animal("Duck", "Ducky", True, True)

for i in range(0, 365):
    Tiger.live()
    Pigeon.live()
    Duck.live()
    print("-------------------------------------")



#
# class Hello:
#     def __init__(self):
#         print("Hello")
#
# class HelloWorld(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
#
#
# hello_world = HelloWorld()
#
#
# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
#
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
#
# class SmartPhone(Display,Computer):
#
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)



# iphone = SmartPhone()
# iphone.print_info()
class Mother:
    def __init__(self):
        self.appearance = "heredity1"

    def gene1(self):
        print("genes1 from Mother")


class Father:
    def __init__(self):
        self.appearance2 = "heredity2"

    def gene2(self):
        print("genes2 from Father")


class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        self.appearance3 = "heredity3"

    def gene3(self):
        print("genes3 from Child")

child = Child()
print(child.appearance)
print(child.appearance2)
print(child.appearance3)

child.gene1()
child.gene2()
child.gene3()
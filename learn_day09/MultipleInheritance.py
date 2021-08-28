class Base1:

    def __init__(self):
        print("Base Class 1")

    def base_method(self):
        print("Base1 Method")


class Base2:

    def __init__(self):
        print("Base Class 2")

    def base_method(self):
        print("Base2 Method")


class ChildClass(Base2, Base1):

    def __init__(self):
        print("Child CLass Constructor")
        super().__init__()

    def test_method(self):
        super().base_method()


cc = ChildClass()
cc.base_method()
cc.test_method()
print(isinstance(cc, Base1))
print(isinstance(cc, Base2))
print(isinstance(cc, ChildClass))
print(isinstance(cc, object))


print(issubclass(ChildClass, Base1))
print(issubclass(ChildClass, Base2))
print(issubclass(ChildClass, object))

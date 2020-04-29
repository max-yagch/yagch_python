class Dog:
    """
        表示狗的类
    """

    def __init__(self, name, age, gender, height):
        self.hidden_name = name
        self.hidden_age = age
        self.hidden_gender = gender
        self.hidden_height = height

    def jiao(self):
        """
            狗的叫法
        """
        print("汪汪汪~~~~~")

    def yao(self):
        """
            狗咬的方法
        """
        print("我咬你~~~~")

    def run(self):
        """
            狗跑的方法
        """
        print("{name} 快乐的奔跑着~~~~".format(name=self.name))


d = Dog("小黄", 8, "male", 30)

d.run()
print(d.age)
help(d.run)

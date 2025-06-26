print("hello world")

def greet():
    print("こんにちは")
greet()

def print_name(name):
    print(f"私の名前は{name}です")
name = input("名前は？")

print_name(name)


def get_greet():
    return "おはようございます"

print(get_greet())


def add(a, b):
    return a + b
a = int(input("最初の数字: "))
b = int(input("2番目の数字: "))

print("合計は{}です".format(add(a, b)))
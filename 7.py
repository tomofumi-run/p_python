class User:
  count = 0
  say = "Hello? こんにちは？"
  def __init__(self,name): # コンストラクター
    User.count += 1
    self.name = name

  def say_hi(self): #インスタンスメソッド（関数）
    print("hi {0}".format(self.name))

  def introduce(self):
    print("こんにちは、私の名前は{0}です".format(self.name))

  @classmethod # クラスメソッドとして表示させる
  def show_info(cls): # クラスメソッド
    print("{0} instances".format(cls.count))

  @classmethod
  def greet(cls):
    print("さぁ、言ってみよう\n{0}".format(cls.say))

user1 = User("Tom")
user2 = User("Bob")

user1.say_hi()
user1.introduce()
User.show_info()
User.greet()

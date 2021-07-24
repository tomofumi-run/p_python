# User -> AdminUser
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

class AdminUser(User):
  def __init__(self,name,action):
    super().__init__(name) # スーパークラスを継承
    self.action = action

  def technique(self):
    print("{0}の{1}攻撃炸裂ー！！！".format(self.name,self.action))

  def say_hi(self): #override
    print("[admin]hi {0}".format(self.name))


bob = AdminUser("bob","頭突き")
bob.say_hi()
bob.greet()
bob.technique()
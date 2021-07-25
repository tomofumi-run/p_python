class A:
  def say_a(self):
    print("私はAなり。")
  def say_Hi(self):
    print("Aです")

class B:
  def say_b(self):
    print("私はBです。")
  def say_Hi(self):
    print("Bです")

class C(A,B):
  pass


c = C()
c.say_a()
c.say_b()
c.say_Hi()
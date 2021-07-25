import mypackage.user as user
# from user import AdminUser //AdminUserだけ読み込みたい

bob = user.AdminUser("bob", "頭突き")
# bob = AdminUser("bob","頭突き")
bob.say_hi()
bob.greet()
bob.technique()
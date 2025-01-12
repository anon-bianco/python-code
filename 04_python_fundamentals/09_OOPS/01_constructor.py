class BankAccount:

  def __init__(self, name, acc_no, balance):
    self.customer_name = name
    self.account_no = acc_no
    self.balance = balance

anon = BankAccount("Anon Bianco", 9489589584, 25.36)

print(anon.customer_name, anon.account_no, anon.balance)

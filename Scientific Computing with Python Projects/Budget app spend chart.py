class Category:
  #The __init__ method initializes the name, total, spent, and ledger attributes for the class.
  def __init__(self, name):
    self.name = name
    self.total = 0.0
    self.spent = 0.0
    self.ledger = []

  #The __repr__ method returns a string representation of the class.
  def __repr__(self):
    num_ast = (30 - len(self.name)) // 2
    result = ""
    for i in range(num_ast):
      result += "*"
    result += self.name
    for i in range(num_ast):
      result += "*"
    result += "\n"

    for t in self.ledger:
      end = len(str(t["description"]))
      if end > 23:
        end = 23
      result += t["description"][0:end]
      amount = "{:.2f}".format(t["amount"])
      num_space = 7-len(str(amount)) + 23 - len(t["description"][0:end])
      
      for i in range(num_space):
        result += " "
        
      result += str(amount) + "\n"
      
    bal = "{:.2f}".format(self.get_balance())
    result += f"Total: {bal}"
    return result

  #The deposit method adds an amount to the total and appends a dictionary containing the amount and description to the ledger.
  def deposit (self, money, description=""):
    self.total += money
    self.ledger.append({"amount":money, "description":description})
  
  #The withdraw method subtracts an amount from the total and spent attributes and appends a dictionary containing the amount 
  #and description to the ledger.
  def withdraw(self, cost, description=""):
    check = self.check_funds(cost)
    if check:
      self.total -= cost
      self.spent += cost
      self.ledger.append({"amount":cost*(- 1), "description":description})
    return check

  #The get_balance method returns the value of the total attribute.
  def get_balance(self):
    return self.total

  #The transfer method transfers an amount from one Category instance to another and appends dictionaries containing the amount and
  # description to the ledger of both instances.
  def transfer(self, amount, instance):
    check = self.check_funds(amount)
    if check:
      description_t = "Transfer to " + instance.name
      self.withdraw(amount, description_t)
      description_d = "Transfer from " + self.name
      instance.deposit(amount, description_d)
    return check
  #The check_funds method checks if there are enough funds to make a withdrawal and returns a Boolean value.
  def check_funds(self, amount):
    if amount > self.total:
      return False
    return True

#The create_spend_chart method creates a spend chart based on the percentage of total spending for each category.
def create_spend_chart(categories):
    total = 0
    final = "Percentage spent by category\n"
    for i in categories:
        total += i.spent
    final += f"100|          \n"
    for i in range(90,-10,-10):
        if i == 0:
            final += " "
        final += f" {i}|"
        for j in categories:
            if round(j.spent / 10)*10/total * 100 >= i:
                final += " o "
            else:
                final += "   "
        final += " \n"
    final += "    " + "-" * ((len(categories) * 3) + 1)
    fails = greatest = 0
    for i in categories:
        if len(i.name) > greatest:
            greatest = len(i.name)
    for j in range(greatest):
        fails = 0
        final += "\n     "
        for i in categories:
            try:
                if fails > 0:
                    final += "   "
                final += i.name[j] + "  "
            except:
                fails += 1
    return final

class Category:
    def __init__(self, name):
        self.name = name.title()
        self.ledger = []
    
    def get_balance(self):
        self.sum = 0
        for object in self.ledger:
            self.sum += object["amount"]
        return self.sum
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            amount = 0 - amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        return False    

    def transfer(self, amount, instance):
        if self.check_funds(amount):
            self.ledger.append({"amount":0-amount, "description":"Transfer to {}".format(instance.name)})
            instance.ledger.append({"amount":amount, "description":"Transfer from {}".format(self.name)})
            return True
        return False
    
    def __str__(self):
        # length = len(self.name)
        header = f"{self.name.center(30,'*')}"
        for i in range(len(self.ledger)):
            float_amount = '%.2f'%float(self.ledger[i]["amount"])
            string = f"{self.ledger[i]['description'][:23].ljust(23)}{float_amount.rjust(7)}"
            header = header+"\n"+string
            float_balance = '%.2f'%float(self.get_balance())
        return header + f"\nTotal: {float_balance}"
    

def create_spend_chart(categories):
    # length = len(categories)
    # column = 5 + length + length * 2
    word_len = 0
    total_spend = 0
    each_spend_arr = []
    for item in categories:
        each_spend = 0
        if len(item.name) > word_len:
            word_len = len(item.name)
        for object in item.ledger:
            if object["amount"] < 0:
                each_spend += (object["amount"] * (-1))
        total_spend += each_spend
        each_spend_arr.append(each_spend)    
    percentages = []
    for amount in each_spend_arr:
        percent = amount / (total_spend/100)
        percentages.append(percent)
    ####bar chart
    dec = 100      
    s1 = ""  
    for rw in range(11):
        s1 += f"{dec}| ".rjust(5," ")
        for col in range(len(percentages)):
            if percentages[col] >= dec:
                s1 += "o  "
            else:
                s1 += "   "
        s1 += "\n"
        dec -= 10
    ##draw underline
    column = (3 * len(percentages)) + 1
    s1 += "    "+("-"*column)

    ##may god help
    arr = ""
    index = 0
    while index < word_len :
        for j in range(len(categories)):
            try:
                arr += f"{categories[j].name[index]}  "
            except:
                arr += f"   "
        if index < word_len-1:
            arr += "\n     "
        index += 1

    return ("Percentage spent by category\n"+s1+"\n     "+arr)
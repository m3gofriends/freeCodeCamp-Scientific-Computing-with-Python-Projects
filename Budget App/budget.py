class Category:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.withdraw_total = 0
        self.ledger = []

    def __str__(self):
        string = ""
        string += (30-len(self.name))//2 * '*' + self.name+(30-len(self.name))//2 * '*' + '\n'
        for i in range(len(self.ledger)):
            description_length = len(self.ledger[i]['description'])
            float_money = "{:.2f}".format(self.ledger[i]['amount'])
            if(description_length > 23):
                string += self.ledger[i]['description'][:23] + ((30 - 23 - len(str(float_money))) * " ") + str(float_money) + '\n'
            else:
                string += self.ledger[i]['description'] + ((30 - description_length - len(str(float_money))) * " ") + str(float_money) + '\n'
        string += "Total: " + str(self.get_balance())    
        return string

    def deposit(self, deposit_money, deposit_description = ""):
        self.ledger.append({"amount": deposit_money, "description": deposit_description})
        self.money = self.money + deposit_money
        self.deposit_description = deposit_description

    def withdraw(self, withdraw_money, withdraw_description = ""):
        if(self.money < withdraw_money):
            return False
        self.ledger.append({"amount": -withdraw_money, "description": withdraw_description})
        self.money = self.money - withdraw_money
        self.withdraw_description = withdraw_description
        self.withdraw_total += withdraw_money
        return True

    def get_balance(self):
        return self.money

    def transfer(self, transfer_money, transfer_name):
        if(self.money < transfer_money):
            return False
        self.withdraw(transfer_money, "Transfer to " + transfer_name.name)
        transfer_name.deposit(transfer_money, "Transfer from " + self.name)
        return True

    def check_funds(self, check_funds_money):
        if(check_funds_money > self.money):
            return False
        return True

def create_spend_chart(class_list):
    withdraw_sum = 0
    class_name_maxlen = 0
    withdraw_percentage = []
    string = ""
    
    for class_name in class_list:
        withdraw_sum += class_name.withdraw_total
        class_name_maxlen = max(len(class_name.name), class_name_maxlen)
    for class_name in class_list:
        withdraw_percentage.append([class_name.name, int(class_name.withdraw_total*10/withdraw_sum)*10])

    string += "Percentage spent by category\n"

    now_percentage = 100
    for i in range(11):
        string += (3 - len(str(now_percentage))) * " " + str(now_percentage) + "| "
        for name, percentage in withdraw_percentage:
            if(percentage >= now_percentage):
                string += "o  "
            else:
                string += "   "
        now_percentage -= 10
        string += "\n"

    string += "    -" + (len(withdraw_percentage) * "---") + "\n"
    
    for name_len in range(class_name_maxlen):
        string += "     "
        for class_name in class_list:
            if(name_len < len(class_name.name)):
                string += class_name.name[name_len] + "  "
            else:
                string += "   "
        if(name_len == class_name_maxlen-1):
          break
        string += "\n"
        
    return string
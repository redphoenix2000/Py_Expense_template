from PyInquirer import prompt
import csv
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"spenders",
        "message":"People involved in the expense - Spenders: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    with open('expense_report.csv', 'a', newline = '') as ef:
        mywriter = csv.writer(ef, delimiter = ',')
        line = []
        for key,value  in infos.items():
            if key == "spender":
                b = check_user(value)
            if key == "spenders" and value != "":
                line.append("|")
                line.append(value)
            if key != "spenders":
                line.append(value)
        if b:
            mywriter.writerow(line)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
            print("Expense Added !")
            return True
    print("Expense not added !")
    return False

def check_user(name):
    b = False
    with open('users.csv', 'r', newline = '') as uf:
        reader = csv.reader(uf)
        data = list(reader)
        for i in data:
            n = [name]
            if i == n:
                b = True
    return b



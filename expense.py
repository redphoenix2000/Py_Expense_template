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
            #call user verification if on spender key
            if key == "spender":
                b = check_user(value)
            #add spenders with a delimiter to my new expense details if they exist
            if key == "spenders" and value != "":
                line.append("|")
                line.append(value)
            #add value if not on spenders key
            if key != "spenders":
                line.append(value)
        if b:
            mywriter.writerow(line)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
            print("Expense Added !")
            return True
    print("Expense not added !")
    return False


#check if the spender is a user
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



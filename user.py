from PyInquirer import prompt
import csv

user_questions = [
        {
            "type":"input",
            "name":"name",
            "message":"New User - Name: ",
        },
]

def add_user(*args):
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline = '') as uf:
        mywriter = csv.writer(uf, delimiter = ',')
        line = []
        for key,value in infos.items():
            line.append(value)
        mywriter.writerow(line)
    print("User Added !")
    return True

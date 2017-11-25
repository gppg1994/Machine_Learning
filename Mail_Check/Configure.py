import csv


class Configure:
    def check(self):
        try:
            fp = open('config.txt', 'r')
            flag = 1
        except Exception as e:
            flag = -1
        return flag

    def create(self):
        try:
            fp = open('config.txt', 'w')
            flag = 1
            fp.close()
        except Exception as e:
            flag = -1
        return flag

    def configure(self):
        try:
            fp = open('config.txt', 'a')
            username = input('Enter username: ')
            password = input('Enter password: ')
            fp.write(username + ',' + password + '\n')
            fp.close()
            flag = 1
        except Exception as e:
            flag = -1
        return flag

    def read(self):
        try:
            accounts = []
            with open('config.txt', 'r') as csvfile:
                rows = csv.reader(csvfile)
                for row in rows:
                    accounts.append(row)

        except Exception as e:
            flag = -1
        return accounts

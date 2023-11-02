account_database = []


def create_account(num, type, name, init_balance):
    """
    This function was created to create a new account information as
    a dictionary if the account has never been in the database before.
    """
    index = search_account_db(num)
    if index == -1:
        account = {}
        account["account_number"] = num
        account["type"] = type
        account["account_name"] = name
        account["balance"] = init_balance
        account_database.append(account)
    else:
        print("Account", num, "already exists")


def delete_account(num):
    """
    Delete the account with the given number from database.
    """
    index = search_account_db(num)
    if index != -1:
        print("Deleting account:", account_database[index]["account_number"])
        del account_database[index]
    else:
        print(num, "invalid account number; nothing to be deleted.")


def search_account_db(num):
    """
    Finding account number if the account exist it will return the index
    if not it will return -1.
    """
    for i in range(len(account_database)):
        if account_database[i]["account_number"] == num:
            return i
    return -1


def deposit(account_num, amount):
    """
    Depositing the money from the specified account,
    if the account doesn't exist it will not perform anything.
    """
    index = search_account_db(account_num)
    if index != -1:
        print("Depositing", amount, "to", account_database[index]["account_number"])
        account_database[index]["balance"] += amount
    else:
        print(account_num, "invalid account number; no deposit action performed.")


def withdraw(account_num, amount):
    """
    Withdrawing money from the specified account,
    if the account doesn't exist it will not perform anything.
    """
    index = search_account_db(account_num)
    if index != -1:
        if account_database[index]["balance"] >= amount:
            print("Withdrawing", amount, "from", account_database[index]["account_number"])
            account_database[index]["balance"] -= amount
        else:
            print("withdrawal amount", amount, "exceeds the balance of", account_database[index]["balance"],
                  "for", account_num, "account.")
    else:
        print(account_num, "invalid account number; no withdrawal action performed.")


def show_account(account_num):
    """
    Show the information of the specified account number.
    """
    index = search_account_db(account_num)
    if index != -1:
        print("Showing details for", account_database[index]["account_number"])
        print(account_database[index])
    else:
        print(account_num, "invalid account number; nothing to be shown for.")


create_account("0000", "saving", "David Patterson", 1000)
create_account("0001", "checking", "John Hennessy", 2000)
create_account("0003", "saving", "Mark Hill", 3000)
create_account("0004", "saving", "David Wood", 4000)
create_account("0004", "saving", "David Wood", 4000)
print(account_database)
show_account('0003')
deposit('0003', 50)
show_account('0003')
withdraw('0003', 25)
show_account('0003')
delete_account('0003')
show_account('0003')
deposit('0003', 50)
withdraw('0001', 6000)

import json

from my_app.models import Customer, Account, Work

with open("data_r.json", "r") as file:
    data = json.load(file)

for i in data:
    customers=Customer(name=i['name'], phone=i['phone'], email=i['email'])
    works=Work.objects.create(address=i['address'], city=i['city'], company=i['company'], postalZip=i['postalZip'], customer=customers)
    accounts=Account.objects.create(pin=i['pin'], acc_num=i['acc_num'], pan=i['pan'], cvv=i['cvv'], customer=customers)










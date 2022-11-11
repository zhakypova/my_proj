from django.db.models import Q, Subquery
from my_app.models import Account,Customer,Work

customers_email = Customer.objects.filter(email__iendswith='icloud.com')
customers_ltd = Customer.objects.filter(work__id__in=Subquery(Work.objects.filter(company__icontains='Ltd').values('id')))
account_email = Account.objects.filter(
    customer__id__in=Subquery(Customer.objects.filter(email__icontains='protonmail').values('id'))
)


print('')
print(customers_email)
print(customers_ltd)
print(account_email)







from django import template
from app.models import Customer,Account,Transaction,AccountType
register = template.Library()

@register.filter(name='get_customer_name')
def get_customer_name(customer_account):
    account=Account.get_account_by_account_number(customer_account)
    customer=account.customer_id
    customer_name=customer.first_name+' '+customer.last_name
    return customer_name

@register.filter(name='get_account_type')
def get_account_type(customer_account):
    account_type=AccountType.get_type_by_name(customer_account.account_type)
    return account_type

@register.filter(name='to_star')
def to_star(account):
    acc=list(account.account_number)
    n=len(acc)
    for i in range(4,n-3):
        acc[i]='*'
    acc = ''.join([str(elem) for elem in acc])
    return acc

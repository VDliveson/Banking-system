from django import template
from app.models import Customer,Account,Transaction
register = template.Library()

@register.filter(name='get_customer_name')
def get_customer_name(customer_account):
    account=Account.get_account_by_account_number(customer_account)
    customer=account.customer_id
    customer_name=customer.first_name+' '+customer.last_name
    return customer_name

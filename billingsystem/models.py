from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Taxi(models.Model):
    taxi_id = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return str(self.taxi_id)



class Bill(models.Model):
    bill_id = models.IntegerField(max_length=70,unique=True,primary_key=True)
    taxi = models.ForeignKey(Taxi)
    user = models.ForeignKey(User)
    total_credit_card = models.IntegerField(default=0)
    total_cash = models.IntegerField(default=0)
    bill_type = models.CharField(max_length=1)
    billed_date = models.DateTimeField('date billed')
    paid_date = models.DateTimeField('date paid',null=True)
    paid = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.bill_id)

    def not_paid(self):
        return not paid

    def total_price(self):
        return total_credit_card + total_cash

    def pay(self):
        paid = True
        paid_date = datetime.now()

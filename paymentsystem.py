# Parent class
class Payment:
    def pay(self):
        print("Payment method")

# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")

# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

# Creating objects
p = Payment()
g = GooglePay()
ph = PhonePe()
c = CreditCard()

# Calling pay() method
p.pay()
g.pay()
ph.pay()
c.pay()

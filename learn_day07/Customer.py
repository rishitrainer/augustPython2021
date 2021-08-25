class Customer:

    def __init__(self, customerId=9999, name="Name", address="Address"):
        print("Customers Constructor")
        self.name = name
        self.address = address
        self.custId = customerId


    def offerDiscount(self, discount=0):
        if discount > 0:
            print(self.name, " has discount %", discount)
        else:
            print(self.name, "has no discount")



# object creation
# objectName = ClassName()
# instanceName = Constructor() --> __init__
custOne = Customer(name="Rishi", address="Some Address", customerId=10001)
custTwo = Customer()

custTwo.custId = "10002"
custTwo.name = "Byron"
custTwo.address = "0121 Cumberland Pwkry"
print(custTwo.custId, custTwo.name, custTwo.address)
print(custOne.custId, custOne.name, custOne.address)
custOne.offerDiscount(5)
print(type(custOne.offerDiscount))
custThree = custOne

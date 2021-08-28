class Customer:

    def __init__(self, firstName, custId):
        self.first_name = firstName
        self.customer_id = custId
        print("Customer", self.customer_id, self.first_name)


    def validate(self):
        if str(self.customer_id).isdigit():
            print("Customer ID Is Valid")
        else:
            print("Invalid Customer ID")


class Validator:

    def __init__(self, value):
        self.value = value
        print("Validator Class")


    def validate(self):
        if str(self.value).isalpha():
            print("Valid Value Provided")
        else:
            print("Invalid Value Provided")


class PreferredCustomer(Customer, Validator):

    def __init__(self, firstName, custId):
        Customer.__init__(self, firstName, custId)
        Validator.__init__(self, firstName)
        print("Preferred Customer Constructor")


    def validate(self):
        print("Validate method from Preferred Customer")
        Customer.validate(self)
        Validator.validate(self)

pCust = PreferredCustomer("David", 100)
pCust.validate()
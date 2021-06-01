# Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge. Derive customer class form scheme and include cust_id, name and mobile_no data.Define necessary functions to read and display data.

class scheme:
    def scheme_id(self, id):
        print("Scheme id is", id)

    def scheme_name(self, name):
        print("Scheme name is:", name)

    def outgoing_rate(self, rate):
        print("Outgoing rate is:", rate)

    def message_charge(self, charge):
        print("Message charges are:", charge)


class customer(scheme):
    def cust_id(self, id):
        print("Customer id is", id)

    def name(self, name):
        print("Name is", name)

    def mobile_no(self, mobileno):
        print("Mobile no. is", mobileno)


detail = customer()
detail.cust_id(7)
detail.name("Devanshi Jani")
detail.mobile_no(9999999999)
detail.scheme_id(300)
detail.scheme_name("buy one get one free")
detail.outgoing_rate(400)
detail.message_charge(2)

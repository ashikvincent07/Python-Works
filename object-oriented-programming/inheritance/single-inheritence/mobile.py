class Mobile:
    model_name : str
    brand : str
    price : int
    features : str

    def __init__(self, model_name, brand, price, features):
        self.model_name = model_name
        self.brand = brand
        self.price = price
        self.features = features

    def get_details(self):
        print(f"Model : {self.model_name}")
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")
        print(f"Features : {self.features}")

mobile_instance1 = Mobile("S23","SAMSUNG",38000,"AI image editor")
mobile_instance1.get_details()

mobile_instance2 = Mobile("IPhone 15","Apple",55000,"Type c charging")
mobile_instance2.get_details()
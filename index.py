class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age 
        self.is_rewards_member = False 
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(f"Congrats {self.first_name}, you are now enrolled!")

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount


carl = User("Carl", "Johnson", "carljohnson@gmail.com", 24)
# carl.display_info()
carl.enroll()

jacob = User("Jacob", "Ehrler", "jacobehrler@gmail.com", 24)
jessica = User("Jessica", "Smith", "jsmith@icloud.com", 26)

jacob.spend_points(50)
jessica.enroll()
jessica.spend_points(80)

carl.display_info()
jacob.display_info()
jessica.display_info()




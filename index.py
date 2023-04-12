class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age 
        self.is_rewards_member = False 
        self.gold_card_points = 0

    def display_info(self):
        print("===================")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("===================")
        

    def enroll(self):
        
        if self.is_rewards_member:
            print("User is already a member.")
            return False
        
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):

        if self.gold_card_points < amount:
            "You don't have enough points."
            return

        self.gold_card_points -= amount 


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




import datetime

class User:
    """
    This is a class to obtain the names and birthdays of a user
    """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        
        # extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    
    def age(self):
        """
        Returns the age of a user
        """
        today = datetime.date(2023, 4, 27)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm ,dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)

if __name__ == '__main__':
    
    user = User("Dave Bowman", "19720430")
    print(user.age())
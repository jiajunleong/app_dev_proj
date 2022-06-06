class User:
    count_id = 0
    def __init__(self, first_name, last_name, gender, email,Password) :
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender

        self.__email = email
        self.__Password = Password

    def get_user_id(self):
        return self.__user_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_gender(self):
        return self.__gender
    def get_email(self):
        return self.__email
    def get_Password(self):
        return self.__Password
    
    def set_user_id(self, user_id):
        self.__user_id = user_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_gender(self,gender):
        self.__gender = gender
    def set_email(self,email):
        self.__email = email
    def set_Password(self,Password):
        self.__Password = Password

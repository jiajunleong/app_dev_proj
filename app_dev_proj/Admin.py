import User


class Admin(User.User):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email,Password):
        super().__init__(first_name, last_name, gender, email,Password)
        Admin.count_id += 1
        self.__Admin_id=Admin.count_id


    def get_admin_id(self):
        return self.__Admin_id


    def set_admin_id(self, Admin_id):
       self.__Admin_id = Admin_id


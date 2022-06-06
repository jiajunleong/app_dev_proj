import User


class repair(User.User):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email,Password, Services):
        super().__init__(first_name, last_name, gender, email,Password)
        repair.count_id +=1
        self.__repair_id=repair.count_id
        self.__Services = Services


    def get_repair_id(self):
        return self.__repair_id

    def get_Services(self):
        return self.__Services

    def set_Services(self, Services):
       self.__Services = Services
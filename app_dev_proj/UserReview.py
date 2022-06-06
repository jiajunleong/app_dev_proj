class UserReview:
    count_id = 0
    def __init__(self, name, repairmen_name, review ) :
        UserReview.count_id += 1
        self.__user_id = UserReview.count_id
        self.__name = name
        self.__repairmen_name = repairmen_name
        self.__review = review

    def get_user_id(self):
        return self.__user_id
    def get_name(self):
        return self.__name
    def get_repairmen_name(self):
        return self.__repairmen_name
    def get_review(self):
        return self.__review

    
    def set_user_id(self, user_id):
        self.__user_id = user_id
    def set_name(self, name):
        self.__name = name
    def set_repairmen_name(self, repairmen_name):
        self.__repairmen_name = repairmen_name
    def set_review(self,review):
        self.__review = review

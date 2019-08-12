class User:

    def __init__(self, login_id, first_name, last_name, phone):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def get_login_id(self):
        return self.login_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def to_json(self):
        return "'login_id' : '{}','first_name': '{}', 'last_name' : '{}' , 'phone' : '{}'  " \
            .format(self.get_login_id(), self.get_first_name(), self.get_last_name(), self.get_phone())


# class UserSchema(app.ma.Schema):
#     class Meta:
#         fields = ('user_id', 'login_id', 'first_name', 'last_name', 'phone', 'created_on', 'updated_on')
#
#
# user_schema = UserSchema(strict=True)
# users_schema = UserSchema(many=True, strict=True)

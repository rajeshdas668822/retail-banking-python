class Customer:

    def __init__(self, customer_ref, id_type, personal_id, email, user_id):
        self.customer_ref = customer_ref
        self.id_type = id_type
        self.personal_id = personal_id
        self.email = email
        self.created_by = user_id
        self.updated_by = user_id

    def get_customer_ref(self):
        return self._customer_ref

    def get_id_type(self):
        return self._id_type

    def get_personal_id(self):
        return self._personal_id

    def get_email(self):
        return self._email

class Usuarios:

    def __init__(self, fullname_edit,
                user_edit,
                email_edit,
                password_edit):

        self.fullname_edit = fullname_edit
        self.user_edit = user_edit
        self.email_edit = email_edit
        self.password_edit = password_edit

    def __str__(self):
        return f"Usuario: {self.user_edit} Contraseña: {self.password2_edit}"
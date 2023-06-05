class Usuarios:

    def __init__(self, fecha,
                fullname_edit,
                user_edit,
                email_edit,
                password_edit,
                height_edit,
                weight_edit,
                nivel_resp,
                plan_resp,
                disease_resp):

        self.fecha = fecha
        self.fullname_edit = fullname_edit
        self.user_edit = user_edit
        self.email_edit = email_edit
        self.password_edit = password_edit
        self.height_edit = height_edit
        self.weight_edit = weight_edit
        self.nivel_resp = nivel_resp
        self.plan_resp = plan_resp
        self.disease_resp = disease_resp

    def __str__(self):
        return f"Usuario: {self.user_edit} Contraseña: {self.password2_edit}"
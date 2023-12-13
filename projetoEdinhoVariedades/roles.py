from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {'cadastrar_produtos': True, 'editar_produtos': True, 'deletar_produtos': True}


# class Consumidor(AbstractUserRole):
#     available_permissions = {}
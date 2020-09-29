def usuario_valido(usuario):
    def decorator(funcao_chamada):
        def inner(*args, **kwargs):
            if usuario == 'Eduardo':
                return funcao_chamada(*args, **kwargs)
            else:
                raise AttributeError

        return inner
    return decorator

@usuario_valido("Eduardo")
def diz_ola():
    print('ola')

diz_ola()
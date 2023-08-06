class DependencyNotFound(Exception):
    def __init__(self,dependency_name:str) -> None:
        msg = f"""
            Dependencia -> {dependency_name}
            No se puede injectar este tipo porque no está registrada en las dependencias
            Por favor registre el servicio o diccionario con el decorador injectdep.register_dependency
        """
        super().__init__(msg)
from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=========================
# Clase storemaneger
# NO TIENE VARIABLES !!!
#=========================
class ManejoDEInscripciones:
    #===============================================================
    # Decorador staticmedthod
    # EL objeto solo tiene la funcion inscribirUsuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    #===============================================================}
    @staticmethod
    def inscribirUsuario(usuarui: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarois.cerrar(
                #===============================================================}
                @staticmethod
                def inscribirUsuario(usuarui: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
                print("------> Guardando usuario ... \n")
                repositorioDeUsuarios.abrir()
                repositorioDeUsuarios.guardar(usuario)
                repositorioDeUsuarois.cerrar()

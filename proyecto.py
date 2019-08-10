class Comunidad():#Clase padre
    def __init__(self,nombre,cuenta,contra):
        self.name = nombre
        self.__ct = cuenta
        self.__cr = contra
        
    def datos(self):
        print('Nombre:',self.name)
        print('Cuenta:',self.__ct)
        print('Contraseña',self.__cr)
        
        
class Administrativo(Comunidad):#1ra clase hija
    def __init__(self,nombre,cuenta,contra,expLaboral):
        super().__init__(nombre,cuenta,contra)
        self.EXPlabo = expLaboral
        
    def datos(self):
        super().datos()
        print('Su experiencia laboral es:',self.EXPlabo,'años')
        
class Estudiante(Comunidad):#2da clase hija
    def __init__(self,nombre,cuenta,contra,promGeneral,creditos):
        super().__init__(nombre,cuenta,contra)
        self.__pGeneral = promGeneral
        self.__CREDITOS = creditos
        
    def datos(self):
        super().datos()
        print('Su promedio es:', self.__pGeneral)
        print('Su avance de creditos es:',self.__CREDITOS,'%')
        
class Profesor(Administrativo):#3ra clase hija
    def __init__(self,nombre,cuenta,contra,expLaboral,numeroGrups):
        super().__init__(nombre,cuenta,contra,expLaboral)
        self.grups = numeroGrups
        #self.expl = explaboral
        
    def datos(self):
        super().datos()
        print('Numero de Grupos:',self.grups)
        #print('Su experiencia laboral es de:',self.expl,'años')

#En un inicio pense aplicar la multiherencia de manera que la class Profesor(Comunidad,Admiistrativo), 
#pero me di cuenta que no era necesario que heredara de manera explicita de Comunidad ya que Administrativo
#ya posee esa herencia (nombre,cuenta y contra). Por lo tanto solo es necesario heredar de una sola clase y es 
#la dee Administrativo.
        

        
#us1 = Comunidad('rene',312,738)
#us1.datos()

#us2 = Administrativo('rene',4432,55,5)
#us2.datos()

us3 = Estudiante('rene',4432,55,8.89,89)
us3.datos()

#us4 = Profesor('rene',3124,877,5,5)
#us4.datos()
class Asignacion:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        asignacion = self.session.get("asignacion")
        if not asignacion:
            self.session["asignacion"]={}
            self.asignacion=self.session["asignacion"]
        else:
            self.asignacion=asignacion

    def add(self,obj):
        id=str(obj.placa)
        if id not in self.asignacion.keys():
            self.asignacion[id]={
            "asignacion_id":obj.placa,
            "marca":obj.marca.marca,
            "modelo":obj.modelo.modelo,
            }
        self.save()

    def save(self):
        self.session["asignacion"]=self.asignacion
        self.session.modified=True

    def remove(self,obj):
        id = str(obj.placa)
        if id in self.asignacion:
            del self.asignacion[id]
            self.save()

    def clear(self):
        print("clear")
        self.asignacion={}
        self.save()
            



class Funcionario:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        funcionario = self.session.get("funcionario")
        if not funcionario:
            self.session["funcionario"]={}
            self.funcionario=self.session["funcionario"]
        else:
            self.funcionario=funcionario
    def add(self,query):
        id=str(query.identificacion)
        if id not in self.funcionario.keys():
            self.funcionario[id]={
            "funcionario_id":query.pk,
            "funcionario_nombre":query.nombres,
            "funcionario_apellido": query.apellidos,
            }
        self.save()

    def save(self):
        self.session["funcionario"]=self.funcionario
        self.session.modified=True

    def clear(self):
        print("clear")
        self.funcionario={}
        self.save()
            

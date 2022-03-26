class Baja:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        baja = self.session.get("baja")
        if not baja:
            self.session["baja"]={}
            self.baja=self.session["baja"]
        else:
            self.baja=baja

    def add(self,consulta):
        id=str(consulta.placa)
        if id not in self.baja.keys():
            self.baja[id]={
            "baja_id":consulta.placa,
            "marca":consulta.marca.marca,
            "modelo":consulta.modelo.modelo,
            }
        self.save()

    def save(self):
        self.session["baja"]=self.baja
        self.session.modified=True

    def remove(self,consulta):
        id = str(consulta.placa)
        if id in self.baja:
            del self.baja[id]
            self.save()
    def clear(self):
        self.session["baja"]={}
        self.session.modified=True
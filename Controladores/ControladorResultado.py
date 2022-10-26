from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    """
    Asignacion Candidato y mesa a Resultado
    """
    def create(self,infoResultado,id_Candidato,id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_Candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de Resultado (Candidato y mesa)
    """
    def update(self,id,infoResultado,id_Candidato,id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa = infoResultado["numero_mesa"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_Candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los inscritos en una mesa"
    def listarInscritosEnMateria(self, id_mesa):
        return self.repositorioResultado.getListadoInscritosEnMesa(id_mesa)

"""
    "Obtener notas mas altas por curso"
    def notasMasAltasPorCurso(self):
        return self.repositorioInscripcion.getMayorNotaPorCurso()

    "Obtener promedio de notas en materia"
    def promedioNotasEnMateria(self, id_materia):
        return self.repositorioInscripcion.promedioNotasEnMateria(id_materia)

"""
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    """
    def getMayorNotaPorCurso(self):
        query1 = {
            "$group": {
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.queryAgregation(pipeline)

    def promedioNotasEnMateria(self, id_materia):
        query1 = {
            "$match": {"materia.$id": ObjectId(id_materia)}
        }
        query2 = {
            "$group": {
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAgregation(pipeline)
    """
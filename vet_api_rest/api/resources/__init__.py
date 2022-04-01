from vet_api_rest.api.resources.usuario import UserResource, UserList
from vet_api_rest.api.resources.almacen_medicamentos import AlmacenMedicamentosResource, AlmacenMedicamentosList
from vet_api_rest.api.resources.almacen_petshop import AlmacenPetshopResource, AlmacenPetshopList
from vet_api_rest.api.resources.categoria_medicamento import CategoriaMedicamentoResource, CategoriaMedicamentoList
from vet_api_rest.api.resources.categoria_producto import CategoriaProductoResource, CategoriaProductoList
from vet_api_rest.api.resources.citas import CitasResource, CitasList
from vet_api_rest.api.resources.cliente import ClienteResource, ClienteList
from vet_api_rest.api.resources.entidad import EntidadResource, EntidadList
from vet_api_rest.api.resources.proveedor import ProveedorResource, ProveedorList
from vet_api_rest.api.resources.nivel import NivelResource, NivelList
from vet_api_rest.api.resources.persona import PersonaResource, PersonaList
from vet_api_rest.api.resources.compra import CompraResource, CompraList
from vet_api_rest.api.resources.compra_medicamento import CompraMedicamentoList, CompraMedicamentoResource
from vet_api_rest.api.resources.compra_producto import CompraProductoResource, CompraProductoList
from vet_api_rest.api.resources.contacto import ContactoResource, ContactoList
from vet_api_rest.api.resources.dosis_medicamento import DosisMedicamentoResource, DosisMedicamentoList
from vet_api_rest.api.resources.historial_mascota import HistorialMascotaResource, HistorialMascotaList
from vet_api_rest.api.resources.vistas_stock import MascotaCompletoList, MascotaCompletoResource

__all__ = ["UserResource", "UserList", "AlmacenMedicamentosResource", "AlmacenMedicamentosList",
           "AlmacenPetshopResource", "AlmacenPetshopList", "CategoriaMedicamentoResource", "CategoriaMedicamentoList",
           "CategoriaProductoResource", "CategoriaProductoList", "CitasResource", "CitasList", "ClienteResource",
           "ClienteList", "EntidadResource", "EntidadList", "ProveedorResource", "ProveedorList", "NivelResource",
           "NivelList", "PersonaResource", "PersonaList", "CompraResource", "CompraList", "CompraMedicamentoResource",
           "CompraMedicamentoList", "CompraProductoResource", "CompraProductoList", "ContactoResource", "ContactoList",
           "DosisMedicamentoResource", "DosisMedicamentoList", "HistorialMascotaResource", "HistorialMascotaList",
           "MascotaCompletoList", "MascotaCompletoResource"]

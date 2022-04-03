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
from vet_api_rest.api.resources.medicamento_venta import MedicamentoVentaResource, MedicamentoVentaList
from vet_api_rest.api.resources.medicamento_almacen import MedicamentoAlmacenResource, MedicamentoAlmacenList
from vet_api_rest.api.resources.medicamentos import MedicamentoResource, MedicamentoList
from vet_api_rest.api.resources.producto_almacen import ProductoAlmacenResource, ProductoAlmacenList
from vet_api_rest.api.resources.producto_por_pagar import ProductoPorPagarResource, ProductoPorPagarList
from vet_api_rest.api.resources.producto_venta import ProductoVentaResource, ProductoVentaList
from vet_api_rest.api.resources.productos import ProductoResource, ProductoList
from vet_api_rest.api.resources.raza import RazaResource, RazaList
from vet_api_rest.api.resources.servicio_por_pagar import ServicioPorPagarResource, ServicioPorPagarList
from vet_api_rest.api.resources.servicio_venta import ServicioVentaResource, ServicioVentaList
from vet_api_rest.api.resources.servicios import ServicioList, ServicioResource
from vet_api_rest.api.resources.tipo_contacto import TipoContactoResource, TipoContactoList
from vet_api_rest.api.resources.tipo_mascota import TipoMascotaResource, TipoMascotaList
from vet_api_rest.api.resources.tratamientos_pendientes import TratamientosPendientesResource, \
    TratamientosPendientesList
from vet_api_rest.api.resources.unidad_contenido import UnidadContenidoResource, UnidadContenidoList
from vet_api_rest.api.resources.vacunas import VacunaResource, VacunaList
from vet_api_rest.api.resources.venta import VentaResource, VentaList
from vet_api_rest.api.resources.marca_medicamento import MarcaMedicamentoResource, MarcaMedicamentoList
from vet_api_rest.api.resources.marca_producto import MarcaProductoResource, MarcaProductoList


__all__ = ["UserResource", "UserList", "AlmacenMedicamentosResource", "AlmacenMedicamentosList",
           "AlmacenPetshopResource", "AlmacenPetshopList", "CategoriaMedicamentoResource", "CategoriaMedicamentoList",
           "CategoriaProductoResource", "CategoriaProductoList", "CitasResource", "CitasList", "ClienteResource",
           "ClienteList", "EntidadResource", "EntidadList", "ProveedorResource", "ProveedorList", "NivelResource",
           "NivelList", "PersonaResource", "PersonaList", "CompraResource", "CompraList", "CompraMedicamentoResource",
           "CompraMedicamentoList", "CompraProductoResource", "CompraProductoList", "ContactoResource", "ContactoList",
           "DosisMedicamentoResource", "DosisMedicamentoList", "HistorialMascotaResource", "HistorialMascotaList",
           "MascotaCompletoList", "MascotaCompletoResource", "MedicamentoVentaResource", "MedicamentoVentaList",
           "MedicamentoAlmacenResource", "MedicamentoAlmacenList", "MedicamentoResource", "MedicamentoList",
           "ProductoAlmacenResource", "ProductoAlmacenList", "ProductoPorPagarResource", "ProductoPorPagarList",
           "ProductoVentaResource", "ProductoVentaList", "ProductoList", "ProductoResource", "RazaResource",
           "RazaList", "ServicioPorPagarResource", "ServicioPorPagarList", "ServicioVentaResource",
           "ServicioVentaList", "ServicioList", "ServicioResource", "TipoContactoResource", "TipoContactoList",
           "TipoMascotaResource", "TipoMascotaList", "TratamientosPendientesResource", "TratamientosPendientesList",
           "UnidadContenidoResource", "UnidadContenidoList", "VacunaResource", "VacunaList", "VentaResource",
           "VentaList", "MarcaMedicamentoResource", "MarcaMedicamentoList", "MarcaProductoResource",
           "MarcaProductoList"]

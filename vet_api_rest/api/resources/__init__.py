from abarrotes_api_rest.api.resources.usuario import UserResource, UserList
from abarrotes_api_rest.api.resources.proveedor import ProveedorResource, ProveedorList
from abarrotes_api_rest.api.resources.cliente import ClienteResource, ClienteList
from abarrotes_api_rest.api.resources.localidad import LocalidadResource, LocalidadList
from abarrotes_api_rest.api.resources.departamento import DepartamentoResource, DepartamentoList
from abarrotes_api_rest.api.resources.contacto import ContactoResource, ContactoList
from abarrotes_api_rest.api.resources.contacto_correo import ContactoCorreoResource, ContactoCorreoList
from abarrotes_api_rest.api.resources.contacto_telefono import ContactoTelefonoResource, ContactoTelefonoList
from abarrotes_api_rest.api.resources.contacto_direccion import ContactoDireccionResource, ContactoDireccionList
from abarrotes_api_rest.api.resources.unidad_presentacion import UnidadPresentacionResource, UnidadPresentacionList
from abarrotes_api_rest.api.resources.presentacion_producto import PresentacionProductoResource, PresentacionProductoList
from abarrotes_api_rest.api.resources.producto import ProductoResource, ProductoList
from abarrotes_api_rest.api.resources.almacen import AlmacenResource, AlmacenList
from abarrotes_api_rest.api.resources.producto_almacen import ProductoAlmacenResource, ProductoAlmacenList
from abarrotes_api_rest.api.resources.disposicion import DisposicionList, DisposicionResource
from abarrotes_api_rest.api.resources.motivo import MotivoResource, MotivoList
from abarrotes_api_rest.api.resources.venta import VentaResource, VentaList


__all__ = ["UserResource", "UserList", "ProveedorResource", "ProveedorList", "ClienteResource", "ClienteList",
           "LocalidadResource", "LocalidadList", "DepartamentoResource", "DepartamentoList", "ContactoResource",
           "ContactoList", "ContactoCorreoResource", "ContactoCorreoList", "ContactoTelefonoResource",
           "ContactoTelefonoList", "ContactoDireccionResource", "ContactoDireccionList", "UnidadPresentacionResource",
           "UnidadPresentacionList", "PresentacionProductoResource", "PresentacionProductoList", "ProductoResource",
           "ProductoList", "AlmacenResource", "AlmacenList", "ProductoAlmacenResource", "ProductoAlmacenList",
           "DisposicionList", "DisposicionResource", "MotivoResource", "MotivoList", "VentaResource", "VentaList"]

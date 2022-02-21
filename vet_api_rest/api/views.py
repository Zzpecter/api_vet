from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from abarrotes_api_rest.api.resources import UserResource, UserList, ProveedorResource, ProveedorList,ClienteResource, \
    ClienteList, LocalidadResource, LocalidadList, DepartamentoResource, DepartamentoList, ContactoResource, \
    ContactoList, ContactoCorreoResource, ContactoCorreoList, ContactoTelefonoResource, ContactoTelefonoList, \
    ContactoDireccionList, ContactoDireccionResource, UnidadPresentacionList, UnidadPresentacionResource, \
    PresentacionProductoResource, PresentacionProductoList, ProductoResource, ProductoList, AlmacenResource, \
    AlmacenList, ProductoAlmacenList, ProductoAlmacenResource, DisposicionList, DisposicionResource, MotivoResource, \
    MotivoList, VentaList, VentaResource


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:id_entidad>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(ProveedorResource, "/proveedores/<int:id_entidad>", endpoint="proveedor_by_id")
api.add_resource(ProveedorList, "/proveedores", endpoint="proveedores")
api.add_resource(ClienteResource, "/clientes/<int:id_entidad>", endpoint="cliente_by_id")
api.add_resource(ClienteList, "/clientes", endpoint="clientes")
api.add_resource(LocalidadResource, "/localidades/<int:id_localidad>", endpoint="localidad_by_id")
api.add_resource(LocalidadList, "/localidades", endpoint="localidades")
api.add_resource(DepartamentoResource, "/departamentos/<int:id_departamento>", endpoint="departamento_by_id")
api.add_resource(DepartamentoList, "/departamentos", endpoint="departamentos")
api.add_resource(ContactoResource, "/contactos/<int:id_contacto>", endpoint="contacto_by_id")
api.add_resource(ContactoList, "/contactos", endpoint="contactos")
api.add_resource(ContactoCorreoResource, "/contactos_correo/<int:id_contacto_correo>", endpoint="contacto_correo_by_id")
api.add_resource(ContactoCorreoList, "/contactos_correo", endpoint="contactos_correo")
api.add_resource(ContactoTelefonoResource, "/contactos_telefono/<int:id_contacto_telefono>", endpoint="contacto_telefono_by_id")
api.add_resource(ContactoTelefonoList, "/contactos_telefono", endpoint="contactos_telefono")
api.add_resource(ContactoDireccionResource, "/contactos_direccion/<int:id_contacto_direccion>", endpoint="contacto_direccion_by_id")
api.add_resource(ContactoDireccionList, "/contactos_direccion", endpoint="contactos_direccion")
api.add_resource(UnidadPresentacionResource, "/unidad_presentacion/<int:id_unidad_presentacion>", endpoint="unidad_presentacion_by_id")
api.add_resource(UnidadPresentacionList, "/unidad_presentacion", endpoint="unidad_presentacion")
api.add_resource(PresentacionProductoResource, "/presentacion_producto/<int:id_presentacion_producto>", endpoint="presentacion_producto_by_id")
api.add_resource(PresentacionProductoList, "/presentacion_producto", endpoint="presentacion_producto")
api.add_resource(ProductoResource, "/productos/<int:id_producto>", endpoint="producto_by_id")
api.add_resource(ProductoList, "/productos", endpoint="productos")
api.add_resource(AlmacenResource, "/almacenes/<int:id_almacen>", endpoint="almacen_by_id")
api.add_resource(AlmacenList, "/almacenes", endpoint="almacenes")
api.add_resource(ProductoAlmacenResource, "/producto_almacen/<int:id_producto_almacen>", endpoint="producto_almacen_by_id")
api.add_resource(ProductoAlmacenList, "/producto_almacen", endpoint="producto_almacen")
api.add_resource(DisposicionResource, "/disposicion/<int:id_salida_producto>", endpoint="disposicion_by_id")
api.add_resource(DisposicionList, "/disposicion", endpoint="disposicion")
api.add_resource(MotivoResource, "/motivos/<int:id_motivo>", endpoint="motivos_by_id")
api.add_resource(MotivoList, "/motivos", endpoint="motivos")
api.add_resource(VentaResource, "/ventas/<int:id_salida_producto>", endpoint="ventas_by_id")
api.add_resource(VentaList, "/ventas", endpoint="ventas")


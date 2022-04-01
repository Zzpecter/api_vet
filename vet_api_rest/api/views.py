from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from vet_api_rest.api.resources import UserResource, UserList, AlmacenMedicamentosResource, AlmacenMedicamentosList, \
    AlmacenPetshopResource, AlmacenPetshopList, CategoriaMedicamentoResource, CategoriaMedicamentoList, \
    CategoriaProductoResource, CategoriaProductoList, CitasResource, CitasList, ClienteResource, ClienteList, \
    EntidadResource, EntidadList, ProveedorResource, ProveedorList, NivelResource, NivelList, PersonaResource, \
    PersonaList, CompraList, CompraResource, CompraMedicamentoResource, CompraMedicamentoList, CompraProductoList, \
    CompraProductoResource, ContactoResource, ContactoList, DosisMedicamentoResource, DosisMedicamentoList, \
    HistorialMascotaResource, HistorialMascotaList, MascotaCompletoList, MascotaCompletoResource


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:id_usuario>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(AlmacenMedicamentosResource, "/almacen_medicamentos/<int:id_almacen_medicamentos>", endpoint="almacen_medicamentos_by_id")
api.add_resource(AlmacenMedicamentosList, "/almacen_medicamentos", endpoint="almacen_medicamentos")
api.add_resource(AlmacenPetshopResource, "/almacen_petshop/<int:id_almacen_petshop>", endpoint="almacen_petshop_by_id")
api.add_resource(AlmacenPetshopList, "/almacen_petshop", endpoint="almacen_petshop")
api.add_resource(CategoriaMedicamentoResource, "/categoria_medicamento/<int:id_categoria_medicamento>", endpoint="categoria_medicamento_by_id")
api.add_resource(CategoriaMedicamentoList, "/categoria_medicamento", endpoint="categoria_medicamento")
api.add_resource(CategoriaProductoResource, "/categoria_producto/<int:id_categoria_producto>", endpoint="categoria_producto_by_id")
api.add_resource(CategoriaProductoList, "/categoria_producto", endpoint="categoria_producto")
api.add_resource(CitasResource, "/citas/<int:id_cita>", endpoint="citas_by_id")
api.add_resource(CitasList, "/citas", endpoint="citas")
api.add_resource(ClienteResource, "/clientes/<int:id_cliente>", endpoint="clientes_by_id")
api.add_resource(ClienteList, "/clientes", endpoint="clientes")
api.add_resource(EntidadResource, "/entidad/<int:id_entidad>", endpoint="entidad_by_id")
api.add_resource(EntidadList, "/entidad", endpoint="entidad")
api.add_resource(ProveedorResource, "/proveedores/<int:id_proveedor>", endpoint="proveedores_by_id")
api.add_resource(ProveedorList, "/proveedores", endpoint="proveedores")
api.add_resource(NivelResource, "/niveles/<int:id_nivel>", endpoint="niveles_by_id")
api.add_resource(NivelList, "/niveles", endpoint="niveles")
api.add_resource(PersonaResource, "/personas/<int:id_persona>", endpoint="personas_by_id")
api.add_resource(PersonaList, "/personas", endpoint="personas")
api.add_resource(CompraResource, "/compras/<int:id_compra>", endpoint="compras_by_id")
api.add_resource(CompraList, "/compras", endpoint="compras")
api.add_resource(CompraMedicamentoResource, "/compra_medicamento/<int:id_compra_medicamento>", endpoint="compra_medicamento_by_id")
api.add_resource(CompraMedicamentoList, "/compra_medicamento", endpoint="compra_medicamento")
api.add_resource(CompraProductoResource, "/compra_producto/<int:id_compra_producto>", endpoint="compra_producto_by_id")
api.add_resource(CompraProductoList, "/compra_producto", endpoint="compra_producto")
api.add_resource(ContactoResource, "/contactos/<int:id_contacto>", endpoint="contactos_by_id")
api.add_resource(ContactoList, "/contactos", endpoint="contactos")
api.add_resource(DosisMedicamentoResource, "/dosis_medicamento/<int:id_dosis_medicamento>", endpoint="dosis_medicamento_by_id")
api.add_resource(DosisMedicamentoList, "/dosis_medicamento", endpoint="dosis_medicamento")
api.add_resource(HistorialMascotaResource, "/historial_mascota/<int:id_historial_mascota>", endpoint="historial_mascota_by_id")
api.add_resource(HistorialMascotaList, "/historial_mascota", endpoint="historial_mascota")


api.add_resource(MascotaCompletoResource, "/vistas/mascota_completo/<string:column>/<string:value>", endpoint="vi_mascota_completo_by_value")
api.add_resource(MascotaCompletoList, "/vistas/mascota_completo", endpoint="vi_mascota_completo")


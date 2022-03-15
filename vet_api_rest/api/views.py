from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from vet_api_rest.api.resources import UserResource, UserList, AlmacenMedicamentosResource, AlmacenMedicamentosList, \
    AlmacenPetshopResource, AlmacenPetshopList, CategoriaMedicamentoResource, CategoriaMedicamentoList, \
    CategoriaProductoResource, CategoriaProductoList, CitasResource, CitasList, ClienteResource, ClienteList, \
    EntidadResource, EntidadList, ProveedorResource, ProveedorList, NivelResource, NivelList, PersonaResource, \
    PersonaList


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


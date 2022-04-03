from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from vet_api_rest.api.resources import UserResource, UserList, AlmacenMedicamentosResource, AlmacenMedicamentosList, \
    AlmacenPetshopResource, AlmacenPetshopList, CategoriaMedicamentoResource, CategoriaMedicamentoList, \
    CategoriaProductoResource, CategoriaProductoList, CitasResource, CitasList, ClienteResource, ClienteList, \
    EntidadResource, EntidadList, ProveedorResource, ProveedorList, NivelResource, NivelList, PersonaResource, \
    PersonaList, CompraList, CompraResource, CompraMedicamentoResource, CompraMedicamentoList, CompraProductoList, \
    CompraProductoResource, ContactoResource, ContactoList, DosisMedicamentoResource, DosisMedicamentoList, \
    HistorialMascotaResource, HistorialMascotaList, MascotaCompletoList, MascotaCompletoResource, \
    MedicamentoVentaResource, MedicamentoVentaList, MedicamentoAlmacenResource, MedicamentoAlmacenList, \
    MedicamentoResource, MedicamentoList, ProductoAlmacenResource, ProductoAlmacenList, ProductoPorPagarResource, \
    ProductoPorPagarList, ProductoVentaResource, ProductoVentaList, ProductoList, ProductoResource, RazaResource, \
    RazaList, ServicioPorPagarList, ServicioPorPagarResource, ServicioVentaResource, ServicioVentaList, ServicioList, \
    ServicioResource, TipoContactoResource, TipoContactoList, TipoMascotaResource, TipoMascotaList, \
    TratamientosPendientesResource, TratamientosPendientesList, UnidadContenidoResource, UnidadContenidoList, \
    VacunaResource, VacunaList, VentaResource, VentaList, MarcaProductoResource, MarcaProductoList, \
    MarcaMedicamentoResource, MarcaMedicamentoList


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
api.add_resource(MedicamentoVentaResource, "/medicamento_venta/<int:id_medicamento_venta>", endpoint="medicamento_venta_by_id")
api.add_resource(MedicamentoVentaList, "/medicamento_venta", endpoint="medicamento_venta")
api.add_resource(MedicamentoAlmacenResource, "/medicamento_almacen/<int:id_medicamento_almacen>", endpoint="medicamento_almacen_by_id")
api.add_resource(MedicamentoAlmacenList, "/medicamento_almacen", endpoint="medicamento_almacen")
api.add_resource(MedicamentoResource, "/medicamentos/<int:id_medicamento>", endpoint="medicamentos_by_id")
api.add_resource(MedicamentoList, "/medicamentos", endpoint="medicamentos")
api.add_resource(ProductoAlmacenResource, "/producto_almacen/<int:id_producto_almacen>", endpoint="producto_almacen_by_id")
api.add_resource(ProductoAlmacenList, "/producto_almacen", endpoint="producto_almacen")
api.add_resource(ProductoPorPagarResource, "/producto_por_pagar/<int:id_producto_por_pagar>", endpoint="producto_por_pagar_by_id")
api.add_resource(ProductoPorPagarList, "/producto_por_pagar", endpoint="producto_por_pagar")
api.add_resource(ProductoVentaResource, "/producto_venta/<int:id_producto_venta>", endpoint="producto_venta_by_id")
api.add_resource(ProductoVentaList, "/producto_venta", endpoint="producto_venta")
api.add_resource(ProductoResource, "/productos/<int:id_producto>", endpoint="producto_by_id")
api.add_resource(ProductoList, "/productos", endpoint="productos")
api.add_resource(RazaResource, "/razas/<int:id_raza>", endpoint="razas_by_id")
api.add_resource(RazaList, "/razas", endpoint="razas")
api.add_resource(ServicioPorPagarResource, "/servicio_por_pagar/<int:id_servicio_por_pagar>", endpoint="servicio_por_pagar_by_id")
api.add_resource(ServicioPorPagarList, "/servicio_por_pagar", endpoint="servicio_por_pagar")
api.add_resource(ServicioVentaResource, "/servicio_venta/<int:id_servicio_venta>", endpoint="servicio_venta_by_id")
api.add_resource(ServicioVentaList, "/servicio_venta", endpoint="servicio_venta")
api.add_resource(ServicioResource, "/servicios/<int:id_servicio>", endpoint="servicios_by_id")
api.add_resource(ServicioList, "/servicios", endpoint="servicios")
api.add_resource(TipoContactoResource, "/tipo_contacto/<int:id_tipo_contacto>", endpoint="tipo_contacto_by_id")
api.add_resource(TipoContactoList, "/tipo_contacto", endpoint="tipo_contacto")
api.add_resource(TipoMascotaResource, "/tipo_mascota/<int:id_tipo_mascota>", endpoint="tipo_mascota_by_id")
api.add_resource(TipoMascotaList, "/tipo_mascota", endpoint="tipo_mascota")
api.add_resource(TratamientosPendientesResource, "/tratamientos_pendientes/<int:id_tratamiento_pendiente>", endpoint="tratamientos_pendientes_by_id")
api.add_resource(TratamientosPendientesList, "/tratamientos_pendientes", endpoint="tratamientos_pendientes")
api.add_resource(UnidadContenidoResource, "/unidad_contenido/<int:id_unidad_contenido>", endpoint="unidad_contenido_by_id")
api.add_resource(UnidadContenidoList, "/unidad_contenido", endpoint="unidad_contenido")
api.add_resource(VacunaResource, "/vacunas/<int:id_vacuna>", endpoint="vacunas_by_id")
api.add_resource(VacunaList, "/vacunas", endpoint="vacunas")
api.add_resource(VentaResource, "/ventas/<int:id_venta>", endpoint="ventas_by_id")
api.add_resource(VentaList, "/ventas", endpoint="ventas")
api.add_resource(MarcaMedicamentoResource, "/marca_medicamento/<int:id_marca_medicamento>", endpoint="marca_medicamento_by_id")
api.add_resource(MarcaMedicamentoList, "/marca_medicamento", endpoint="marca_medicamento")
api.add_resource(MarcaProductoResource, "/marca_producto/<int:id_marca_producto>", endpoint="marca_producto_by_id")
api.add_resource(MarcaProductoList, "/marca_producto", endpoint="marca_producto")


api.add_resource(MascotaCompletoResource, "/vistas/mascota_completo/<string:column>/<string:value>", endpoint="vi_mascota_completo_by_value")
api.add_resource(MascotaCompletoList, "/vistas/mascota_completo", endpoint="vi_mascota_completo")


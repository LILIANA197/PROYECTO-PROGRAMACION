# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy

from Proyecto import material
from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from pedido import Pedido


doc1= Docente(cedula="0123457759", nombre="Marcelo", apellido= "Villalba", email="Marcelo@gmail.com",
               telefono="0944563344", direccion="Avenida El Ejercito", numero_libros=2, activo=True,
                carrera="Finanzas", titulo_3er_nivel="Licenciatura en Contaduria ",
                titulo_4to_nivel="Magister en Finanzas")
doc2= Docente(cedula="0964553423", nombre="Jessica", apellido= "Moncada", email="Jessica@gmail.com",
                telefono="0960356422", direccion="Avenida Juan TancaMarengo", numero_libros=4, activo=False,
                carrera="Psicologia", titulo_3er_nivel="Licenciada en Psicopedagogia",
                titulo_4to_nivel="Magister en estudios sociales")


# print(d1)
# print(d2)

# Estudiantes
est1 = Estudiante(cedula="0123456789", nombre="Pablo", apellido="Pérez", email="pablo@gmail.com",
                      telefono="0960354278", direccion="Francisco de Orellana", carrera="Ingeniería", numero_libros=2,
                      activo=True, nivel=2)
est2 = Estudiante(cedula="0987456123", nombre="Luisa", apellido="López", email="luisa@gmail.com",
                  telefono="0936157689", direccion="Avenida Sixto Garay", carrera="Medicina",
                  numero_libros=4, activo=False, nivel=3)

# print(e1)
# print(e2)
# print(e3)
# print(e4)


libro1 = Libro(codigo="620.1/C87", autor="Craig Jr Roy", titulo="Mecanica de materiales", anio=2002,
                   editorial="continental", disponible=True, cantidad_disponible=30, tipo_pasta="cubierta carton")


revista2 = Revista(codigo=" 10.7660/IC47702", autor="Smith J.M.& Davis H.",
                       titulo="Language acquisition among autistic children", anio=2019,
                       editorial="volume5_Issue2_2011", disponible=True, cantidad_disponible=104, tipo="online")



# pedido = Pedido(solicitante='joseph paez', lista_material='Compra domicilio',
#                  fecha_prestamo='20/junio/2023', fecha_devolucion='28/Junio/2023')

materiales = list()
materiales.append(libro1)
materiales.append(revista2)
# print(materiales)
pedido1 = Pedido(solicitante=doc1, fecha_prestamo='20/junio/2023', lista_material=materiales,
                 fecha_devolucion='28/Junio/2023', material=material)

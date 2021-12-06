from validator import val
from getpass import getpass
import stdiomask
from producto import producto
from vistas import vista_productos, total_ventas, vista_facturas, vista_factura_detalle, vista_factura_final,vista_detalle_producto
from consultas import select_producto
from usuario import Usuario
from factura import Factura,FacturaDetalle
import datetime
menuInicio=[
  {"id":1,"descripcion":"Crear usuario"},
  {"id":2,"descripcion":"Login"}
  ]
menuUsuario=[
  {"id":1,"descripcion":"controlStock","acciones":["vista Productos","seleccionar un producto","Ingresar Nuevo Producto"]},
  {"id":2,"descripcion":"facturacion","acciones":["vista facturacion","Ver detalle factura","generar factura"]}
  ]
menuLocal=[
  {"id":1,"nombre":"local_Urquiza"},
  {"id":2,"nombre":"local_Nuñez"},
  {"id":3,"nombre":"local_Martinez"}
  ]
medio_pago=['Debito','Credito','Mercado_Pago','Efectivo']

###########-------    REGISTRO EN LA DB   -------#############

def registro_detalle_ticket(newProducto):
  datos = newProducto
  errores=val.validar_detalle_factura(datos)

  if not errores:
    detalle_newProducto = FacturaDetalle(**datos)
    detalle_newProducto.save()
    flag=True
    return detalle_newProducto
        
  for error in errores.values():
    print(error)

def registro_ticket(localID):
  local = localID
  datos = {}

  ## ---- Seleccion medio de pago -----
  for i in medio_pago:
    print(medio_pago.index(i),i)

  seleccion_medio = int(input('Seleccione el numero que corresponde al medio de pago'))

  ## ----- Validacion de datos -------
  datos = {}
  datos["fecha"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  datos["medioDePago"]=medio_pago[seleccion_medio]
  datos["id_local"]= local
  print(datos)

  errores=val.validar_factura(datos)


  #### --- Si no hubo errrores, se guarda el ticket en la DB
  if not errores:
    ticket=Factura(**datos)
    ticket.save()
    print('Se añadió un nuevo ticket a la DB')

  return ticket
        
  for error in errores.values():
    print(error)

def registro_producto():
  flag =False
  while not flag == True:
    datos = {}
    try:
      datos["nombre"]=input("Ingrese el nombre del producto\n")
      datos["marca"]=input("Ingrese el marca\n")
      datos["precio"]=float(input("Ingrese el precio\n"))
      datos["PrecioVenta"]=float(input("Ingrese el Precioventa\n"))
      datos["id_categoria"]=int(input("Ingrese el id_categoria\n"))
      datos["num_codigo"]=input("Ingrese el num_codigo\n")
      datos["id_proveedor"]=int(input("Ingrese el numero de ID del Proveedor\n"))

      errores=val.validar_producto(datos)
    except NameError:
      print("Error - registro_producto - Algo salió mal")
      print(NameError)
    except:
      print("Error - registro_producto - Revise los campos que son numericos y los que son texto")
    else:
      if not errores:
        art=producto(**datos)
        art.save()
        print('Se añadió un nuevo articulo a la DB')
        flag=True
        return art
        
      for error in errores.values():
        print(error)

  def menu_principal():
    for opcion in menuUsuario:
      print(opcion['id'], opcion['descripcion'])
    opcionElegida = int(input("Escriba un numero\n"))

    if opcionElegida != 0:
      if opcionElegida == 1:
        menu_controlStock()

      elif opcionElegida == 2:
        print("---- FACTURACION -----")
    else:
      return

#########-----    CARRITO    -------###############
def generar_carrito():
  carrito=[]
  ticketFlag = False
  while not ticketFlag == True:
    respuesta = input('Quiere agregar otro producto S/N ???').upper()
    if respuesta == 'S':
      try:
        detalle = {}
        detalle['id_producto']=int(input('Ingrese ID producto'))
        detalle['cantidad'] = float(input('Ingrese cantidad'))
      except NameError:
        print('Error - generar_carrito ')
        print(NameError)
      except:
        print('Error - generar_carrito - Algo salio mal')
      else:
        if not detalle == {}:
          carrito.append(detalle)
        else:
          pass
    else:
      ticketFlag=True
      if not carrito == []:
        return carrito

def login():
  flag=False
  while not flag == True:
    try:
      datos = {}
      datos["nombre"]=input("Ingrese usuario\n")
      datos["mail"]=input("Ingrese mail\n")
      datos["clave"]=stdiomask.getpass(prompt="Ingrese contraseña\n",mask="*")
      errores = val.validar_login(datos)
    except:
      print('Ocurrio un error')
    else:
      if not errores:
        user = Usuario(**datos)
        print('Se logeo correctamente')
        flag = True
        return user
      print(errores)

def seleccion_local():
  print('Elija un local')
  local_elegido = {}

  localFlag = False
  ## ----    SELECCION LOCAL   -------
  while localFlag == False:
    for opcion in menuLocal:
      print(opcion['id'], opcion['nombre'])
    try:
      opcionElegida = int(input("Escriba un numero\n"))
    except:
      print('ingrese un numero')
      opcionElegida = int(input("Escriba un numero\n"))
    else:
      for local in menuLocal:
        if opcionElegida == local['id']:
          local_elegido["nombre"] = local['nombre']
          local_elegido['id'] = local['id']
          localFlag = True
          return local_elegido
        else:
          pass

###########------   MENUs  -----############

def menu_controlStock():
  print("---- CONTROL STOCK -----")
  #-------- Despliegue menu acciones -------------
  for accion in menuUsuario[0]['acciones']:
    print(menuUsuario[0]['acciones'].index(accion) + 1, accion)

  accionElegida = int(input("Escriba el numero de accion\n"))

  #--------------  Vista lista Productos  -------------
  if accionElegida == 1:
    print(vista_productos())
    menu_principal()

  #-------------- Vista segun ID Producto --------------
  elif accionElegida == 2:
    flag = False
    while not flag == True:
      try:
        input_ID = int(input('Escriba el ID del producto\nRecuerde que es un numero entero\n'))
      except NameError:
        print('Error')
        print(NameError())
      except:
        print('Error: ingrese un numero\n')
      else:
        art = select_producto(input_ID)
        print(art.get_details())
        flag=True

    menu_principal()
    #--------------  Registro Producto  ---------------
  
  #-------------- Registro de Producto --------------
  elif accionElegida == 3:
    registro_producto()
    menu_principal()

def menu_facturacion(local):
  local = local
  ### SELECCION ACCION
  print(' - acciones - ')
  menu_facturacion = menuUsuario[1]
  acciones = menu_facturacion['acciones']
  for i in acciones:
    print(acciones.index(i)+1,i)

  accionElegida = int(input("Escriba el numero de accion\n"))

  ## ------- Vista de toda la facturacion ----
  if accionElegida == 1:
    vista_facturas(local["nombre"])
    menu_principal()

  ## --------- Vista factura detalle --------
  elif accionElegida == 2:
    my_id = input('Introduzca el ID de la factura:\n')
    vista_factura_detalle(my_id)
    menu_principal()

  ## ------ Generar lista de productos de un ticket --------
  elif accionElegida == 3:
    print('######## Ticket ##########')
    lista_detalles = []

    carrito = generar_carrito()
    if not carrito == []:
      for producto in carrito:
        print("ID producto: ",producto.get('id_producto')," - Cantidad: ",producto.get('cantidad'))

      finalizar = input('Finalizar compra S/N')
      if finalizar.upper() == 'S':
        factura = registro_ticket(local["id"])
        print('Ticket ID: ',factura.get_id(),'\nMedio de pago: ',factura.get_medioP())
        if factura:
          for producto in carrito:
            producto['id_factura']=factura.get_id()
            newProducto = registro_detalle_ticket(producto)
            vista_detalle_producto( factura.get_id(), newProducto.get_id_producto() )

          print(vista_factura_final(factura.get_id()))
          menu_principal()
        else:
          print('Error - Menu_facturacion - Generar factura - Hubo un error en la generacion de factura')

    else:
      print('Carrito vacio')


  else:
    menu_principal()

def menu_principal():
  ### Seleccion local
  local = seleccion_local()
  if local:
    print(local)
    print('Elige una opcion escribiendo su numero\n')
    for opcion in menuUsuario:
      print(opcion['id'], opcion['descripcion'])
    opcionElegida = int(input("Escriba un numero\n"))


    if opcionElegida == 1:
      menu_controlStock()

    elif opcionElegida == 2:
      print("---- FACTURACION -----")
      menu_facturacion(local)

def inicializador():
  print("----- INICIO SESSION -----\n")
  for opcion in menuInicio:
    print(opcion['id'], opcion['descripcion'])

  opcionElegida = int(input("Escriba un numero\n"))

  if opcionElegida == 1:
    #----------------   VALIDAR USUARIO   --------------------
    flag =False
    while not flag == True:
      datos = {}
      datos["nombre"]=input("Ingrese el nombre:\n")
      datos["mail"]=input("Ingrese el mail\n")
      datos["clave"]=stdiomask.getpass(prompt="Ingrese clave\nQue contenga una minuscula,una mayuscula y un caracter especial @ # $ %:\n",mask='*')
      datos["confirmPass"]=stdiomask.getpass(prompt="Confime la clave:\n",mask='*')
      print(datos)
      errores = val.validar_usuario(datos)
      if not errores:
        datos.pop('confirmPass')
        user=Usuario(**datos)
        user.save()
        print('Se añadió un nuevo user a la DB')
        flag=True
      else:
        for error in errores.values():
          print(error)

    inicializador()

      
  elif opcionElegida ==2:
    user = login()
    print("---  Bienvenido/a ",user.get_nombre(),"  ---")
    menu_principal()
  else:
    inicializador()
  
  
inicializador()



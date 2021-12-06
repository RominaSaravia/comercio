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
  {"id":2,"descripcion":"facturacion","acciones":["vista facturacion","Ver detalle factura","generar factura"],},
  {"id":3,"descripcion":"Session","acciones":["modificar nombre","modificar mail","cambiar clave"]}
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
        print(vista_productos())
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
  while flag == False:
    datos = {}
    datos["nombre"]=input("Ingrese usuario\n")
    datos["mail"]=input("Ingrese mail\n")
    datos["clave"]=stdiomask.getpass(prompt="Ingrese contraseña\n",mask="*")
    errores = val.validar_login(datos)

    if not errores:
      user = Usuario(**datos)
      user.set_id_fromDB()     
      print('Se logeo correctamente')
      flag = True
      return user

    print(errores)

def seleccion_local():
  print('Elija un local')
  local_elegido = {}
  flag = False
  ## --  PRINT Locales  --
  for opcion in menuLocal:
    print(opcion['id'], opcion['nombre'])

  opcionElegida = input("Escriba un numero\n")
  ## ----    SELECCION LOCAL   -------
  while flag == False:
    if opcionElegida.isdigit() == False:
      print('Debe ingresar solo numeros')
      opcionElegida = input("Vuelva a escriba un numero\n")
    elif int(opcionElegida) > len(menuLocal):
      print('El numero no corresponde a un local')
      opcionElegida = input("Vuelva a escriba un numero\n")
    elif int(opcionElegida) <= 0:
      print('NO se pueden ingresar -0- o numeros negativos\n')
      opcionElegida = input("Vuelva a escriba un numero\n")
    else:
      opcionElegida = int(opcionElegida)
      flag=True

  for local in menuLocal:
    if opcionElegida == local['id']:
      local_elegido["nombre"] = local['nombre']
      local_elegido['id'] = local['id']
      localFlag = True
      return local_elegido
    else:
      pass

###########------   MENUs  -----############

def menu_controlStock(user):
  user=user
  print("---- CONTROL STOCK -----")
  #-------- Despliegue menu acciones -------------
  menu = menuUsuario[0]['acciones']
  for accion in menu:
    print(menu.index(accion) + 1, accion)

  flag = False
  accionElegida = input("Escriba el numero de accion\n")

  while flag == False:
    if accionElegida.isdigit() == False:
      print('Debe escribir un numero')
      accionElegida = input("Vuelva a escribir el numero de accion\n")
    elif int(accionElegida) >= len(menu):
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir el numero de accion\n")
    elif int(accionElegida) <= 0:
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir el numero de accion\n")
    else:
      flag = True
      accionElegida = int(accionElegida)
  

  #--------------  Vista lista Productos  -------------
  if accionElegida == 1:
    print(vista_productos())
    menu_principal(user)

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

    menu_principal(user)
    #--------------  Registro Producto  ---------------
  
  #-------------- Registro de Producto --------------
  elif accionElegida == 3:
    registro_producto()
    menu_principal(user)

def menu_facturacion(local,user):
  print("---- FACTURACION -----")
  local = local
  user=user
  ### SELECCION ACCION
  print(' - acciones - ')
  menu_facturacion = menuUsuario[1]
  acciones = menu_facturacion['acciones']
  for i in acciones:
    print(acciones.index(i)+1,i)

  accionElegida = input("Escriba el numero de accion\n")
  flag = False
  while flag == False:
    if accionElegida.isdigit() == False:
      print('Debe ingresar un numero')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    if int(accionElegida) > len(acciones):
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    if int(accionElegida) < 0:
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    else:
      flag = True
      accionElegida = int(accionElegida)
      


  ## ------- Vista de toda la facturacion ----
  if accionElegida == 1:
    vista_facturas(local["nombre"])
    menu_principal(user)

  ## --------- Vista factura detalle --------
  elif accionElegida == 2:
    my_id = input('Introduzca el ID de la factura:\n')
    result = vista_factura_detalle(my_id)
    if result == {} or result == None:
      print('No se encontro la factura')
    else:
      print('Producto: ',result['Producto'],'Cantidad: ',result['Cantidad'],'Monto: ',result['Monto'])
    menu_principal(user)

  ## ------ Generar lista de productos de un ticket --------
  elif accionElegida == 3:
    print('\n######## Ticket ##########')
    lista_detalles = []

    carrito = generar_carrito()
    if not carrito == []:
      for producto in carrito:
        print("ID producto: ",producto.get('id_producto')," - Cantidad: ",producto.get('cantidad'))

      finalizar = input('Finalizar compra S/N')
      if finalizar.upper() == 'S':
        factura = registro_ticket(local["id"])
        print('\nTicket ID: ',factura.get_id(),'\nMedio de pago: ',factura.get_medioP(),'\n')
        if factura:
          for producto in carrito:
            producto['id_factura']=factura.get_id()
            newProducto = registro_detalle_ticket(producto)
            vista_detalle_producto( factura.get_id(), newProducto.get_id_producto() )

          print(vista_factura_final(factura.get_id()))
          menu_principal(user)
        else:
          print('Error - Menu_facturacion - Generar factura - Hubo un error en la generacion de factura')

    else:
      print('Carrito vacio')


  else:
    menu_principal(user)

def menu_principal(user):
  user = user
  ### Seleccion local
  local = seleccion_local()
  flag = False
  if local:
    print(local)
    print('Elige una opcion escribiendo su numero\n')
    for opcion in menuUsuario:
      print(opcion['id'], opcion['descripcion'])

    opcionElegida = input("Escriba un numero\n")
    while flag == False:
      if opcionElegida.isdigit() == False:
        print('Debe ser un numero')
        opcionElegida = input("Vuelva a intentarlo, escriba un numero\n")
      elif int(opcionElegida) > len(menuUsuario) :
        print('No corresponde a una opcion')
        opcionElegida = input("Vuelva a intentarlo, escriba un numero\n")
      elif int(opcionElegida) < 0:
        print('No corresponde a una opcion')
        opcionElegida = input("Vuelva a intentarlo, escriba un numero\n")
      else:
        opcionElegida = int(opcionElegida)
        flag=True

    
    if opcionElegida == 1:
      menu_controlStock(user)

    elif opcionElegida == 2:
      menu_facturacion(local,user)

    elif opcionElegida == 3:
      menu_session(user)

def menu_session(user):
  print('------ SESSION ------')
  user = user
  # ["modificar nombre","modificar mail","cambiar clave"]
  ### SELECCION ACCION
  print(' - acciones - \n')
  menu_facturacion = menuUsuario[2]
  acciones = menu_facturacion['acciones']
  for i in acciones:
    print(acciones.index(i)+1,i)

  accionElegida = input("Escriba el numero de accion\n")
  flag = False
  while flag == False:
    if accionElegida.isdigit() == False:
      print('Debe ingresar un numero')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    if int(accionElegida) > len(acciones):
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    if int(accionElegida) < 0:
      print('No corresponde a una accion')
      accionElegida = input("Vuelva a escribir un numero de accion\n")
    else:
      flag = True
      accionElegida = int(accionElegida)
  
  if accionElegida == 1:
    flag = False

    newName=input("Ingrese nuevo nombre\n")
    while flag == False:
      newName = newName.strip()
      if newName == "":
        print('Campo vacio')
        newName=input("Ingrese nuevo nombre\n")
      else:
        flag = True
        print('nombre ingresado: ',newName)
        user.set_nombre(newName)
        inicializador()

  elif accionElegida == 2:
    flag = False
    ##Elimino espacios entre caracteres

    newMail=input("Ingrese nuevo mail\n")
    while flag == False:
      newMail = newMail.strip()
      if newMail == "":
        print('Campo vacio')
        newMail=input("Ingrese nuevo mail\n")
      else:
        flag = True
        print('mail ingresado: ',newMail)
        user.set_mail(newMail)
        inicializador()

  if accionElegida == 3:
    flag = False

    newPass=input("Ingrese clave\nQue contenga una minuscula,una mayuscula y un caracter especial @ # $ %:\n")
    confirmPass=input("Ingrese nuevamnete la clave\n")

    while flag == False:
      result = val.validar_clave(newPass, confirmPass)
      if result:
        user.set_clave(newPass)
        inicializador()
      else:
        print(result.values())





def inicializador():
  print("----- INICIO SESSION -----\n")
  for opcion in menuInicio:
    print(opcion['id'], opcion['descripcion'])

  flag1 = False
  opcionElegida = input("Escriba un numero\n")
  while flag1 == False:
    if opcionElegida.isdigit() == False:
      print('Debe ingresar un numero')
      opcionElegida = input("Vuelva a intentarlo un numero\n")
    elif int(opcionElegida) > len(menuInicio):
      print('No corresponde a una opcion')
      opcionElegida = input("Vuelva a intentarlo un numero\n")
    elif int(opcionElegida) < 0:
      print('No corresponde a una opcion')
      opcionElegida = input("Vuelva a intentarlo un numero\n")
    else:
      flag1 = True
      opcionElegida = int(opcionElegida)
      

  if opcionElegida == 1:
    user = registro_usuario()
    if user != None:
      inicializador()
      
  elif opcionElegida ==2:
    user = login()
    if user != None:
      print("---  Bienvenido/a ",user.get_nombre(),"  ---")
      menu_principal(user)
  else:
    inicializador()


def registro_usuario():
    flag =False
    while not flag == True:
      datos = {}
      datos["nombre"]=input("Ingrese el nombre:\n")
      datos["mail"]=input("Ingrese el mail\n")
      datos["clave"]=stdiomask.getpass(prompt="Ingrese clave\nQue contenga una minuscula,una mayuscula y un caracter especial @ # $ %:\n",mask='*')
      datos["confirmPass"]=stdiomask.getpass(prompt="Confime la clave:\n",mask='*')
      errores = val.validar_usuario(datos)
      if not errores:
        datos.pop('confirmPass')
        user=Usuario(**datos)
        user.save()
        print('Se añadió un nuevo user a la DB')
        flag=True
        return user
      else:
        for error in errores.values():
          print(error)
  
inicializador()



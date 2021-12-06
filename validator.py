from db import dba
import base64

class Validator():
  def __init__(self):
    pass

  #producto(nombre, marca, precio, PrecioVenta, id_categoria, num_codigo, id_proveedor)
  def validar_producto(self,dicc):
    datosFinales={}
    errores={}
    caracteresEsp=["$","@","#","%"]

    def validarFloat(x):
      try:
        float(x)
        return True
      except ValueError:
        return False

    ##Elimino espacios entre caracteres
    # for x,y in dicc.items():
    #   datosFinales[x] = y.strip()

    for x,y in dicc.items():
      datosFinales[x] = y

    if datosFinales["nombre"] =='':
      errores["nombre"] = "Campo vacio"

    if datosFinales["marca"] =='':
      errores["marca"] = "Campo vacio"

    if datosFinales["num_codigo"].isdigit() == False:
      errores["num_codigo"] = "Error -> num_codigo = Contiene almenos una letra"

    if errores == {}:
      sql = "SELECT id_producto from productos WHERE num_codigo = %s"
      search = datosFinales["num_codigo"]
      val = (search,)

      dba.get_cursor().execute(sql,val)
      result = dba.get_cursor().fetchone()

      if result is not None:
        errores["num_codigo"] = "El codigo del producto ya esta en uso"
        return errores
      
    return errores

  def validar_usuario(self,dicc):
    datosFinales={}
    errores={}
    caracteresEsp=["$","@","#","%"]

    ##Elimino espacios entre caracteres
    for x,y in dicc.items():
      datosFinales[x] = y.strip()

    if datosFinales["nombre"] =='':
      errores["nombre"] = "Campo vacio"

    if datosFinales["mail"] =='':
      errores["mail"] = "Campo vacio"

    if len(datosFinales["clave"]) <6:
      errores["clave"] = "La clave debe contener mas de 6 caracteres"
    elif datosFinales['clave']=='':
      errores["clave"] = "Campo vacio"
    elif not any(i.isupper() for i in datosFinales['clave']):
      errores['clave'] = 'Debe contener almenos una mayuscula'
    elif not any(i.islower() for i in datosFinales['clave']):
      errores['clave'] = 'Debe contener almenos una minuscula'
    elif not any(i.isdigit() for i in datosFinales['clave']):
      errores['clave'] = 'Debe contener almenos un numero'
    elif not any(i in caracteresEsp for i in datosFinales['clave']):
      errores['clave'] = 'Debe contener almenos un caracter especial'
    elif datosFinales['clave'] != datosFinales['confirmPass']:
      errores['clave'] = 'No coincide clave y confirmacion de clave'

    if errores == {}:
      sql = "SELECT id_usuario from usuarios WHERE mail = %s"
      val = (datosFinales["mail"],)

      dba.get_cursor().execute(sql,val)
      result = dba.get_cursor().fetchone()

      if result is not None:
        errores["mail"] = "El mail ya esta en uso"
        return errores

    return errores

  def validar_login(self, dicc):
    errores={}
    datosFinales={}
    for x,y in dicc.items():
      datosFinales[x]=y.strip()

    sql= "select * from usuarios where mail=%s"
    val=(datosFinales['mail'],)
    dba.get_cursor().execute(sql,val)
    result=dba.get_cursor().fetchone()
    print('Buscando en la base')

    clave = result[3]
    a = result[3].decode('utf-8')
    aDecode = base64.b64decode(a)

    if result is None:
      errores['mail']="el Mail ingresado no existe en la base"
      return errores
    
    if (aDecode.decode('utf-8')) == datosFinales['clave']:
      print('clave confirmada')
      return
    else:
      errores["clave"]="la clave es incorrecta"

  def validar_detalle_factura(self,dicc):
    datosFinales=dicc
    errores={}

    ##Elimino espacios entre caracteres
    # for x,y in dicc.items():
    #   datosFinales[x] = y.strip()

    if  datosFinales["id_producto"] == None:
      errores["id_producto"] = "Campo vacio"

    if  datosFinales["cantidad"] == None:
      errores["cantidad"] = "Campo vacio"

    if  datosFinales["id_factura"] == None:
      errores["id_factura"] = "Campo vacio"


    if errores == {}:
      sql = "SELECT id_producto,id_factura from facturadetalle WHERE id_factura = %s AND id_producto=%s"
      val = (datosFinales["id_factura"], datosFinales["id_producto"],)

      dba.get_cursor().execute(sql,val)
      result = dba.get_cursor().fetchone()

      if result is not None:
        errores["id_producto"] = "Los productos no se pueden repetir"
        return errores

    return errores

  def validar_clave(self,clave,confirmPass):
    errores={}
    caracteresEsp=["$","@","#","%"]

    if len(clave) < 6:
      errores["clave"] = "La clave debe contener mas de 6 caracteres"
    elif clave=='':
      errores["clave"] = "Campo vacio"
    elif not any(i.isupper() for i in clave):
      errores['clave'] = 'Debe contener almenos una mayuscula'
    elif not any(i.islower() for i in clave):
      errores['clave'] = 'Debe contener almenos una minuscula'
    elif not any(i.isdigit() for i in clave):
      errores['clave'] = 'Debe contener almenos un numero'
    elif not any(i in caracteresEsp for i in clave):
      errores['clave'] = 'Debe contener almenos un caracter especial'
    elif clave != confirmPass:
      errores['clave'] = 'No coincide clave y confirmacion de clave'

    if errores == {}:
      return
    else:
      return errores


  def validar_factura(self,dicc):
    print('Validando datos')
    datosFinales=dicc
    errores={}

    ##Elimino espacios entre caracteres
    # for x,y in dicc.items():
    #   datosFinales[x] = y.strip()


    if datosFinales["fecha"] =='':
      errores["fecha"] = "Campo vacio"

    if datosFinales["medioDePago"] =='':
      errores["medioDePago"] = "Campo vacio"

    if datosFinales["id_local"] == 0 :
      errores["id_local"] = "NO se designo un local"


    if errores == {}:
      sql = "SELECT fecha,id_local from factura WHERE fecha = %s AND id_factura = %s"
      val = (datosFinales["fecha"],datosFinales["id_local"],)

      dba.get_cursor().execute(sql,val)
      result = dba.get_cursor().fetchone()

      if result is not None:
        errores["fecha"] = "Error en la fecha - No puede imprimir 2 tickets con 1 misma fecha"
        return errores

    return errores


val=Validator()

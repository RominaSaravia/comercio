from db import dba

class local():
  def __init__(self,nombre,numEmpleados,nombreEncargado,id_Barrio,controlStock):
    self.nombre=nombre
    self.numEmpleados=numEmpleados
    self.nombreEncargado=nombreEncargado
    self.__id_Barrio=id_Barrio
    self.controlStock=controlStock
    self.lista_facturas=[]
    self.__id=0

  def get_id(self):
    return self.__id
  def get_nombre(self):
    return self.nombre
  def get_numEmpleados(self):
    return self.numEmpleados
  def get_nombreEncargado(self):
    return self.nombreEncargado

  def get_facturacion(self):
    return self.lista_facturas
  def get_controlStock(self):
    return self.controlStock

  def set_id(self,new_id):
    self.__id=new_id


#########  STOCK  ###########

class controlStock():
  def __init__(self,nombre):
    self.nombre=nombre
    self.__lista_productos=[]
    self.__id=0

  def get_lista_productos(self):
    return self.__lista_productos

  def set_new_producto(self,new_product):
    self.__lista_productos.append(new_product)

  def set_lista_productos(self):
    sql='SELECT nombre ,producto,categoria,UM,cantidad FROM vista_controlstock WHERE nombre = (SELECT nombre FROM locales WHERE id_local = 1)'
    dba.get_cursor().execute(sql)
    for i in dba.get_cursor().fetchall():
      producto = {"detalle":i[1],"rubro":i[2],"UM":i[3],"cantidad":i[4]}
      self.set_new_producto(producto)

  
  def set_id(self,new_id):
    self.__id=new_id

  def set_cantidad(self,id_producto,new_cantidad,id_local):
    sql='UPDATE controlStock SET cantidad = %s WHERE id_producto = %s AND id_local = %s'
    val = (new_cantidad,id_producto,id_local)
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

from db import dba

class Factura():
  def __init__(self,fecha,medioDePago,id_local):
    self.__fecha=fecha
    self.__medioDePago=medioDePago
    self.__id_local=id_local
    self.__id=0

  def get_fecha(self):
    return self.__fecha

  def get_id_local(self):
    return self.__id_local

  def get_medioP(self):
    return self.__medioDePago

  def get_id(self):
    return self.__id


  def set_id(self,new_id):
    self.__id=new_id


  #######\\CREATE & DELETE en la DBA//#########
  
  def save(self):

    sql='insert into factura(fecha,medioDePago,id_local) VALUES(%s,%s,%s)'
    val=(self.get_fecha(),self.get_medioP(),self.get_id_local())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
    self.set_id(dba.get_cursor().lastrowid)

  def delete(self):
    sql = 'DELETE from factura WHERE id_factura = %s'
    val=(self.get_id(),)
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()


##### ------------------------------------------------#####

class FacturaDetalle():
  def __init__(self,id_producto,cantidad,id_factura):
    self.id_producto=id_producto
    self.cantidad=cantidad
    self.id_factura=id_factura
    self.__id=0

  def get_id_producto(self):
    return self.id_producto

  def get_cantidad(self):
    return self.cantidad

  def get_id_factura(self):
    return self.id_factura

  def get_id(self):
    return self.__id

  def set_id(self,new_id):
    self.__id=new_id


  #######\\CREATE & DELETE en la DBA//#########
  
  def save(self):
    sql='insert into facturadetalle(id_producto,cantidad,id_factura) VALUES(%s,%s,%s)'
    val=(self.get_id_producto(),self.get_cantidad(),self.get_id_factura())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
    self.set_id(dba.get_cursor().lastrowid)

  def delete(self):
    sql = 'DELETE from facturadetalle WHERE id_detalle = %s'
    val=(self.get_id(),)
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
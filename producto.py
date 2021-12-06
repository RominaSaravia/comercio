from db import dba

class producto():
  def __init__(self,nombre,marca,precio,PrecioVenta,id_categoria,num_codigo,id_proveedor):
    self.__nombre=nombre
    self.__marca=marca
    self.precio_proveedor=precio
    self.precio_venta=PrecioVenta
    self.id_categoria=id_categoria
    self.__id_proveedor=id_proveedor
    self.cantidad=0
    self.num_codigo=num_codigo
    self.__id=0

  def get_nombre(self):
    return self.__nombre

  def get_marca(self):
    return self.__marca

  def get_precio(self):
    return self.precio_venta

  def get_precio_p(self):
    return self.precio_proveedor

  def get_categoria(self):
    return self.id_categoria

  def get_num_codigo(self):
    return self.num_codigo

  def get_id_p(self):
    return self.__id_proveedor

  def get_id(self):
    return self.__id

  def get_details(self):
    print(self.get_nombre(),self.get_marca(),'Precio venta: $',self.get_precio(),'codigo art:',self.get_num_codigo())


  def set_nombre(self,new_nombre):
    sql='UPDATE productos SET nombre = %s WHERE id_producto = %s'
    val = (new_nombre,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

  def set_marca(self,new_marca):
    sql='UPDATE productos SET marca = %s WHERE id_producto = %s'
    val = (new_marca,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

  def set_precioV(self,newPrecio):
    sql='UPDATE productos SET PrecioVenta = %s WHERE id_producto = %s'
    val = (newPrecio,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

  def set_id(self,new_id):
    self.__id=new_id


  def set_cantidad(self,add_cantidad):
    self.cantidad+= add_cantidad

  ########\\CREATE & DELETE en la DBA//#########
  
  def save(self):
    #(self,nombre,marca,precio,PrecioVenta,id_categoria,num_codigo,id_proveedor)
    sql='insert into productos(nombre,marca,precio,PrecioVenta,id_categoria,num_codigo,id_Proveedor) VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val=(self.get_nombre(),self.get_marca(),self.get_precio_p(),self.get_precio(),self.get_categoria(),self.get_num_codigo(),self.get_id_p())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
    self.set_id(dba.get_cursor().lastrowid)

  def delete(self):
    sql = 'DELETE from productos WHERE id_producto = %s'
    val=(self.get_id(),)
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
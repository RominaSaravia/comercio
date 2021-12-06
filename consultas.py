from db import dba
from comercio import local,controlStock 
from empleado import empleado 
from factura import Factura 
from producto import producto


## seleccionar producto por id_producto
def select_producto(ids):
  sql='SELECT id_producto,nombre,marca,precio,PrecioVenta,id_categoria,num_codigo,id_Proveedor FROM productos where id_producto=%s '
  val=(ids,)
  dba.get_cursor().execute(sql,val)
  result = dba.get_cursor().fetchall()[0]
  detalle_articulo=[]
  for i in result:
    detalle_articulo.append(i)
  
  #producto(nombre, marca, precio, PrecioVenta, id_categoria, num_codigo, id_proveedor)
  art_selected = producto(*detalle_articulo[1:])
  art_selected.set_id(detalle_articulo[0])

  return art_selected

#print(select_producto(12).get_marca())
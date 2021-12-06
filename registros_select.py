from comercio import local,controlStock 
from empleado import empleado 
from factura import Factura,FacturaDetalle
from producto import producto
from db import dba
import base64
from validator import val
from getpass import getpass
import stdiomask
from usuario import Usuario
import datetime



#----------------   CONTROL STOCK   ------------------
def select_controlStock(my_id):
  sql='SELECT id_ControlStock,nombre FROM controlstock where id_local=%s '
  val=(my_id,)
  dba.get_cursor().execute(sql,val)
  result = dba.get_cursor().fetchall()[0]
  detalle=[]
  for i in result:
    detalle.append(i)
  
  controlStock_selected = controlStock(*detalle[1:])
  controlStock_selected.set_id(detalle[0])

  return controlStock_selected


def select_local(my_id,my_controlStock):
  sql='SELECT id_local,nombre,numEmpleados,nombreEncargado,id_Barrio FROM locales where id_local=%s '
  val=(my_id,)
  dba.get_cursor().execute(sql,val)
  result = dba.get_cursor().fetchone()
  detalle_articulo=[]

  
  local_selected = local(result[1],result[2],result[3],result[4],my_controlStock)
  local_selected.set_id(result[0])

  return local_selected

# my_id=1

# my_controlStock = select_controlStock(my_id)
# my_controlStock.set_lista_productos()

# local_selected = select_local(my_id,my_controlStock)

#---SELECT todas las facturas detalle de un TICKET
def select_factura_detalle(my_id):
  sql='SELECT * FROM facturadetalle where id_factura=%s '
  val=(my_id,)
  dba.get_cursor().execute(sql,val)
  result = dba.get_cursor().fetchall()[0]
  detalle=[]
  for i in result:
    detalle.append(i)
  
  facturas_detalle = FacturaDetalle(*detalle[1:])
  facturas_detalle.set_id(detalle[0])

  return facturas_detalle



# #print(select_local(my_id, my_controlStock))
# print(local_selected.get_numEmpleados())
# print(local_selected.get_nombre())
# print(local_selected.get_nombreEncargado())
# # print(local_selected.get_controlStock().get_lista_productos())




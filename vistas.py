from db import dba


### visualizar listado de productos
def vista_productos():
  print("######### Vista productos  #########")
  sql='SELECT * FROM vista_Productos '
  dba.get_cursor().execute(sql)
  
  for i in dba.get_cursor().fetchall():
    print("ID:",i[0],"Descripcion",i[1],"- Precio venta $",i[2],"- UM ",i[3])

#vista_productos()

### total ventas segun id_local
def total_ventas(nombre):
  print("######### Vista ventas  #########")
  dba.get_cursor().callproc('Totalventas',[nombre,])
  lista_ventas=[]
  
  for i in dba.get_cursor().stored_results():
    totalVentas=i.fetchall()
    for e in totalVentas:
      venta = {"dia":e[0],"Facturacion":e[1],"num_facturas":e[2],"Observacion":e[3]}
      lista_ventas.append(venta)

  for venta in lista_ventas:
    print(venta)

  dba.get_cursor().close()
  dba.get_conexion().close()


### Visualizar facturas/tickets
#### Se le aplica un filtro por local
def vista_facturas(nombre):
  print("#########   Vista facturas   #########")
  sql='SELECT * FROM vista_ventas_locales where local_nombre = %s'
  val=(nombre,)
  dba.get_cursor().execute(sql,val)
  
  for i in dba.get_cursor().fetchall():
    print("Fecha:",i[0],'  -  ',"id_factura:",i[2],'  -  ',"Medio de pago:",i[1],'  -  ',"Monto:",i[3])

### Visualizar ticket
## Filtro por id_factura
def vista_factura_final(my_id):
  print("\n#########    TRANSACCION    #########\n")
  sql='SELECT * FROM vista_ventas_locales where id_factura = %s'
  val=(my_id,)
  dba.get_cursor().execute(sql,val)
  
  for i in dba.get_cursor().fetchall():
    print("Medio de pago:",i[1],'  -   ',"Total a Pagar: $",i[3],'\n')



### Visualizar factura detalle - Todos los productos
#### Se le aplica un filtro Id_factura
def vista_factura_detalle(id_factura):
  print('######### Vista factura detalle id: ',id_factura,'   #########')
  sql='''
  SELECT id_detalle,CONCAT(productos.nombre,space(1),productos.marca) as producto, cantidad,ROUND(productos.PrecioVenta*cantidad , 2) AS 'Monto', categoria.nombre as categoria 
  FROM facturadetalle  
  INNER JOIN productos ON facturadetalle.id_producto = productos.id_producto
  INNER JOIN categoria ON productos.id_categoria = categoria.id_categoria
  WHERE id_factura = %s
  '''
  val=(id_factura,)
  dba.get_cursor().execute(sql,val)
  
  for i in dba.get_cursor().fetchall():
    print('Producto:',i[1],'Cantidad: ',i[2],'Categria:',i[4],'Monto: ',i[3])

### Visualizar factura detalle - Retorna vista de un producto
#### Se le aplica un filtro Id_factura
def vista_detalle_producto(id_factura,id_producto):
  sql='''
  SELECT id_detalle,CONCAT(productos.nombre,space(1),productos.marca) as producto, cantidad,ROUND(productos.PrecioVenta*cantidad , 2) AS 'Monto', categoria.nombre as categoria 
  FROM facturadetalle  
  INNER JOIN productos ON facturadetalle.id_producto = productos.id_producto
  INNER JOIN categoria ON productos.id_categoria = categoria.id_categoria
  WHERE id_factura = %s AND productos.id_producto = %s
  '''
  val=(id_factura,id_producto)
  dba.get_cursor().execute(sql,val)
  
  for i in dba.get_cursor().fetchall():
    print('Producto:',i[1],'Cantidad: ',i[2],'Categria:',i[4],'Monto: $',i[3])

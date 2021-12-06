from db import dba
import base64

class Usuario():
  def __init__(self,nombre,mail,clave):
    self.__nombre=nombre
    self.__mail=mail
    self.__clave=self.__encriptClave(clave)
    self.__id=0

  def get_nombre(self):
    return self.__nombre
  def get_mail(self):
    return self.__mail
  def get_clave(self):
    return self.__clave
  def get_clearClave(self):
    return self.__desencriptClave(self.__clave)
  def get_id(self):
    return self.__id

  def __encriptClave(self,clave):
    encrypted = base64.b64encode(clave.encode('utf-8'))
    return encrypted

  def __desencriptClave(self,clave):
    return base64.b64encode(clave).decode('utf-8')

  def set_id_fromDB(self):
    sql='SELECT id_usuario from usuarios WHERE mail = %s'
    val = (self.get_mail(),)
    dba.get_cursor().execute(sql,val)
    result = dba.get_cursor().fetchone()
    self.set_id(result[0])


  
  def set_id(self,newId):
    self.__id=newId

  def setPass(self,newPass):
    self.__clave = self.__encriptClave(newPass)

  def set_mail(self,newMail):
    sql='UPDATE usuarios SET mail = %s WHERE id_usuario = %s'
    val = (newMail,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

  def set_nombre(self,newNombre):
    sql='UPDATE usuarios SET nombre = %s WHERE id_usuario = %s'
    val = (newNombre,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()

  def set_clave(self,newClave):
    clave = self.__encriptClave(newClave)
    sql='UPDATE usuarios SET nombre = %s WHERE id_usuario = %s'
    val = (clave,self.get_id())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
    self.set_clave(newClave)

  ########\\CREATE & DELETE en la DBA//#########
  
  def save(self):
    sql='insert into usuarios(nombre,mail,clave) VALUES (%s,%s,%s)'
    val=(self.get_nombre(),self.get_mail(),self.get_clave())
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
    self.set_id(dba.get_cursor().lastrowid)

  def delete(self):
    sql = 'DELETE from usuarios WHERE id_usuario = %s'
    val=(self.get_id(),)
    dba.get_cursor().execute(sql,val)
    dba.get_conexion().commit()
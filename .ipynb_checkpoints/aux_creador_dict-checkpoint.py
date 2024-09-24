import pickle

dict_i = {
 'FECHA_INSCRITO': 'datetime64[ns]',
 #'INR_IDEN_NUMERO': 'str',
 'INR_NACI_FECHA': 'datetime64[ns]',
 'INR_GRADO': 'int64',
 'GRD_NOMBRE': 'str',
 'GRD_NIVEL_ESCOLAR': 'str',
 'D_SEXO': 'str',
 'INR_RES_CIUDAD': 'int64',
 'CIU_NOMBRE': 'str',
 'INR_RES_LOCALIDAD': 'int64',
 'LOC_NOMBRE': 'str',
 'ZON_NOMBRE': 'str',
 'BAR_NOMBRE': 'str',
 'UPZ_NOMBRE': 'str',
 'INR_DISCAPACIDAD': 'int64',
 'DIT_NOMBRE': 'str',
 'TAE_NOMBRE': 'str',
 'ETN_NOMBRE': 'str',
 'INR_ES_VICTIMA': 'int64',
 'PAI_NOMBRE': 'str',
 'INE_NOMBRE_INTERNO': 'str',
 'ASIGNADO_GRADO': 'float64',
 'ASIGNADO_OPCION': 'float64',
 'ASIGNADO_DANE_SEDE': 'str',
 'ASIGNADO_DANE_IED':'str',
 'ASIGNADO_LOCALIDAD': 'str',
 'ASIGNADO_FECHA': 'datetime64[ns]'}

pickle.dump(dict_i, open("dict_inscripciones.p", "wb"))
# The Watson studio notebook cell
!pip install --upgrade pixiedust

import pixiedust

username = credentials_1["username"]
password = credentials_1["password"]
host = username + '.cloudantnosqldb.appdomain.cloud'
dbName = 'iotp_65cjsf_sensor-data_2020-03-03' # DB name, can be found on the cloudant service

pixiedust.installPackage("cloudant-labs:spark-cloudant:2.0.0-s_2.11")


cloudantdata = sqlContext.read.format("com.cloudant.spark").\
option("cloudant.host", host).\
option("cloudant.username", username).\
option("cloudant.password", password).\
load(dbName)

cloudantdata.show()
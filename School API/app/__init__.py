import pymysql
pymysql.install_as_MySQLdb()

# Desativa checagem de versão e sintaxe incompatível com MariaDB 10.4
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

BaseDatabaseWrapper.check_database_version_supported = lambda self: None
DatabaseFeatures.can_return_columns_from_insert = False
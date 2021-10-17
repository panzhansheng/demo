import sqlalchemy as db

#engine = db.create_engine('sqlite:///census.sqlite')
# "mysql+pymysql://user:pass@host_name/dbname?charset=utf8"
engine = db.create_engine('mysql+pymysql://pzs:pzs@localhost/coursedb?charset=utf8')
connection = engine.connect()
metadata = db.MetaData()
account = db.Table('course_account', metadata, autoload=True, autoload_with=engine)
query = db.select([account])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
# print first row first column
print(f'{ResultSet[0][0]}')

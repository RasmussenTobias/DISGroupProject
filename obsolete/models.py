from datetime import datetime
from arbitrageBettingSite import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql

@login_manager.user_loader
def load_user(uid):
    cur = conn.cursor()

    schema = 'users'
    id = 'uid'
    if str(uid).startswith('60'):
        schema = 'users'        

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(uid))

    cur.execute(user_sql, (int(uid),))
    if cur.rowcount > 0:
        # return-if svarer til nedenstående:
    		# if schema == 'employees':
    		#   return Employees(cur.fetchone())
    		# else:
    		#   return Customers(cur.fetchone())

        return Users(cur.fetchone()) if schema == 'users' else Users(cur.fetchone())
    else:
        return None
    
class Users(tuple, UserMixin):
    def __init__(self, userData):
        self.uId = userData[0]
        self.name = userData[1]
        self.surname = userData[2]
        self.accessType = userData[3]

    def get_id(self):
        return (self.uId)
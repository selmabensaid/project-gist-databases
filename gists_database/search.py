
from .models import Gist
import sqlite3

def search_gists(db_connection, github_id=None, created_at=None):
    
    if (github_id!= None and  created_at==None) :
        cursor=db_connection.execute(('select * from gists where github_id=:github_id'),{'github_id':github_id})
    elif (created_at!=None and github_id==None):
        cursor=db_connection.execute(('select * from gists where datetime(created_at)== datetime(:created_at)'),{'created_at':created_at})
    elif (github_id and created_at):
        cursor=db_connection.execute(('select * from gists where github_id=:github_id and datetime(created_at)==datetime(:created_at)'),{'github_id':github_id, 'created_at':created_at })
    else:
        cursor=db_connection.execute(('select * from gists'))
    gists_data= cursor.fetchall()
    return [Gist(gist) for gist in gists_data]

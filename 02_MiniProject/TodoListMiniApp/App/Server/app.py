from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import json
import datetime

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (config.db_username, config.db_password, config.db_host, config.db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.flask_secret

api = Api(app)

db = SQLAlchemy(app)

class TaskTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.Text)
    complete = db.Column(db.Boolean)
    add_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<TaskTable id=%i title=%s>' % (self.id, self.title)

    @staticmethod
    def getColumns():
        return [column.key for column in TaskTable.__table__.columns]
        
    def toJSON(self):
        return {'id' : self.id, 'title' : self.title, 'description' : self.description, 'complete' : self.complete, 'add_time' : str(self.add_time)}


# A Testing REST API
class Test(Resource):
    def get(self):
        return {'Test' : 'It works!'}
    
    def post(self):
        send = request.get_json()
        return {'Info Send' : send}

#   Task API Example:   
#
#   {
#       'id' : 0
#       'title' : 'task title as a string' ,
#       'description' : 'task description as a string' ,
#       'complete' : [True or False] ,
#       'add-time' : 'datetime'
#   }
#
class Task(Resource):
    # Getting Task Data From database
    def get(self):
        # json received from get request
        receive = request.get_json()
        

        all_tasks = list(map(lambda x: x.toJSON(), TaskTable.query.all()))
        return {'Tasks' : all_tasks}
    
    # Adding Task Data To Database
    def post(self):
        # json received from post request
        receive = request.get_json()

        # filter the received json to ensure that only the valid info can be added to the database
        valid_receive_dict = {}
        for key, value in receive.items():
            if key in ['title', 'description', 'complete']:
                valid_receive_dict[key] = value
        
        # add received json to database
        if len(valid_receive_dict) > 0:
            valid_receive_dict['add_time'] = str(datetime.datetime.now())
            signature = TaskTable(**valid_receive_dict)
            db.session.add(signature)
            db.session.commit()

            return {'Success' : True, 'Inserted-Data' : signature.toJSON()}
        
        return {'Success' : False, 'Message' : 'No valid data was sent from the post request'}

api.add_resource(Test, '/')
api.add_resource(Task, '/task')

if __name__ == "__main__":
    app.run(debug=True, port=8080)

    

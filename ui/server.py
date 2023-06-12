from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
from db import query_db







app = Flask(__name__)
CORS(app)

@app.route('/', methods=["POST","OPTIONS"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def getData():
    if request.method=="OPTIONS":
        response = jsonify()
        
        return response

    data = request.get_json()
    # Process the data and return a response
   # return data["query"]
    
        

    return query_db(data["query"])["matches"]




if( __name__ =='__main__'):
    app.run(debug=True)
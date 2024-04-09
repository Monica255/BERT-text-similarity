from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
# import requests
import text_similarity
import preprocess

url = "https://flask-heroku3-8ee949830100.herokuapp.com/api"

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.json
            text = data.get('text', 'Default Text')
            print(text)
            
            data2 = {"text": text}
            
            preprocessed_text =  preprocess.preprocess_text(data2['text'])
            conf, post_id, title, thread, img = text_similarity.getData(preprocessed_text)

            if isinstance(img, str):
                return {
                'confidence': conf,
                'question': text,
                'preprocessed_text': preprocessed_text,
                'id': post_id,
                'title': title,
                'thread': thread,
                'img': img
            }, 200
            else:          
                return {
                'confidence': conf,
                'question': text,
                'preprocessed_text': preprocessed_text,
                'id': post_id,
                'title': title,
                'thread': thread
            }, 200

        except Exception as error:
            return {'error': str(error)}, 500

api.add_resource(GetPredictionOutput,'/get')

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 4000))
#     app.run(host='0.0.0.0', debug=True,port=port)
#     app.run(port=port)

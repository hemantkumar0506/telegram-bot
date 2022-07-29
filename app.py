import requests
from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def get_gpt_response(text):

    r = requests.post(
        url="https://hf.space/embed/singh5587/gpt-j-6b/+/api/predict ",
        json={"data": [text]},
    )
    response = r.json()
    return response["data"][0]


get_gpt_response('hello')



if __name__ == "__main__":
    app.run()
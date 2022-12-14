from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import cross_origin
import os

from email_sender import EmailSender
from json_responder import JsonResponse

load_dotenv()

FRONTEND_DOMAIN = os.environ.get('FRONTEND_DOMAIN')
app = Flask(__name__)


""" Email configuration """
Email_Sender = EmailSender(app)

""" JsonResponds for json and status """
JsonResponder = JsonResponse(app)

""" ROUTES """
@app.route("/email", methods = ['POST'])
@cross_origin(origins=[FRONTEND_DOMAIN])
def index():
    data = request.get_json()

    name =  data.get("name", "unknow")
    email =  data.get("email", "unknow")
    subject = data.get("subject", "unknow")
    user_message = data.get("message", "unknow")

    try:
        Email_Sender.send_email(name, email, subject, user_message)
    except:
        return JsonResponder.Response({"ERROR":"We couldn't send your email"}, status=500)

    return JsonResponder.Response({"Success":"I have received your email"}, status=200)

if __name__ == '__main__':
   app.run(debug = True, port=os.getenv("PORT", default=5000))
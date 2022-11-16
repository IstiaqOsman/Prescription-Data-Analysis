from flask import Blueprint
from queryservices.q1 import q1api
from queryservices.q10 import q10api
from queryservices.q2 import q2api
from queryservices.q3 import q3api
from queryservices.q4 import q4api
from queryservices.q5 import q5api
from queryservices.q6 import q6api
from queryservices.q7 import q7api
from queryservices.q9 import q9api

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/q1', view_func=q1api.as_view("Get REGION WISE Sales"))
query_api.add_url_rule('/q2', view_func=q2api.as_view("WHICH REGION HAS MOST SALES MONTHLY"))
query_api.add_url_rule('/q3', view_func=q3api.as_view(" Which chemical substance is used most monthly?"))
query_api.add_url_rule('/q4', view_func=q4api.as_view("Which organization sold most medicine monthly?"))
query_api.add_url_rule('/q5', view_func=q5api.as_view("What medicines are prescribed the most? What types of medicine need to be available more"))
query_api.add_url_rule('/q6', view_func=q6api.as_view("WHICH STP_CODE HAS MOST NUMBER OF ORGANISATION"))
query_api.add_url_rule('/q7', view_func=q7api.as_view("WHICH STP_CODE HAS least ORGANISATIONS BUT MOST SALES"))
query_api.add_url_rule('/q9', view_func=q9api.as_view("hello"))
query_api.add_url_rule('/q10', view_func=q10api.as_view("HI"))
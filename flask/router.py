from flask import Blueprint
from services.s1 import Query1API
from services.s2 import Query2API
from services.s3 import Query3API
from services.s4 import Query4API
from services.s5 import Query5API
from services.s6 import Query6API
from services.s7 import Query7API
from services.s8 import Query8API
from services.s9 import Query9API
from services.s10 import Query10API

query_api1 = Blueprint('queryapi1', __name__)
query_api2 = Blueprint('queryapi2', __name__)
query_api3 = Blueprint('queryapi3', __name__)
query_api4 = Blueprint('queryapi4', __name__)
query_api5 = Blueprint('queryapi5', __name__)
query_api6 = Blueprint('queryapi6', __name__)
query_api7 = Blueprint('queryapi7', __name__)
query_api8 = Blueprint('queryapi8', __name__)
query_api8 = Blueprint('queryapi8', __name__)
query_api9 = Blueprint('queryapi9', __name__)
query_api10 = Blueprint('queryapi10', __name__)

query_api1.add_url_rule('/q1',view_func = Query1API.as_view(""))
query_api2.add_url_rule('/q2',view_func = Query2API.as_view(""))
query_api3.add_url_rule('/q3',view_func = Query3API.as_view(""))
query_api4.add_url_rule('/q4',view_func = Query4API.as_view(""))
query_api5.add_url_rule('/q5',view_func = Query5API.as_view(""))
query_api6.add_url_rule('/q6',view_func = Query6API.as_view(""))
query_api7.add_url_rule('/q7',view_func = Query7API.as_view(""))
query_api8.add_url_rule('/q8',view_func = Query8API.as_view(""))
query_api9.add_url_rule('/q9',view_func = Query9API.as_view(""))
query_api10.add_url_rule('/q10',view_func = Query10API.as_view(""))

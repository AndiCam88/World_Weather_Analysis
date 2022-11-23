
#deppendencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# set up dataae enginge
engine = engine = create_engine("sqlite:///hawaii.sqlite")

# reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session
sesstion = Session(engine)

# define flask app 
app = Flask(__name__)


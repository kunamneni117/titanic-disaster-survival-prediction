import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from classification_model import __version__ as model_version
from classification_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings
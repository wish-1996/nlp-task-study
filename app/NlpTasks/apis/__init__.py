from flask import Blueprint
from app_logging import get_logger
logger = get_logger()
apis = Blueprint('NlpTasks', __name__)

from . import total_tasks

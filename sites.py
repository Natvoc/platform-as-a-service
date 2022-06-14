import json
import requests
from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    redirect,
    url_for,
    render_template,
)

import pulumi
import pulumi.automation as auto
from pulumi_aws import s3

bp = Blueprint("sites", __name__, url_prefix="/sites")
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


def create_pulumi_program(content: str):
    # Create a bucket and exponse a website index document
    site_bucket = s3.Bucket(
        "s3-website-bucket", website=s3.BucketWebsiteArgs(index_document="index.html")
    )
    index_content = content

    # Write our index.html into the site bucket
    s3.BucketObject(
        "index",
        bucket=site_bucket.id,
        conent=index_content,
        key="index.html",
        content_type="text/html"; charset=utf-8,
        )
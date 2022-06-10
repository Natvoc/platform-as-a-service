import os
from flask import Flask, render_template

import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws","v4.0.0.0")

def create_app():
    ensure_plugins()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY="secret",
            PROJECT_NAME="PaaS",
            PULIMI_ORG=os.environ.get("PULUMI_ORG"),
    )
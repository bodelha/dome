from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/docs"
API_SPEC_PATH = "/static/openapi.yml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_SPEC_PATH,
    config={"app_name": "My API"}
)

static_files_blueprint = Blueprint("static", __name__)

@static_files_blueprint.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("docs", filename)

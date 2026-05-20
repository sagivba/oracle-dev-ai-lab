from flask import Blueprint, jsonify

from oracle_ai_lab.services.example_service import get_health_status

api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health():
    return jsonify(get_health_status())

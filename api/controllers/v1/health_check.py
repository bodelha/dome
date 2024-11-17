from db import Database
from schema import HealthCheckSchema
from flask import jsonify

def health_check():
    db = Database()
    db_status = "unhealthy"

    try:
        db.connect()
        db.execute("SELECT 1;")
        db_status = "healthy"
    except Exception as e:
        db_status = "unhealthy"
    finally:
        db.close()

    response_data = {
        "status": "ok" if db_status == "healthy" else "degraded",
        "database": db_status,
        "message": "API is running",
    }

    schema = HealthCheckSchema()
    result = schema.dump(response_data)

    return jsonify(result), 200 if db_status == "healthy" else 503
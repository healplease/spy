from app import app

@app.context_processor
def inject_debug():
    return dict(debug=app.config.get('DEBUG', False))
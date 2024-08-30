from flask import render_template
from app import app
from app.monitoring import get_system_metrics

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    metrics = get_system_metrics()
    return render_template('status.html', metrics=metrics)

@app.route('/report')
def report():
    # Sample static report data for demonstration
    return render_template('report.html', report="Sample Report Data")


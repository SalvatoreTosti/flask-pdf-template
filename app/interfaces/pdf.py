from app import app
from flask import render_template, make_response, request
import pydf

@app.route('/generate-pdf')
def generate_jacket():
    rendered = render_template('example_pdf.html', items=request.args)
    try:
        pdf = pydf.generate_pdf(rendered)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        return response
    except:
        return rendered
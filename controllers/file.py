from flask import jsonify, send_file
from services.convert_pdf_to_txt import pdf_to_txt_service

def pdf_to_txt_controller(request):
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    
    files = request.files.getlist('files[]')

    errors, success = pdf_to_txt_service(files)

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 201
        return resp and send_file('APIResults.zip', mimetype = 'zip', as_attachment = True)
    if success:
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp and send_file('APIResults.zip', mimetype = 'zip', as_attachment = True)
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
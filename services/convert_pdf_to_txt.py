from flask import jsonify, send_file
from fitz.__main__ import gettext
from models.archivo import Archivo
from werkzeug.utils import secure_filename
import os, shutil, zipfile

ALLOWED_EXTENSIONS= ['pdf','txt','xlsx']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_txt_service(files):
    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('input', filename))
            success = True
            gettext(Archivo('input/'+filename))
            source = 'input/'+filename.replace('.pdf','.txt')
            shutil.copy(source, 'output')
            os.remove(source)
        else:
            errors[file.filename] = 'File type is not allowed'

    zipfolder = zipfile.ZipFile('APIResults.zip','w', compression = zipfile.ZIP_STORED)
    for root,dirs, files in os.walk('output/'):
        for file in files:
            zipfolder.write('output/'+file)
    zipfolder.close()

    return errors, success
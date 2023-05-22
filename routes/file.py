from flask import Blueprint, request
from controllers.file import pdf_to_txt_controller

file_route = Blueprint('file_route',__name__)

@file_route.route('/kai-api/pdf-to-txt', methods=['POST'])
def pdf_to_txt():
    return pdf_to_txt_controller(request)
from django import forms
from aplication.attention.models import Certificado
import datetime

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ['atencion', 'tipo_certificado', 'descripcion', 'archivo_pdf']
        
        error_messages = {
            'atencion': {
                'required': "El campo atención es requerido"
            },
            'tipo_certificado': {
                'required': "El campo tipo de certificado es requerido"
            },
            'descripcion': {
                'required': "El campo descripción es requerido"
            },
            'archivo_pdf': {
                'required': "El campo archivo PDF es requerido"
            }
        }
        
        widgets = {
            'atencion': forms.Select(
                attrs={
                    "id": "id_atencion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'tipo_certificado': forms.Select(
                attrs={
                    "id": "id_tipo_certificado",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese la descripción del certificado",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": 4,
                }
            ),
            'archivo_pdf': forms.FileInput(
                attrs={
                    "id": "id_archivo_pdf",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }
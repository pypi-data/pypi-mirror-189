# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         26/01/23 9:40 PM
# Project:      CFHL Transactional Backend
# Module Name:  oasis_certs
# Description:
# ****************************************************************
from datetime import date
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError as CoreValidationError
from django.utils.translation import gettext_lazy as _
from oasis.models import Company
from oasis.models import Periods
from oasis_certs.lib.cursors import TaxCerts
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from wsgiref.util import FileWrapper
from zibanu.django.repository.lib.utils import DocumentGenerator
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.exceptions import ValidationError
from zibanu.django.rest_framework.viewsets import ViewSet
from zibanu.django.utils import CodeGenerator


class OasisCertsServices(ViewSet):
    __prefix = "oasis_certs"
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
    if settings.DEBUG:
        authentication_classes.append(authentication.TokenAuthentication)

    def wh_source(self, request) -> Response:
        """
        REST Service to generate a withholding certificate
        :param request: request object from HTTP Post.
        :return: response with status 200 if successfully
        """
        try:
            today = date.today()
            user = request.user
            default_company = settings.OASIS_DEFAULT_COMPANY
            if not hasattr(user, "profile"):
                raise ValidationError(_("The user is not registered."), code=status.HTTP_401_UNAUTHORIZED)

            if {"year"} <= request.data.keys():
                # Validate period status
                if Periods.objects.is_open(request.data.get("year")):
                    raise ValidationError(_("The period is not closed."))

                company_data = Company.objects.get_by_company_id(default_company).first()
                certificate, account_data = TaxCerts.wh_source("cert_rtf", request.data.get("year"),
                                                               user.profile.document_id)
                # Determine issue date for taxable year
                issue_date = date(request.data.get("year"), certificate.get("issue_date").month,
                                  certificate.get("issue_date").day)
                certificate["issue_date"] = today if today <= issue_date else issue_date
                template_name = certificate.pop("template")
                generator = CodeGenerator("generate_pdf", code_length=10)

                template_data = {
                    "company": company_data,
                    "user": user,
                    "certificate": certificate,
                    "account_data": account_data,
                    "year": request.data.get("year"),
                    "code": generator.get_alpha_numeric_code()
                }
                document = DocumentGenerator(self.__prefix)
                file_uuid = document.generate_from_template(template_name, template_data, request)
                data_return = {
                    "file_id": file_uuid
                }
            else:
                raise ValidationError(_("Data required not found"))
        except Company.DoesNotExist:
            raise APIException(msg=_("Company has not been defined."), error="The company has not data on database.",
                               http_status=status.HTTP_412_PRECONDITION_FAILED)
        except CoreValidationError as exc:
            raise APIException(msg=exc.message, error="wh_source") from exc
        except ValidationError as exc:
            raise APIException(msg=exc.detail[0]) from exc
        except Exception as exc:
            raise APIException(str(exc)) from exc
        else:
            return Response(status=status.HTTP_200_OK, data=data_return)

    def get_document(self, request) -> Response:
        try:
            user = request.user
            if "file_id" in request.data.keys():
                download_file = str(user.profile.document_id) + ".pdf"
                document = DocumentGenerator(self.__prefix)
                document_file = document.get_file(user=request.user, uuid=request.data.get("file_id"))
                file_handler = open(document_file, "rb")
                file_wrapper = FileWrapper(file_handler)
                response = Response(
                    headers={"Content-Disposition": f'attachment; filename={download_file}'},
                    content_type="application/pdf",
                )
                response.content = file_handler.read()
                file_handler.close()
            else:
                raise CoreValidationError(_("Field 'file_id' is required"))
        except ValueError as exc:
            raise APIException(msg=_("Data value error"), error=str(exc),
                               http_status=status.HTTP_412_PRECONDITION_FAILED) from exc
        except CoreValidationError as exc:
            raise APIException(msg=_("Data validation error"), error=exc.message,
                               http_status=status.HTTP_406_NOT_ACCEPTABLE) from exc
        except OSError as exc:
            raise APIException(msg=_("Document error"), error=exc.strerror,
                               http_status=status.HTTP_400_BAD_REQUEST) from exc
        except ObjectDoesNotExist as exc:
            raise APIException(msg=_("Document does not exists."), error=str(exc)) from exc
        else:
            return response

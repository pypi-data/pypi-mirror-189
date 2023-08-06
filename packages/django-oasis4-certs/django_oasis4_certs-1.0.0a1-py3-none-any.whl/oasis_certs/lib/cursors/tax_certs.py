# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         27/01/23 2:42 PM
# Project:      CFHL Transactional Backend
# Module Name:  wh_source
# Description:
# ****************************************************************
from django.core.exceptions import ValidationError
from django.db import connections
from django.utils.translation import gettext_lazy as _
from oasis_certs.models import Certificate


class TaxCerts:
    connection_name = "oasis"

    @classmethod
    def execute_query(cls, query: str, *args):
        if isinstance(query, str):
            if "%s" in query:
                if len(args) <= 0:
                    raise ValueError(_("The arguments required for the query were not received."))
            cursor = connections[cls.connection_name].cursor()
            cursor.execute(query, args)
            raw_data = cursor.fetchall()
        else:
            raise ValueError(_("The query text must be string type."))
        return raw_data

    @classmethod
    def wh_source(cls, key: str, *args) -> tuple:
        try:
            dataset = []
            certificate = Certificate.objects.get_by_key(key).values("name", "legend", "footer_text", "issue_date",
                                                                     "query_text", "template").first()
            sql_to_execute = certificate.pop("query_text")
            raw_data = cls.execute_query(sql_to_execute, *args)

            if len(raw_data) > 0:
                for data in raw_data:
                    dataset.append({
                        "account": data[0],
                        "account_name": data[1],
                        "percentage": data[2],
                        "withholding_value": data[3],
                        "base_value": data[4]
                    })
        except Certificate.DoesNotExist:
            raise ValidationError(_("The key of certificate does not exists."))
        except Exception as exc:
            raise
        else:
            return certificate, dataset

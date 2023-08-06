# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         1/02/23 21:03
# Project:      CFHL Transactional Backend
# Module Name:  admin_views
# Description:
# ****************************************************************
from django.contrib import admin


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "key", "template")
    fields = ("name", "key", "legend", "footer_text", "issue_date", "template", "query_text", "enabled")


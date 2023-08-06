# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         2/02/23 6:22
# Project:      CFHL Transactional Backend
# Module Name:  certificate
# Description:
# ****************************************************************
from zibanu.django.db import models


class Certificate(models.Manager):
    def get_by_key(self, key: str):
        return self.filter(key__exact=key, enabled__exact=True)


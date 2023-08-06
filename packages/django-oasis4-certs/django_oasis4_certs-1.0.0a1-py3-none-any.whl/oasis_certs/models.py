# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         1/02/23 15:53
# Project:      CFHL Transactional Backend
# Module Name:  models
# Description:
# ****************************************************************
import uuid
from django.utils.translation import gettext_lazy as _
from oasis_certs.lib import managers
from zibanu.django.db import models


class Certificate(models.Model):
    """
    Class model to represent certificate definition entity at database
    """
    name = models.CharField(max_length=80, blank=False, null=False, verbose_name=_("Certificate name"),
                            help_text=_("Name that appears as the title of the certificate"))
    key = models.CharField(max_length=20, blank=False, null=False, verbose_name=_("Key to call back"),
                           help_text=_("Key that identifies the certificate for its execution"))
    legend = models.TextField(blank=False, null=False, verbose_name=_("Certificate text"),
                              help_text=_("Text that goes inside the body of the certificate"))
    issue_date = models.DateField(blank=True, null=True, verbose_name=_("Issue date"), help_text=_("Issue date"))
    query_text = models.TextField(blank=False, null=False, verbose_name=_("Query text"),
                                  help_text=_("Text used to execute the query"))
    template = models.CharField(max_length=150, blank=False, null=False, verbose_name=_("Template to use"),
                                help_text=_("Template used to generate the certificate"))
    enabled = models.BooleanField(default=True, blank=False, null=False, verbose_name=_("Enabled"),
                                  help_text=_("Enabled"))
    footer_text = models.CharField(max_length=150, blank=True, null=False, verbose_name=_("Footer text"),
                                   help_text=_("Text that is located in the footer of the certificate"))

    # Default Manager
    objects = managers.Certificate()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("key",), name="UNQ_certificates_key")
        ]
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")



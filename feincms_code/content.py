from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from feincms_template_content.models import TemplateContent


@python_2_unicode_compatible
class CodeContent(TemplateContent):
    class Meta(object):
        abstract = True
        verbose_name = 'code'
        verbose_name_plural = 'codes'

    code = models.TextField(_("code"), blank=True)

    def __str__(self):
        return u"code"

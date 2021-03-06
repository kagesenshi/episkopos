# -*- coding: utf-8 -*-

"""
Created on 2016-08-19
:author: Izhar Firdaus (kagesenshi.87@gmail.com)
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import LargeBinary
from zope.interface import implements
from depot.fields.sqlalchemy import UploadedFileField

from episkopos import _
from uuid import uuid4

class Company(Content):
    """ A company content type. """
    __versioned__ = {}
    __tablename__ = 'companies'

    implements(IDefaultWorkflow)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    registration_number = Column(Unicode(100))
    uuid = Column(Unicode(50))
    type_info = Content.type_info.copy(
        name=u'Company',
        title=_(u'Company'),
        add_view=u'add_company',
        addable_to=[u'Document'],
        add_permission='episkopos.add_company',
        selectable_default_views=[
#            ("alternative-view", _(u"Alternative view")),
        ],
    )

    def __init__(self, registration_number=None, uuid=None, **kwargs):
        """ Constructor

        :param custom_attribute: A very custom attribute
        :type custom_attribute: unicode

        :param **kwargs: Arguments that are passed to the base class(es)
        :type **kwargs: see :class:`kotti.resources.Content`
        """

        super(Company, self).__init__(**kwargs)

        self.registration_number = registration_number
        self.uuid = uuid or str(uuid4())

    @property
    def in_navigation(self):
        return False

    @in_navigation.setter
    def in_navigation(self, value):
        pass


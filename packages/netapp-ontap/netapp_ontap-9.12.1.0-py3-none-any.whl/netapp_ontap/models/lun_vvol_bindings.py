r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["LunVvolBindings", "LunVvolBindingsSchema"]
__pdoc__ = {
    "LunVvolBindingsSchema.resource": False,
    "LunVvolBindingsSchema.opts": False,
    "LunVvolBindings": False,
}


class LunVvolBindingsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the LunVvolBindings object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the lun_vvol_bindings. """

    id = Size(data_key="id")
    r""" The identifier assigned to the binding. The bind identifier is unique amongst all class `vvol` LUNs bound to the same class `protocol_endpoint` LUN.


Example: 1 """

    partner = fields.Nested("netapp_ontap.models.lun_vvol_bindings_partner.LunVvolBindingsPartnerSchema", unknown=EXCLUDE, data_key="partner")
    r""" The partner field of the lun_vvol_bindings. """

    @property
    def resource(self):
        return LunVvolBindings

    gettable_fields = [
        "links",
        "id",
        "partner",
    ]
    """links,id,partner,"""

    patchable_fields = [
        "partner",
    ]
    """partner,"""

    postable_fields = [
        "partner",
    ]
    """partner,"""


class LunVvolBindings(Resource):

    _schema = LunVvolBindingsSchema

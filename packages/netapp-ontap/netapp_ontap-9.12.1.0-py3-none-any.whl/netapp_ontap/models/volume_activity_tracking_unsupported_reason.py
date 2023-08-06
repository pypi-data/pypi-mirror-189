r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["VolumeActivityTrackingUnsupportedReason", "VolumeActivityTrackingUnsupportedReasonSchema"]
__pdoc__ = {
    "VolumeActivityTrackingUnsupportedReasonSchema.resource": False,
    "VolumeActivityTrackingUnsupportedReasonSchema.opts": False,
    "VolumeActivityTrackingUnsupportedReason": False,
}


class VolumeActivityTrackingUnsupportedReasonSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the VolumeActivityTrackingUnsupportedReason object"""

    code = fields.Str(data_key="code")
    r""" If volume activity tracking is not supported on the volume, this field provides an appropriate error code.

Example: 124518405 """

    message = fields.Str(data_key="message")
    r""" If volume activity tracking is not supported on the volume, this field provides an error message detailing why this is the case.

Example: Volume activity tracking cannot be enabled on volumes that contain LUNs. """

    @property
    def resource(self):
        return VolumeActivityTrackingUnsupportedReason

    gettable_fields = [
        "code",
        "message",
    ]
    """code,message,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class VolumeActivityTrackingUnsupportedReason(Resource):

    _schema = VolumeActivityTrackingUnsupportedReasonSchema

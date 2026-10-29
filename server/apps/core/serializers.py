from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is None:
            request = self.context.get("request")
            if request:
                param = request.query_params.get("fields")
                if param:
                    fields = [f.strip() for f in param.split(",")]

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            for field_name in list(self.fields.keys() - allowed):
                self.fields.pop(field_name)


class AuditFieldsMixin:
    """
    Automatically sets creator and changer fields
    based on the authenticated user.
    """

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(changer=self.request.user)

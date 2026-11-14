from rest_framework import serializers
from rest_framework.settings import api_settings


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that supports:
    - Excluding fields via 'exclude' parameter
    - Including only specific fields via 'fields' parameter
    - Takes an additional `fields` and `exclude` via constructor argument that
    controls which fields should be displayed
    """

    _fields_cache = {}

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        inc_fields = kwargs.pop("fields", None)
        exc_fields = kwargs.pop("exclude", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        # Get the request from context
        request = self.context.get("request")
        path = request.path if request else None
        fields_param = request.query_params.get("fields") if request else None
        exclude_param = request.query_params.get("exclude") if request else None

        key = (
            self.__class__.__name__,
            path,
            fields_param,
            exclude_param,
            tuple(inc_fields) if inc_fields else None,
            tuple(exc_fields) if exc_fields else None,
        )

        if key in self._fields_cache:
            allowed, excluded = self._fields_cache[key]
        else:
            allowed = set(fields_param.split(",")) if fields_param else None
            excluded = set(exclude_param.split(",")) if exclude_param else set()

            if inc_fields is not None:
                allowed = (
                    allowed.intersection(inc_fields) if allowed else set(inc_fields)
                )

            if exc_fields is not None:
                excluded.update(exc_fields)

            self._fields_cache[key] = (allowed, excluded)

        existing = set(self.fields.keys())

        if allowed is not None:
            for field in existing - allowed:
                self.fields.pop(field, None)

        for field in excluded:
            self.fields.pop(field, None)


class GeneralSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that marks common system-managed fields
    (`id`, timestamps, `creator`, `modifier`) as read-only.
    """

    READ_ONLY_FIELDS = (
        "id",
        "date_joined",
        "date_created",
        "date_modified",
        "creator",
        "modifier",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.READ_ONLY_FIELDS:
            if field_name in self.fields:
                self.fields[field_name].read_only = True


class HyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A HyperlinkedModelSerializer that configures the `url` field automatically:
    - `view_name` defaults to `<model_name>-detail` (e.g. `course-detail`)
    - `lookup_field` defaults to `slug` if the model has one, otherwise `pk`

    Values set in `Meta.extra_kwargs` take precedence over these defaults.
    """

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        url_kwargs = extra_kwargs.setdefault(api_settings.URL_FIELD_NAME, {})
        url_kwargs.setdefault("view_name", f"{self.Meta.model._meta.model_name}-detail")
        url_kwargs.setdefault(
            "lookup_field",
            "slug" if hasattr(self.Meta.model, "slug") else "pk",
        )
        return extra_kwargs

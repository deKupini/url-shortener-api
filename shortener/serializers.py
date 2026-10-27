from rest_framework import serializers

from .models import URLMapping
from .utils import get_short_code


class URLMappingSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)
    original_url = serializers.URLField(validators=[])

    class Meta:
        model = URLMapping
        fields = ["code", "original_url", "short_url"]
        read_only_fields = ["code"]

    def create(self, validated_data):
        original_url = validated_data["original_url"]
        if URLMapping.objects.filter(original_url=original_url).exists():
            code = URLMapping.objects.get(original_url=original_url).code
        else:
            while True:
                code = get_short_code()
                if not URLMapping.objects.filter(code=code).exists():
                    break
        mapping, created = URLMapping.objects.get_or_create(
            original_url=original_url,
            code=code
        )

        request = self.context.get("request")

        mapping.short_url = request.build_absolute_uri(f"{code}")
        mapping._is_created = created

        return mapping

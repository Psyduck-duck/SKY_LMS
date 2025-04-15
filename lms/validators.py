from rest_framework.serializers import ValidationError

part_youtube_url = 'youtube.com'


def validate_youtube_url(value):
    if value and part_youtube_url not in value:
        raise ValidationError(f'сылка должна быть на ресурс {part_youtube_url}')

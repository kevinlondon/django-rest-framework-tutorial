from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
		
	def restore_object(self, attrs, instance=None):
		"""
		Create or update a new snippet instance, 
		given a dictionary of deserialized field values.

		Note: If we don't define this method, then deserializing
		data will simply return a dictionary of items.
		"""
		if not instance:
			# Create a new instance
			return Snippet(**attrs)

		# Update an existing instance
		instance.title = attrs.get('title', instance.title)
		instance.code = attrs.get('code', instance.code)
		instance.linenos = attrs.get('linenos', instance.linenos)
		instance.language = attrs.get('language', instance.language)
		instance.style = attrs.get('style', instance.style)
		return instance


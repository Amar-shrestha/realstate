from django.apps import AppConfig


class Api(AppConfig):
	name = 'api'

	def ready(self):
		import api.signals
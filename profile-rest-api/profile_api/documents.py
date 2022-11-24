from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Chat


@registry.register_document
class ChatDocument(Document):
    chat = fields.ObjectField(properties= {
        'sender': fields.TextField(),
        'receiver': fields.TextField(),
        'message': fields.TextField(),
        'timestamp': fields.TextField(),

    })    

    class Index:
        name= 'chat'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0
                    }
    class Django:
        model = Chat
        fields = [
            'sender',
            'receiver',
            'message',
            'timestamp',
            ]
from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry

"""
chat_index= Index('chat')
chat_index.settings(number_of_shards= 1,
                    number_of_replicas=0,
)

@chat_index.register_document
class ChatDocument(Document):
    chat = fields.ObjectField(properties = {
        'sender': fields.TextField(),
        'receiver': fields.TextField(),
        'message': fields.TextField(),
        'timestamp': fields.TextField(),
                                })    
    class Index:
        name = 'messages'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    class Django:
        model = Chat
        fields = [
            'sender',
            'message',
            'timestamp',
            ] """
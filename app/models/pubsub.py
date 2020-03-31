import sys
from google.cloud import pubsub_v1

def publish(project, topic, data ):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic)
    try:
        publisher.publish(topic_path, data=data)
    except:
        raise Exception(sys.exc_info()[1])
import logging
import azure.functions as func
import json, os
import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
# from .sendtoeventhub import run

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    jsonData= json.loads(myblob.read())
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://icl-demo.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Dt9H/ulEGfFdEkSR1v2IPhRs3JYpdq/iR0z6t5clqUs=", eventhub_name="nsg-demo")
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(jsonData))
    producer.send_batch("event_data_batch")
    print (jsonData)




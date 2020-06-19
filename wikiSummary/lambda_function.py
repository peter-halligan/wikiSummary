import json
import wikipedia


def lambda_handler(event, context):

    if 'entity' in event:
        entity = event['entity']
        
        res = wikipedia.summary(entity, sentences=1)

        print(f"context: {context}, event: {event}")
        print(f"Response from wikipedia API: {res}")
    
        response = {
            "statusCode": "200",
            "headers": { "Content-type": "application/json" },
            "body": json.dumps({"res": res})
        }
    else:
        response = {
            "statusCode": "400"
        }

    return response
import json
import wikipedia


def lambda_handler(event, context):
    # TODO implement
    if 'body' in event:
        body = json.loads(event['body'])
        
    entity = body['entity']
    res = wikipedia.summary(entity, sentence=1)
    
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }

    return response
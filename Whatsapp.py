import json
import requests

phone_number_id = "" # Phone number ID provided
access_token = "" # Your temporary access token
recipient_phone_number = "" # Your own phone number
    
url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    'Content-Type': 'application/json'
}

build_number = '2023.5'
build_author = 'Ivan Pettinga'

msg_body_params = [
        {
            "type": "text",
            "text": build_number
        },
        {
            "type": "text",
            "text": build_author
        }
]

data = {
    'messaging_product': 'whatsapp',
    'to': recipient_phone_number,
    'type': 'template',
    'template': {
        'name': 'build_pipeline_failure',
        'language': {
            'code': 'en'
        },
        'components': [
            {
                'type': 'body',
                'parameters': msg_body_params
            }
                
        ]
    }
}
    
response = requests.post(
    url,
    headers=headers,
    data=json.dumps(data)
)

response.ok
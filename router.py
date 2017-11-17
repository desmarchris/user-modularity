import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username = '{username}',
  password = '{password}',
  version = '2017-05-26'
)

# parent workspace id
workspace_id = ''

# input text
text = 'what is my credit score'

# send to router
response = conversation.message(
    workspace_id=workspace_id,
    message_input={
        'text': text
    }
)

print(json.dumps(response, indent=2))

# save child workspace id
child_workspace_id = response['context']['workspace_id']
print child_workspace_id

# send to child workspace
child_response = conversation.message(
    workspace_id=child_workspace_id,
    message_input={
        'text': text
    }
)

print(json.dumps(child_response, indent=2))

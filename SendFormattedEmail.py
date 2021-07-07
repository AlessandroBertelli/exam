import boto3, time
#
#   expects event parameter to contain:
#   {
#       "device_id": "32",
#       "cell": 38,
#       "notify_topic_arn": "arn:aws:sns:eu-central-1:210786020439:bertelliEmailTopic" //pescato da database
#   }
# 
#   sends a plain text string to be used in a text message
#
#      "Nella LifeThing {} è stata assunta la cella {} contenente () alle ore {}."
#   

def lambda_handler(event, context):

    # Create an SNS client to send notification
    sns = boto3.client('sns')

    # Format text message from data
    message_text = "Gentile Utente,\n\nNella LifeThing {0} è stata assunta uan medicina nela cella {1}  alle ore {2}\n\nIl Team LifeThing".format(
            str(event['device_id']),
            str(event['cell']),
            str (time.strftime("%H:%M:%S"))
        )

    # Publish the formatted message
    response = sns.publish(
            TopicArn = "arn:aws:sns:eu-central-1:210786020439:bertelliEmailTopic",
            Message = message_text,
            Subject = "LifeThing | Assunto medicinale nella cella "+str(event['cell'])
        )

    return response
    
    
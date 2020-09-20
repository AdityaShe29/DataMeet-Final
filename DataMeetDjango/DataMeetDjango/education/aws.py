import boto3
import base64
import imageio
import json
client=boto3.client('rekognition',aws_access_key_id="AKIA4PHC362UPWQYYS42",aws_secret_access_key="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",region_name="us-east-1")
emotions=["CONFUSED","HAPPY","SAD","SURPRISED"]

def get_emotion(frame):
    frame=frame.split(',')[1]
    frame=base64.b64decode(frame)
    response=client.detect_faces(
        Image={
            'Bytes':frame
        },
        Attributes=["ALL"]
    )
    
    d={"confused":0,"happy":0,"sad":0,"surprised":0}
    for each in response["FaceDetails"][0]["Emotions"]:
        if each["Type"] in emotions:
            if each["Confidence"]>=25:
                d[each["Type"].lower()]=1
            else:
                d[each["Type"].lower()]=0
    #print(list(d.values()))
    return(list(d.values()))
'''
def get_emotion(frame):
    return [1,0,1,0]'''
    
import boto3
from app.utils.config import AWS_REGION, KNOWLEDGE_BASE_ID, INFERENCE_PROFILE_ARN

bedrock_client = boto3.client(
    "bedrock-agent-runtime",
    region_name=AWS_REGION
)

def query_knowledge_base(question: str):
    response = bedrock_client.retrieve_and_generate(
        input={
            "text": question
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                "modelArn": INFERENCE_PROFILE_ARN
            }
        }
    )

    answer = response["output"]["text"]

    return {
        "answer": answer
    }
# Resume-RAGing-AWS


python -m uvicorn app.main:app --reload


                    +----------------------+
                    |      User / Client   |
                    |  (Swagger / Frontend)|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      FastAPI App     |
                    |   (/upload, /ask)    |
                    |  Currently Local     |
                    +----+------------+----+
                         |            |
                         |            |
             upload PDF  |            | ask question
                         |            |
                         v            v
          +-------------------+   +-----------------------------+
          |   S3 Input Bucket |   | Bedrock Agent Runtime API   |
          | anurag-resume-    |   | RetrieveAndGenerate         |
          | ragging           |   +--------------+--------------+
          +---------+---------+                  |
                    |                            |
                    | manual sync                |
                    v                            v
         +----------------------------+   +----------------------+
         | Bedrock Knowledge Base     |   | Inference Profile    |
         | anurag-rag-kb              |   | APAC Nova Lite       |
         | Data Source: S3            |   +----------------------+
         +-------------+--------------+
                       |
                       v
         +-----------------------------+
         | Titan Embeddings V2         |
         | Chunking + Embeddings       |
         +-------------+---------------+
                       |
                       v
         +-----------------------------+
         | OpenSearch Serverless       |
         | Vector Index                |
         +-------------+---------------+
                       |
                       v
         +-----------------------------+
         | S3 KB Storage Bucket        |
         | anurag-rag-kb-storage       |
         +-----------------------------+



# Updated target architecture

                    +----------------------+
                    |     User / Client    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     API Gateway      |
                    |  Public HTTPS API    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   AWS Lambda         |
                    |  FastAPI Backend     |
                    | (/upload, /ask)      |
                    +----+------------+----+
                         |            |
                         |            |
                         v            v
              +----------------+   +-----------------------------+
              | S3 Input Bucket|   | Bedrock Agent Runtime API   |
              +----------------+   +-----------------------------+

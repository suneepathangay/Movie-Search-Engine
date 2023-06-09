from milvus import default_server
from pymilvus import connections,utility,DataType,CollectionSchema,FieldSchema,Collection
import milvus
from embedding import text_to_vector
import re
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


default_server.start()


connections.connect(host='127.0.0.1', port=default_server.listen_port)


conn = connections.connect(host="127.0.0.1", port=19530)


field1=FieldSchema("id",DataType.VARCHAR,is_primary=True,max_length=20)
field2=FieldSchema("vector",DataType.FLOAT_VECTOR,dim=384)
field3=FieldSchema("link",DataType.VARCHAR,max_length=400)


schema=CollectionSchema(fields=[field1,field2,field3])

collection=Collection(
    name="movies",schema=schema,using='default'
)



link="https://myflixer.to/movie/polite-society-96739"

result = re.split(r'[/\?]', link)[-1]
result=re.split('-',result)
id=result[-1]
result.remove(id)
title=' '.join(result)

vector_title=text_to_vector(title)

# data=[
#     ["96739"],
#     vector_title,
#     [link]

# ]

# mr=collection.insert(data)
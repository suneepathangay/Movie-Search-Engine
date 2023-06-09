Search Engine

Previously attempting to make a general search engine. Now focusing on search engine for a popular movei streaming website. 

Created a crawler to crawl through the website and get the links for all the movies. 

Built a text to vector mebedding model to convert the the titles within the links for a 384 dimensional vector. 

Stored all 40,000 vectors in a Pinecone vector database.

Using the cosine similarity algorithm, created a function to determine the similiarty between the query vector entered by the user compared with the vectors in the database.


Future Steps:

Create a user interface for user to browse through the movies. 

Figure out a way to make the search algorithm run even faster.


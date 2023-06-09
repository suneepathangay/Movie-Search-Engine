from sentence_transformers import SentenceTransformer,util
import math


model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ['Here’s a cheffy way to cook steak that really makes the most of a good cut!',
  'These burger patties are made with ground beef and an easy bread crumb mixture.',
  'You can use any cut of beef for this sausage recipe, but a rib-eye is the best.']

sentences=['South Park','South Central','3 South','South Beach']


question = 'Park South'

##here we are converting our sentences into vectors with 384 dimensions that each represent a spefic attritubte of the phrase
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
question_embeddings = model.encode(question, convert_to_tensor=True)

#print("Question: " + question)


##using the cosine similarity algorithm to compute the similarities between the and senteces
cosine_scores = util.cos_sim(question_embeddings, sentence_embeddings)

def cosine_simialrit(vector1,vector2):
    cosine_score=util.cos_sim(vector1,vector2)
    return cosine_score



#3formula is all the embeddings for one phrase times the embeddings for the other phrase 


def text_to_vector(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding=model.encode(text,convert_to_numpy=True)
    return embedding


vector=text_to_vector("hello")

vector=text_to_vector("HELOEROER ERWQ RWEW")
print(len(vector))






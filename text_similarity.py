import numpy as np
import pandas as pd
import pickle

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('firqaaa/indo-sentence-bert-base')
# To load the embeddings later:
with open('embeddings_distilbert4.pkl', 'rb') as f:
    saved_embeddings = pickle.load(f)

def find_similar(vector_representation, all_representations, k=1):
    similarity_matrix = cosine_similarity(vector_representation, all_representations)
    similarities = similarity_matrix[0]
    if k == 1:
        max_index = np.argmax(similarities)
        return [(max_index, similarities[max_index])]
    elif k is not None:
        sorted_indexes = np.flip(similarities.argsort()[-k:][::1])
        return [(idx, similarities[idx]) for idx in sorted_indexes]

def getData(text):
    df = pd.read_excel('dataset.xlsx')
    paragraph = df.iloc[:, 3] # the first column values

    # embeddings_distilbert = model.encode(paragraph.values)  
    # # Save embeddings to a file
    # with open('embeddings_distilbert4.pkl', 'wb') as f:
    #     pickle.dump(embeddings_distilbert, f)

    # print(embeddings_distilbert[0])
    # print(saved_embeddings[0].shape)

    search_vect = model.encode([text])
    print(search_vect[0].shape)

    K = 3 # no. of paragraphs that has to be extracted
    distilbert_similar_indexes = find_similar(search_vect, saved_embeddings, K)
    print(distilbert_similar_indexes)

    output_data = []
    for index,conf in distilbert_similar_indexes:
        output_data.append([index,paragraph[index],conf])

    print(output_data[0])
    for index, paragraph, conf in output_data:
        print("Index: ",index)
        print("Paragraph:", paragraph)
        print("Confidence:", conf)
        print()

    selected_data= output_data[0]
    # Load Excel data into a DataFrame
    df2 = pd.read_excel('prepopulate data.xlsx')

    post_id = df[df['label'] == selected_data[0]]['post_id'].values[0]
    print(post_id)
    float32_object = np.float32(selected_data[2])
    confidence = float(float32_object)
    # print(confidence)
    predicted_content = df2[df2['post_id'] == post_id]['content'].values[0]
    # print(predicted_content)

    predicted_title = df2[df2['post_id'] == post_id]['title'].values[0]
    # print(predicted_title)

    img_values = df2[df2['post_id'] == post_id]['img_header'].values[0]
    # print("image",img_values)
    # print("image",len(img_values))
    # if len(img_values) > 0:
    #     img = img_values.values[0]
    #     print("a")
    # else:
    #     img = None
    #     print("b")
    return confidence,post_id,predicted_title,predicted_content,img_values

# print(getData("tungau"))
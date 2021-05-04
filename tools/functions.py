import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from scipy import spatial

# Função para leitura  dos dados e retorno de dataframe

def read_data(name_data, columns, separator):
    data = pd.read_csv(name_data, names=columns, sep=separator)
    return data

def similar_cos_user(similar, user_id, mat_item_user, u_data, n_recomend): # entradas similaridade (cos, pearson, spearman), id do item, matriz de items por usuários, dataframe com os dados dos usuários (user_id, item_id, rating), numero de recomendações
    user = user_id
    similar_dict = {}
    items_user = list(mat_item_user[user].dropna().index)
    similar_ratings = []

    for k in list(mat_item_user.columns):
        items_user2 = list(mat_item_user[k].dropna().index)
        merge_users = [x for x in items_user if x in items_user2]
        if len(merge_users)>1: # para apenas um filme em comum o resultado é nulo
            cos1 = list(mat_item_user.iloc[merge_users][user])
            cos2 = list(mat_item_user.iloc[merge_users][k])
            if similar == 'cos':
                similar_ratings.append(spatial.distance.cosine(cos1, cos2))
            elif similar == 'pearson':
                similar_ratings.append(pearsonr(cos1, cos2))
            elif similar == 'spearman':
                similar_ratings.append(spearmanr(cos1, cos2))
        else:
            similar_ratings.append(np.nan)

    similar_dict[user] = similar_ratings
    similar_pd = pd.DataFrame(similar_dict) # Retorna o dataframe de similaridade do cosseno para o usuário informado

    top_similar = similar_pd[user].sort_values()[1:n_recomend+1] # o id do usuário é o index + 1

    # lista dos 5 usuários mais similares
    top_similar_user = list(top_similar.index)

    items = []

    for i in top_similar_user:
        aux = list(mat_item_user[i+1].dropna().index) # lista de filmes do usuaŕio similar i
        for k in range(len(aux)):
            if aux[k] not in items:
                items.append(aux[k])

    user_movies = list(u_data[(u_data['user_id']==user)]['item_id']) # lista de filmes assistidos pelo usuário

    items_rec = [x for x in items if x not in user_movies] # lista de filmes para rankear e recomendar ao usuário

    rank = {}

    for i in items_rec:
        aux = mat_item_user.iloc[i+1].mean() # média do filme
        rank[i+1] = aux
    rank_pd = pd.DataFrame(rank, index=['nota']).T  # Dataframe com os filmes e notas médias

    rank_pd = rank_pd.sort_values(by='nota', ascending=False)[0:n_recomend+1]
    rank_pd.index.name = 'Item'

    return print(f'Usuários similares a você recomendam os seguintes filmes:\n{rank_pd}')

def similar_cos_item(similar, item_id, mat_item_user, n_recomend): # entradas similaridade (cos, pearson, spearman), id do item, matriz de items por usuários, numero de recomendações

    item = item_id
    similar_dict = {}

    items_user = list(mat_item_user.iloc[item-1].dropna().index) # lista de usuários que viram o fime item 1
    similar_ratings = []

    for k in list(mat_item_user.index):
        items_user2 = list(mat_item_user.iloc[k].dropna().index)
        merge_users = [x for x in items_user if x in items_user2]

        # Criar numero mínimo de items em comum (por enquanto = a 1)
        if len(merge_users)>1: # para apenas um usuário em comum o resultado é nulo
            cos1 = list(mat_item_user[merge_users].iloc[item-1])
            cos2 = list(mat_item_user[merge_users].iloc[k])

            if similar == 'cos':
                similar_ratings.append(spatial.distance.cosine(cos1, cos2))
            elif similar == 'pearson':
                similar_ratings.append(pearsonr(cos1, cos2))
            elif similar == 'spearman':
                similar_ratings.append(spearmanr(cos1, cos2))
        else:
            similar_ratings.append(np.nan)

    similar_dict[item] = similar_ratings
    similar_item_pd = pd.DataFrame(similar_dict)

    top_item_similar = similar_item_pd[item].sort_values()[1:n_recomend+1]

    top_item_dict = {}

    for i in list(top_item_similar.index):
        top_item_dict[i+1] = mat_item_user.iloc[i].mean()

    item_rank_pd = pd.DataFrame(top_item_dict, index=['nota']).T.sort_values(by='nota', ascending=False)
    item_rank_pd.index.name = 'Item'

    return print(f'Filmes similares recomendados:\n {item_rank_pd}')

    # Os usuários que viram esse filme também viram os recomendados

from gensim.models import LdaModel, LdaMulticore
import pandas as pd
import os
import numpy as np

def save_bow(texts, name):

    import json
    with open(f'./corpora/{name}.json', 'w') as filehandle:
        json.dump(texts, filehandle)

def load_bow(name):

    import json
    with open(f'./corpora/{name}.json', 'r') as filehandle:
        return json.load(filehandle)

def dataset():

        path = './database'
        query_dataframe = pd.read_csv(path+'/query_dataframe.csv')
        included_df = query_dataframe[query_dataframe['Incluído']=='Yes']
        
        df = pd.DataFrame()
        for source in os.listdir(path+'/venues'):
            if source[:-4] in included_df['SIGLA'].values:
                ven = pd.read_csv(path+'/venues/'+source)
                ven['Venue'] = source[:-4]
                df = pd.concat([df, ven], ignore_index=True, axis=0)

        def extract_month(date_string):
            try:
                first_part = date_string.split("-")
                if first_part[0].isdigit():
                    month = first_part[1].upper()[:3]
                else:
                    month = first_part[0].split()[0].upper()[:3]
                return month
            except:
                return np.nan

        def extract_year(date_string):
            try:
                first_part = date_string.split("-")
                if len(first_part) > 1:
                    year = str(2000 + int(first_part[1]))
                else:
                    year = date_string.split()[1]
                return year
            except:
                return np.nan

        # Treatment
        df.index = range(len(df))
        df['Publication Date'] = df.apply(lambda row: extract_month(row['Conference Date']) if pd.isna(row['Publication Date']) else row['Publication Date'], axis=1)
        df['Publication Date'] = df['Publication Date'].fillna(df['Early Access Date'])
        df['Publication Date'] = df['Publication Date'].apply(lambda x: str(x)[:3].upper())
        df['Publication Date'] = df['Publication Date'].apply(lambda x: str(x)[0].upper() + str(x)[1:].lower())
        df['Publication Date'] = df['Publication Date'].replace('Nan', np.nan)

        df['Publication Year'] = df.apply(lambda row: extract_year(row['Early Access Date']) if pd.isna(row['Publication Year']) else row['Publication Year'], axis=1)
        df['Publication Year'] = df['Publication Year'].astype(str)
        df['Publication Year'] = df['Publication Year'].apply(lambda x: x[:4])
        return df

def train_lda_model(corpus, id2word, K, alpha, eta, df, tfidf):

    path = f'models/lda_models/{K}_{alpha}_{eta}_{df}_{tfidf}'
    try:
        lda_model = LdaModel.load(path)
        return lda_model

    except FileNotFoundError:
        if alpha == 'auto':
            lda_model = LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=K,
                                            alpha=alpha,
                                            eta=eta,
                                            passes=20)
        else:
            lda_model = LdaMulticore(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=K,
                                            alpha=alpha,
                                            eta=eta,
                                            passes=20)
        lda_model.save(path)
        return lda_model

def Novelty(index, w, df, kullback_leibler):
    try:
        pbar.update()
        start = df['Date'][index] - relativedelta(months=1)
        end = df['Date'][index] - relativedelta(months=w)
        date = df[(df['Date'] <= start) & (df['Date'] >= end)]
        date['KLD'] = np.vectorize(kullback_leibler)(df['LDA Distribution'][index], date['LDA Distribution'])
        return date.groupby('Date')['KLD'].mean().mean()
    except:
        return np.nan
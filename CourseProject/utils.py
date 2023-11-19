import pandas as pd

def getData(round):
    data_path = '../data/'
    venue_short = 'iclr2023'
    if round == "finalRound":
        date = '20230210'
        df = pd.read_csv(f'{data_path}{venue_short}_{date}.csv')
        # add a new column called paper_index
        df['paper_index'] = df.index
        # convert the string of ratings to list
        df['ratings'] = df['ratings'].apply(lambda x: eval(x))
        # delete the rows with no ratings
        df = df[df['ratings'].apply(lambda x: len(x) > 0)]

    elif round == "firstRound":
        date = "20221105"
        df = pd.read_csv(f'{data_path}{venue_short}_{date}.csv')
        # add a new column called paper_index
        df['paper_index'] = df.index
        # convert the string of ratings to list
        df['ratings'] = df['ratings'].apply(lambda x: eval(x))
        # delete the rows with no ratings
        df = df[df['ratings'].apply(lambda x: len(x) > 0)]
        # check if all the ratings are larger than 0


    return df

if __name__ == "__main__":
    import sys
    # sys.path.append('../')
    df_firstRound = getData("firstRound")
    df_finalRound = getData("finalRound")
    print(len(df_firstRound),len(df_finalRound))
    print()
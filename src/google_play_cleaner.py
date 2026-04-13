import pandas as pd
import numpy as np

def drop_unused_cols(df, verbose):
    """
    Remove colunas não utilizadas.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame original
    verbose : bool, opcional
        Se True, imprime mensagens informando quais colunas foram removidas.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame sem as colunas desnecessárias.
    """
    logs = []
    if "App Name" in df.columns.values:
        df.drop(columns=["App Name"], inplace=True)
        if verbose:
            logs.append("Coluna 'App Name' descartada!")
    if "Installs" in df.columns.values:
        df.drop(columns=["Installs"], inplace=True)
        if verbose:
            logs.append("Coluna 'Installs' descartada!")
    if "Maximum Installs" in df.columns.values:
        df.drop(columns=["Maximum Installs"], inplace=True)
        if verbose:
            logs.append("Coluna 'Maximum Installs' descartada!")
    if "Free" in df.columns:
        df.drop(columns=["Free"], inplace=True)
        if verbose:
            logs.append("Coluna 'Free' descartada!")
    if "Currency" in df.columns:
        df.drop(columns=["Currency"], inplace=True)
        if verbose:
            logs.append("Coluna 'Currency' descartada!")
    if "Developer Website" in df.columns.values:
        df.drop(columns=["Developer Website"], inplace=True)
        if verbose:
            logs.append("Coluna 'Developer Website' descartada!")
    if "Developer Email" in df.columns.values:
        df.drop(columns=["Developer Email"], inplace=True)
        if verbose:
            logs.append("Coluna 'Developer Email' descartada!")
    if "Privacy Policy" in df.columns.values:
        df.drop(columns=["Privacy Policy"], inplace=True)
        if verbose:
            logs.append("Coluna 'Privacy Policy' descartada!")
    if "Scraped Time" in df.columns.values:
        df.drop(columns=["Scraped Time"], inplace=True)
        if verbose:
            logs.append("Coluna 'Scraped Time' descartada!")
    return df, logs

def clean_size(df, verbose):
    """
    Substitui os valores NaN da coluna 'Size' pela moda e converte os valores da coluna em 'MB'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando a conversão dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Size' convertida.   
    """
    logs = []
    if "Size" in df.columns:
        df["Size"] = df["Size"].str.lower().str.replace(",", "")
        df = df[~df["Size"].str.endswith("device", na=False)]
        moda = df["Size"].mode()[0]
        df.fillna({"Size": moda}, inplace=True)
        def convert_size(size):
            if pd.isna(size):
                return np.nan
            size = str(size)
            if size.endswith("m"):
                return float(size[:-1])
            if size.endswith("k"):
                return float(size[:-1]) / 1024
            if size.endswith("g"):
                return float(size[:-1]) * 1024
            else:
                return np.nan
        df["Size (MB)"] = df["Size"].apply(convert_size)
        df.drop(columns=["Size"], inplace=True)
        if verbose:
            logs.append(f"Size : Valores NaN substituídos pelo valor da moda '{moda}'!")
            print(f"Size : Valores da coluna convertidos para 'MB'!")
    return df, logs
    
def clean_rating(df, verbose):
    """
    Substitui todas as linhas NaN da coluna 'Rating' pelo valor da mediana.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando qual tratamento foi realizado.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Rating' tratada.
    """
    logs = []
    mediana = df["Rating"].median()
    df.fillna({"Rating": mediana}, inplace=True)
    if verbose:
        logs.append(f"Rating : Valores NaN substituídos pelo valor da mediana '{mediana}'!")
    return df, logs

def clean_rating_count(df, verbose):
    """
    Substitui os valores NaN da coluna 'Rating Count' pelo valor da mediana e converte os valores em 'int'.

    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame original
    verbose : bool, opcional
        Se True, imprime mensagens informando qual tratamento foi realizado.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Rating Count' tratada.
    """
    logs = []
    mediana = df["Rating Count"].median()
    df.fillna({"Rating Count": mediana}, inplace=True)
    df["Rating Count"] = df["Rating Count"].astype(int)
    if verbose:
        logs.append(f"Rating Count : Valores NaN substituídos pelo valor da mediana '{mediana.astype(int)}'!")
    return df, logs

def clean_minimum_installs(df, verbose):
    """
    Remove os valores NaN da coluna 'Minimum Installs' e converte os valores restantes para 'int'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Minimum Installs' tratada.   
    """
    logs = []
    df.dropna(subset=["Minimum Installs"], inplace=True)
    df["Minimum Installs"] = df["Minimum Installs"].astype(int)
    if verbose:
        logs.append(f"Minimum Installs : Valores NaN descartados!")
    return df, logs

def clean_price(df, verbose):
    """
    Renomeia a coluna 'Price' para 'Price (USD)'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Price' substituída por 'Price (USD)'.   
    """
    logs = []
    if "Price" in df.columns:
        df.rename(columns={"Price": "Price (USD)"}, inplace=True)
        if verbose:
            logs.append(f"Nome da coluna 'Price' alterado para 'Price (USD)'")
    else:
        if verbose:
            logs.append(f"Nome da coluna 'Price' alterado para 'Price (USD)'")
    return df, logs

def clean_min_android(df, verbose):
    """
    Substitui os valores NaN da coluna 'Minimum Android' pelo valor da moda e converte os valores para 'int'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Minimum Android' tratada.   
    """
    logs = []
    moda = df["Minimum Android"].mode()[0]
    df.fillna({"Minimum Android": moda}, inplace=True)
    if verbose:
        logs.append(f"Minimum Android : Valores NaN substituídos pela moda '{moda}'!")
    return df, logs

def clean_dev_id(df, verbose):
    """
    Remove os valores NaN da coluna 'Developer Id''.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando a remoção dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Developer Id' tratada.   
    """
    logs = []
    if "Developer Id" in df.columns.values:
        df.dropna(subset=["Developer Id"], inplace=True)
        if verbose:
            logs.append(f"Developer Id : Valores NaN descartados!")
    return df, logs


def clean_release(df, verbose):
    """
    Substitui os valores NaN da coluna 'Released' pelo valor da mediana e converte a coluna para 'datetime'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Released' tratada.   
    """
    logs = []
    if "Released" in df.columns.values:
        df["Released"] = pd.to_datetime(df["Released"], errors="coerce")
        mediana = df["Released"].median()
        df.fillna({"Released": mediana}, inplace=True)
        if verbose:
            logs.append(f"Released : Valores NaN substituídos pela mediana '{mediana}'!")
    return df, logs


def clean_last_updated(df, verbose):
    """
    Converte os valores da coluna 'Last Updated' para 'datetime'.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento dos dados.

    Retorno
    -------
    df : pandas.DataFrame
        DataFrame com a coluna 'Last Updated' tratada.   
    """
    logs = []
    if "Last Updated" in df.columns.values:
        df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")
        if verbose:
            logs.append("Last Updated : Valores convertidos para 'datetime'!")
    return df, logs


def df_cleaner(df, verbose):
    """
    Realiza o tratamento completo do DataFrame 'Google-Playstore.csv'

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame original.
    verbose : bool, opcional
        Se True, imprime mensagens informando o tratamento de todas as colunas.

    Retorno
    -------
    pandas.DataFrame com as colunas tratadas e status do tratamento concluído.
    """
    all_logs = []
    df = df.copy()
    steps = [drop_unused_cols, clean_size, clean_rating, clean_rating_count, clean_minimum_installs, clean_price, clean_min_android, clean_dev_id, clean_release, clean_last_updated]
    for step in steps:
        df, logs = step(df, verbose)
        all_logs.extend(logs)
        
    return df, all_logs
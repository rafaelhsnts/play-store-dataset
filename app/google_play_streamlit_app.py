import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import streamlit as st
import gdown
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.google_play_cleaner as cleaner

st.set_page_config(layout="wide")

FILE_ID_RAW = "19_TStrigv0hPwvGz-7ALGIUMBVkzcNNz"
FILE_ID_PROCESSED = "10WPRO9Jl0h3v1HFLZtLC7MyAThPe3TVD"
url_raw_drive = f"https://drive.google.com/uc?export=download&id={FILE_ID_RAW}"
url_processed_drive = f"https://drive.google.com/uc?id={FILE_ID_PROCESSED}"

@st.cache_data
def load_raw():
    output = "./src/dados/raw/play_store_app_raw_sample.csv"
    if not os.path.exists(output):
        gdown.download(url_raw_drive, output, quiet=False)
    return pd.read_csv(output)
        
@st.cache_data
def process_data(df_raw, verbose=False):
    df, logs = cleaner.df_cleaner(df_raw, verbose)
    return df, logs

st.sidebar.title("Menu")
menu = st.sidebar.radio("**Navegação**", ["Sobre os dados", "Tratamento dos dados", "Visualizações"])
if menu == "Visualizações":
    graph = st.sidebar.radio("**Analises**", ["Preço por categoria", "Preço por quantidade de instalações", "Preço entre as escolhas dos Editores", "Preço por tamanho do aplicativo", "Análise das escolhas dos Editores", "Total de Avaliação por compras e anuncios internos", "Versão do Android por tamanho do aplicativo"])

if menu == "Sobre os dados":
    st.title("Google Play Store Apps")

    st.markdown(
    """
    ## **Descrição**

    A plataforma Google Play Store, disponível em aparelhos que utilizam o sistema Android, funciona como uma loja virtual que disponibiliza aplicações e games aos usuários do sistema. A loja atua como uma espécie de curadoria que, impede que aplicativos com conteúdo malicioso sejam listados na plataforma, ao mesmo tempo que realiza a atualização automática dos aplicativos.
    
    **App Name:** Nome do aplicativo listado na plataforma da Play Store.  
    **App Id:** Código único do aplicativo listado na plataforma da Play Store.  
    **Category:** Categoria em que o aplicativo se enquadra.  
    **Rating:** Valor médio das avaliações recebidas pelo aplicativo na plataforma da Play Store.  
    **Rating Count:** Total de avaliações recebidas pelo aplicativo.  
    **Installs:** Faixa publica de instalações informada pela Play Store, representa o valor mínimo do intervalo de vezes em que o aplicativo foi instalado em algum dispositivo.  
    **Minimum Installs:** Número mínimo de vezes em que o aplicativo foi instalado em algum dispositivo.  
    **Maximum Installs:** Número máximo de vezes em que o aplicativo foi instalado em algum dispositivo.  
    **Free:** Valor booleano que informa se o aplicativo listado na Play Store é gratuito.  
    **Price:** Preço do aplicativo listado na Play Store.  
    **Currency:** Moeda em que o preço do aplicarivo é definido na Play Store.  
    **Size:** Tamanho do aplicativo, indicando o espaço de armazenamento que ele ocupa no dispositivo do usuário.  
    **Minimum Android:** Versão mínima do sistema Android instalado, necessária para a instalação do aplicativo.  
    **Developer Id:** Nome único de identificação, criado pelo desenvolvedor do aplicativo.  
    **Developer Website:** Site do desenvolvedor do aplicativo.  
    **Developer Email:** Email do desenvolvedor do aplicativo.  
    **Released:** Data em que o aplicativo foi listado na Play Store.  
    **Last Updated:** Data da última atualização disponibilizada para este aplicativo.  
    **Content Rating:** Indicador de classificação etária do aplicativo.  
    **Privacy Policy:** Política de privacidade do aplicativo.  
    **Ad Supported:** Indicador de exibição de propagandas dentro do aplicativo.  
    **In App Purchases:** Indicador da disponibilidade de compras oferecidas dentro do aplicativo.  
    **Editors Choice:** Indicador de destaque do aplicativo como Escolha dos Editores na Play Store.   
    **Scraped Time:** Data de registro da coleta destes dados na Play Store.
    """
    )
    st.info("Para a análise serão utilizadas as colunas **Price**, **Category**, **Minimum Installs**, **Editors Choice**, **Size**, **Minimum Android**, **Rating**, **Rating Count**, **Ad Supported**, **In App Purchases**")

    st.markdown("<br>", unsafe_allow_html=True)
    df_raw = load_raw()
    st.dataframe(df_raw.head(1000))

    st.markdown("""
    ## **Objetivo da Análise**

    O objetivo é analisar dados da Play Store da Google, para identificar as características dos aplicativos associadas ao seu desempenho na plataforma. As principais variáveis deste conjunto de dados são **Category**, **Rating**, **Rating Count**, **Minimum Installs**, **Free**, **Price in $**, **Minimum Android**, **Content Rating**, **Ad Supported**, **In App Purchases**, **Editors Choice**, **Size (MB)**. Serão extraídos insights que tragam informações importantes que influênciem em decisões que possam ser tomadas, a fim de melhorar a experiência do usuário.  
    
    ## **Pergunta de negócio:**  
    
    A análise será orientada pelas seguintes questões:  
    
    **Monetização**  
    
    * Categorias de aplicativos apresentam preços elevados?  
    * O preço do aplicativo influencia diretamente no número de instalações?  
    * Aplicativos mais caros costumam ser mais indicados pelos Editores?  
    * Aplicativos pagos são maiores em tamanho que aplicativos gratuitos?  
    
    **Qualidade e desempenho**  
    
    * Escolhas dos Editores recebem avaliações melhores ou são mais instalados?  
    * Aplicativos com propagandas ou compras internas são piores avaliados?  
    * Aplicativos que consomem mais memoria, exigem versões mais novas do Android?  
    
    ## **Objetivo final**  
    
    O objetivo é identificar características que permitam:  
    
    * Entender fatores associados ao sucesso de um aplicativo.  
    * Entender se a confiança na indicação da plataforma aumenta o consumo do aplicativo.  
    * Verificar tendências de evolução de hardware, e tambem o acesso dos usuarios a hardwares melhores.  
    """)

    st.markdown("""
    ## **Conclusão**  
  
    Ao final da análise, foi possível obter resultados relevantes que contribuem para a compreensão do comportamento dos aplicativos na Google Play Store.  
    Os resultados indicam que, embora a distribuição do preço entre as categorias se concentrem em valores próximos, existem valores extremos acima do intervalo interquartil, indicando a presença de aplicativos com preços significativamente mais elevados em nichos específicos. Por outro lado, não foi identificado relação relevante entre o preço e o tamanho do aplicativo, sugerindo que o preço não influência no tamanho dos aplicativos.  
    Em relação a curadoria da plataforma, aplicativos classificados como Editors Choice apresentam preços mais elevados e menor dispersão, indicando uma precificação mais consistente. Além disso, a análise do número de instalação em função do preço mostra que, preços mais elevados estão associados a menores volumes de instalações.  
    A relação entre Editors Choice e Rating não apresentou diferenças relevantes. Entretanto aplicativos destacados pela curadoria, demonstram um maior volume de instalações, indicando maior alcance e popularidade.  
    A análise das variável Ad Supported e In App Purchases em relação a variável Rating mostrou que, não há diferenças significativas entre as medianas das avaliações de aplicativos com e sem esses recursos. Contudo, a distribuição dos 50% centrais é mais consistente quando esses mecanismos de monetização estão presentes.  
    Por fim, a relação entre Minimum Android e Size indica uma tendência de aumento no tamanho dos aplicativos, à medida que versões mais recentes do sistema Android são exigidas, sugerindo maior demanda por recursos.
    """)    

if menu == "Tratamento dos dados":
    df_raw = load_raw()

    st.subheader("Valores antes do tratamento dos dados")
    st.dataframe(df_raw.isna().sum().rename("Total de nulos").sort_values(ascending=False))
    st.info(f"O DataFrame possui **{df_raw.shape[0]} linhas** e **{df_raw.shape[1]} colunas**")

    df, logs = process_data(df_raw, verbose=True)
    with st.expander("Logs de tratamento"):
        for log in logs:
            log_destacado = log.replace("'","**").replace("NaN","**NaN**")
            st.write(log_destacado)

    st.subheader("Valores após o tratamento dos dados")
    st.dataframe(df.isna().sum().rename("Total de nulos").sort_values(ascending=False))
    st.info(f"O DataFrame possui **{df.shape[0]} linhas** e **{df.shape[1]} colunas**")

if menu == "Visualizações":
    col1, col2, col3 = st.columns([1,2,1])
    df_raw = load_raw()
    df, _ = process_data(df_raw)

    if graph == "Preço por categoria":
        df2 = df[df["Price (USD)"] > 0].copy()
        cat_price = df2.groupby(["Category"])["Price (USD)"].agg(["mean", "median"]).reset_index().sort_values("mean", ascending=False)
        cat_long = cat_price.melt(id_vars="Category", value_vars=["mean", "median"], var_name="Metric", value_name="Price (USD)")
        fig = plt.figure(figsize=(8, 12))
        sns.barplot(data=cat_long, x="Price (USD)", y="Category", hue="Metric")
        plt.title("Price (USD) x Category", fontweight="bold")
        plt.legend(title="Statistic")
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Price (USD)** em relação a **Category** mostra que, entre as categorias de aplicativos, as medianas de preço são semelhantes, enquanto as médias apresentam grande variação.  
        As categorias **Dating**, **Medical** e **Business** ocupam as primeiras posições no ranking de preços médios da Play Store. Esse resultado sugere que essas áreas estão associadas a serviços especializados, funcionalidades profissionais ou modelos de monetização voltados para nichos específicos.
        """, text_alignment="justify")

    if graph == "Preço por quantidade de instalações":
        df2 = df[df["Price (USD)"] > 0].copy()
        df2 = df2[["Price (USD)", "Minimum Installs"]]
        fig = plt.figure(figsize=(10, 8))
        sns.lineplot(data=df2, x="Minimum Installs", y="Price (USD)")
        plt.title("Minimum Installs (log) x Price (USD)", fontweight="bold")
        plt.xscale("log")
        plt.xlabel("Minimum Installs (log)")
        plt.ylim(0, 10)
        plt.yticks(np.arange(0, 10, .5))
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Minimum Installs** em escala logarítmica em relação a **Price (USD)** indica que existe uma relação negativa entre o preço e número de instalações. Esse resultado sugere que aplicativos com valor de venda elevado, são adquiridos com menor frequência na loja.
        """, text_alignment="justify")

    if graph == "Preço entre as escolhas dos Editores":
        df2 = df.loc[df["Price (USD)"] > 0, ["Editors Choice", "Price (USD)"]].copy()
        fig = plt.figure(figsize=(10, 8))
        sns.boxenplot(data=df2, x="Editors Choice", y="Price (USD)")
        plt.title("Editors Choice x Price (USD - log scale)", fontweight="bold")
        plt.ylabel("Price (USD - log scale)")
        plt.yscale("log")
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variáveis **Editors Choice** em relação a **Price (USD)** em escala logarítmica mostra que, a mediana de aplicativos destacados como **Editors Choice**, é superior à dos aplicativos não destacados. Esse resultado indica que, em geral, os aplicativos selecionados pelos editores apresentam valores mais elevados na região central da distribuição.
        Além disso, a dispersão dos 50% centrais (IQR) entre os aplicativos **Editors Choice** está mais concentrada em torno da mediana, sugerindo maior consistência de preços dentro desse grupo. Em contraste, os aplicativos não destacados apresentam maior variabilidade, com uma distribuição mais dispersa e presença de valores extremamente elevados, acima do limite superior IQR.
        """, text_alignment="justify")

    if graph == "Preço por tamanho do aplicativo":
        df2 = df[["Price (USD)", "Size (MB)"]].copy()
        df2["Type"] = df2["Price (USD)"].apply(lambda x: "Free" if x == 0 else "Paid")
        fig = plt.figure(figsize=(10, 8))
        sns.boxplot(data=df2, x="Type", y="Size (MB)")
        plt.title("Type x Size (MB - log scale)", fontweight="bold")
        plt.yscale("log")
        plt.ylabel("Size (MB - log)")
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Price (USD)** redistribuída nas categorias **Free** e **Paid** alocadas na coluna **Type** em relação a **Size (MB)** em escala logarítmica indica que, a mediana de tamanho entre aplicativos gratuitos e pagos é bastante semelhante. A dispersão dos 50% centrais (IQR) também apresenta valores próximos, embora a dispersão entre os aplicativos pagos seja ligeiramente maior.  
        Esses resultados sugerem que não há diferença aparente de tamanho entre aplicativos das categorias **Free** e **Paid**. Vale considerar que, nesta base de dados, os aplicativos da categoria **Paid** representam apenas 1,9% do total, o que pode limitar a robustez dessa comparação.
        """, text_alignment="justify")

    if graph == "Análise das escolhas dos Editores":
        df2 = df[["Rating", "Rating Count", "Minimum Installs", "Editors Choice"]].copy()
        df2 = df2[df2["Rating Count"] >= 10]
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))
        sns.barplot(data=df2, x="Editors Choice", y="Rating", ax=axs[0])
        axs[0].set_title("Editors Choice x Rating", fontweight="bold")
        axs[0].set(yticks=np.arange(0, 5, step=.2))
        sns.barplot(data=df2, x="Editors Choice", y="Minimum Installs", ax=axs[1])
        axs[1].set_title("Editors Choice x Minimum Installs", fontweight="bold")
        axs[1].set(yscale="log", ylabel="Minimum Installs (log)", ylim=(10**0, 10**8))
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Editors Choice** em relação a **Rating**, indica que não há diferença aparente entre aplicativos padrão e destacados, embora estes apresentem uma pontuação ligeiramente melhor.  
        Por outro lado, ao analisar a variável **Editors Choice** em relação a **Minimum Installs** na escala logarítmica, a diferença é notável. Aplicativos destacados como **Editors Choice** apresentam volume de instalações significativamente maior, sugerindo que esse método possa influenciar na escolha do usuário, demonstrando que essa é uma excelente estratégia de negócio.
        """, text_alignment="justify")

    if graph == "Total de Avaliação por compras e anuncios internos":
        df2 = df[["Rating", "Rating Count", "Ad Supported", "In App Purchases"]].copy()
        df2 = df2[df2["Rating Count"] >= 10]
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))
        sns.boxplot(data=df2, x="Ad Supported", y="Rating", ax=axs[0])
        axs[0].set(title="Ad Supported x Rating")
        sns.boxplot(data=df2, x="In App Purchases", y="Rating", ax=axs[1])
        axs[1].set(title="In app purchases x Rating")
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Ad Supported ** em relação a **Rating** indica que, a mediana das avaliações é semelhante entre aplicativos com e sem anúncios. No entanto, aplicativos suportados por anúncios apresentam um intervalo interquartil (IQR) ligeiramente mais estreito, indicando maior consistência nas avaliações, enquanto aplicativos sem anúncios demonstram maior variabilidade.  
        De maneira similar, a análise a variável **In App Purchases** em relação a **Rating** indica medianas praticamente iguais entre os grupos. Entretanto, aplicativos que não oferecem compras internas apresentam um intervalo interquartil (IQR) ligeiramente maior, indicando maior dispersão nas avaliações, enquanto aplicativos com compras internas demonstram avaliações um pouco mais consistentes. Vale considerar que nessa base dados, aplicativos indicados com In App Purchases **True** representam apenas 8,9% dos dados, o que pode limitar a robustez da comparação.
        """, text_alignment="justify")

    if graph == "Versão do Android por tamanho do aplicativo":
        df2 = df[["Minimum Android", "Size (MB)"]].copy()
        df2["Minimum Android"] = df2["Minimum Android"].astype(str).str.extract(r"^(\d+\.\d+|\d+)")[0]
        df2.dropna(subset=["Minimum Android"], inplace=True)
        df2["Minimum Android"] = df2["Minimum Android"].astype(float)
        fig = plt.figure(figsize=(10, 8))
        sns.barplot(data=df2, x="Minimum Android", y="Size (MB)")
        plt.title("Minimum Android x Size (MB)")
        with col2:
            st.pyplot(fig)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("""
        A análise da variável **Minimum Android** em relação a **Size (MB)** indicam uma tendência de aumento no tamanho médio dos aplicativos conforme cresce a versão mínima exigida do sistema.  
        Esse comportamento sugere que aplicativos desenvolvidos para versões mais recentes do Android tendem possuir mais funcionalidades, interfaces gráficas melhoradas, e bibliotecas adicionais, resultando em um maior consumo de armazenamento.  
        Como consequência, usuários com dispositivos com sistemas defasados e capacidades de memória reduzidas, enfrentem limitações de compatibilidade de desempenho. Esses resultados reforçam a importância de estratégias de otimização e do desenvolvimento de aplicativos mais leves para ampliar a acessibilidade dos aplicativos.
        """, text_alignment="justify")
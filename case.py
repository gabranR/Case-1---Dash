import streamlit as st
import pandas as pd
import altair as alt
st.title('Case dos Atrativos de Brasília - Medidas de Tendência Central')

st.write("Esse painel é parte de um exercício feito em sala de aula para a disciplina de Fundamentos da Estatística Aplicados ao Turismo, CET/UnB.")

st.markdown("""---""")

#
df = pd.read_excel("Links_DF.xlsx")

#
st.dataframe(df)
#

st.markdown("""### Quais atrativos tem popularidade acima da média?""")

st.write("Dado pela fórmula:")

##
col1, col2 = st.columns(2)

col1.latex(r"\frac{1}{n} \sum_{i=i}^{n} x_{i} = ")

col2.metric(label = "Média", value = round(df["Num_avaliacoes"].mean(), 2))

st.dataframe(df[df.Num_avaliacoes > round(df["Num_avaliacoes"].mean(), 2)])
##

st.markdown("""---""")
st.markdown("""### Quais são os 50\% atrativos mais populares?""")

st.write(f"n = {len(df)}, logo mediana para números pares")


st.metric("Mediana",df["Num_avaliacoes"].median())

st.write("Selecionando apenas os atrativos que compõem a metade superior da amostra, temos:")

st.dataframe(df[df.Num_avaliacoes > df["Num_avaliacoes"].median()])


##
st.markdown("""---""")
st.markdown("""### Qual o atrativo mais na "moda"? :wink:""")

st.write("Essa é fácil, basta ordenar os dados e encontrar o atrativo com a maior frequência. Interaja com a tabela :point_down:")

st.dataframe(df.sort_values("Num_avaliacoes", ascending=True))


st.markdown("""---""")
st.markdown("""### Extra: A distribuição completa  	:wine_glass: """)

"\n"

st.bar_chart(df["Num_avaliacoes"])

"\n\n\n\n"

st.write("Desenvolvido por Gabriel Rangel, Mestrado Acadêmico em Administração - Estágio Docência")
import streamlit as st

st.title("🏗️Diseño óptimo de mezclas de concreto")

st.header("⚡Introducción")
st.write("El concreto es uno de los materiales más usados en la construcción. Su resistencia a la compresión depende de las cantidades de cada componente de la mezcla y de la edad a la que se ensaya.")

st.subheader("Objetivo del proyecto")
st.write("Analizar cómo influyen los componentes de la mezcla y la edad del ensayo en la resistencia a la compresión, para encontrar una mezcla de concreto óptima.")

st.header("Datos del proyecto")
st.write("Los datos provienen de ensayos de laboratorio de concreto y están guardados en un archivo CSV publicado en GitHub.")

st.subheader("Descripción del dataset")
st.write("El dataset tiene 1030 ensayos y 9 columnas: cemento, escoria, ceniza volante, agua, superplastificante, agregado grueso, agregado fino, edad (días) y resistencia a la compresión (MPa).")

# pestañas internas
tab1, tab2 = st.tabs(["Componentes de la mezcla", "Resistencia a la compresión"])

with tab1:
    st.subheader("Componentes de la mezcla")
    st.write("Cemento, escoria, ceniza volante, agua, superplastificante, agregado grueso y agregado fino. Todos se miden en kg por metro cúbico de mezcla.")

with tab2:
    st.subheader("Resistencia a la compresión")
    st.write("Es la variable que se quiere maximizar. Se mide en MPa y depende de los componentes de la mezcla y de la edad del ensayo.")
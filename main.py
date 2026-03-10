import streamlit as st

st.title("🩺 Sistema de Diagnóstico - Inteligência Artificial")
st.write("Selecione os sintomas do paciente abaixo para gerar o diagnóstico.")

col1, col2 = st.columns(2)

with col1:
    coriza = st.radio("O paciente apresenta coriza?", ["Sim", "Não"])
    tosse = st.radio("O paciente apresenta tosse?", ["Sim", "Não"])

with col2:
    manchas = st.radio("O paciente apresenta manchas na pele?", ["Sim", "Não"])
    febre = st.radio("Qual o nível de febre do paciente?", ["Alta", "Baixa", "Não"])

if st.button("Gerar Diagnóstico"):
    if manchas == "Sim":
        if febre == "Alta":
            st.error("O paciente pode estar com Dengue.")
        else:
            st.success("O paciente pode estar com Alergia.")
    else:
        if febre == "Alta":
            st.warning("O paciente pode estar com Gripe.")
        elif febre == "Não" or febre == "Baixa":
           st.info("O paciente pode estar com Resfriado.")

with st.expander("Como a Inteligência Artificial tomou essa decisão?"):
    st.write("""
    Este sistema utiliza um modelo clássico de **Árvore de Decisão**, um dos algoritmos fundamentais em Inteligência Artificial. 

    A partir de uma análise de dados históricos (tabela de regras), o algoritmo busca o caminho mais curto e eficiente para classificar uma informação. Neste caso, a IA identificou que **não é necessário analisar todos os 4 sintomas** para chegar ao resultado correto. 

    A árvore foi otimizada da seguinte forma:
    * **Nó Raiz (A primeira divisão):** O sintoma *Manchas na Pele* é o divisor principal. Ele separa os diagnósticos perfeitamente em dois grupos (Dengue/Alergia ou Gripe/Resfriado).
    * **Nós de Decisão (O desempate):** O sintoma *Febre* atua como o fator de desempate final para ambos os grupos.
    * **Otimização:** Os sintomas *Tosse* e *Coriza* foram classificados como redundantes para o diagnóstico final e descartados da lógica de decisão.

    Essa estrutura demonstra como modelos lógicos podem otimizar a triagem médica, reduzindo o número de perguntas e acelerando o diagnóstico.
    """)

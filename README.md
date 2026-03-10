# Sistema de Diagnóstico IA - Árvore de Decisão (2026)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=120&text=Diagnóstico%20Médico%20com%20IA&fontAlign=50&fontSize=34&desc=LCP%20•%20Inteligência%20Artificial%20•%20Árvore%20de%20Decisão&descAlign=50&descAlignY=70" alt="Banner IA" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&duration=4000&pause=1000&color=58A6FF&center=true&vCenter=true&width=650&lines=Inteligência+Artificial;Árvore+de+Decisão;Python+&+Streamlit" alt="Typing SVG"/>
  </a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
</p>

<p align="center">
  <img alt="Status do Projeto" src="https://img.shields.io/badge/status-concluído-green">
  <img alt="Último Commit" src="https://img.shields.io/github/last-commit/skyzinha-chan/sistema-diagnostico-ia?style=flat">
  <img alt="Licença" src="https://img.shields.io/badge/license-MIT-green">
</p>

---

## 📌 Sobre o Projeto
Este repositório contém uma aplicação web interativa desenvolvida como atividade da disciplina de **Inteligência Artificial** (Prof. Dr. Lucas Hermann Negri). 

O projeto implementa um modelo clássico de **Árvore de Decisão** para realizar triagem médica. A partir da análise de um conjunto de regras (sintomas), o algoritmo foi otimizado para classificar a doença (Gripe, Resfriado, Dengue ou Alergia) realizando o menor número possível de perguntas ao paciente.

## 🌳 Lógica da Árvore de Decisão

O diagrama abaixo ilustra a estrutura lógica otimizada pela IA, descartando sintomas redundantes (como tosse e coriza) para agilizar o diagnóstico:

```mermaid
flowchart TD
    A{Manchas na Pele?} 
    A -->|Sim| B{Tem Febre?}
    A -->|Não| C{Tem Febre?}
    
    B -->|Alta| D((Dengue))
    B -->|Não| E((Alergia))
    
    C -->|Alta| F((Gripe))
    C -->|Baixa ou Não| G((Resfriado))

    style D fill:#ff4b4b,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#00cc96,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#ffa15a,stroke:#fff,stroke-width:2px,color:#fff
    style G fill:#636efa,stroke:#fff,stroke-width:2px,color:#fff
```
---

## 🚀 Como acessar
A aplicação está hospedada na nuvem e pode ser acessada diretamente pelo navegador através do link abaixo:

## [🔗 Acessar Sistema de Diagnóstico (Streamlit)](https://sistema-diagnostico-ia.streamlit.app/)

## 🧑‍💻 Autora

<div align="center">

| Nome                        |                                                      GitHub                                                      |                                                                  LinkedIn                                                                  |                                                             Instagram                                                             |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------: |
| **Talita Mendonça Marques** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/skyzinha-chan) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/talita-mendonca-marques/) | [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram)](https://www.instagram.com/skyzinha_chan/) |

<br>

<a href="https://github.com/skyzinha-chan">
  <img src="https://github.com/skyzinha-chan.png" width="150" alt="Foto de Talita Mendonça Marques" style="border-radius: 50%;"/>
</a>

<p>
Licenciatura em Computação<br>
Instituto Federal de Mato Grosso do Sul - <b>Campus Jardim</b>
</p>

</div>

## ⚖️ Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!

_Projeto desenvolvido com ❤️ por [Talita Mendonça Marques](https://github.com/skyzinha-chan)._
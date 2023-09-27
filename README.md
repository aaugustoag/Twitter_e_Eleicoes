# Twitter e Eleições
 
 
<div align="left"> 
  <img align="center" src="https://img.shields.io/badge/Python-FF8C00?style=for-the-badge&logo=python&logoColor=grey"><br>
  <img src="https://img.shields.io/badge/Mineração%20de%20Dados-white">
  <img src="https://img.shields.io/badge/Ciência%20de%20Dados-red">
</div>

Trabalho Final de Mineração e Ciência de Dados no contexto da disciplina Aprendizado de Máquina no CEFET-MG.
## Problema e relevancia
<p align="justify">Nas eleições presidenciais de 2018, foi vista uma forte presença do uso de redes sociais como forma primária de comunicação de um dos candidatos, Jair Bolsonaro.  
<br>Essa guinada nada convencional do discurso público, da tv para redes sociais, deixou muitos analistas políticos desnorteados.
<br>Vimos assim a importância de utilizar metodologias computacionais para buscar correlações entre o discurso deste canditado em suas postagens com o aumento de sua popularidade nas pesquisas eleitorais, visto que tal metodologia poderia ser aplicada em futuras eleições para complementar a interpretação de cenários políticos.</p>

## Modelagem
- <span style="color:coral">(a) qual tarefa/problema a ser resolvido?;</span>
- <span style="color:coral">(b) o que é a instância deste problema e como ela é representada: Quais são os atributos e o que
significa a classe alvo?</span>

<p align="justify">O problema consiste em extratir dados de uma determinada rede social deste candidato, no caso o Twitter, e transformar em métricas para podermos usar um modelo de aprendizado de máquinas tentando prever a aprovação deste candidato, conforme pesquisas eleitorais, dado seu engajamento nesta rede social.
<br>Usamos como instancia um grupo de tweets pré processado em métricas numéricas limitado por intervalos de tempos definidos pelas pesquisas naquele periodo, que representam nossa classe alvo.
<br>As métricas extraidas diretamente dos dados dos tweets foram a quantidade de favoritos o tweet recebeu e a quantidade de vezes que ele foi compartilhado e as métricas modeladas foram as classes gramaticas o sentimento e a sbjetividade extraidos do texto dos tweets.</p>

<p align="justify">Desta forma o que se quer saber é:  
    
- Qual a relação entre o número de compartilhamentos e favoritos com sua performance nas pesquisas?
- Existe alguma correlação com o que o candidato escreve em seus tweets com sua performance nas pesquisas?</p>

## <span style="color:blueviolet">Análise dos dados</span>
- <span style="color:coral">Quais tipos de dados serão os atributos?</span>
- <span style="color:coral">Existem ruídos, valores inválidos ou inexistentes para algum atributo?</span>
- <span style="color:coral">Qual preprocessamento é necessário para os tipos de atributos e métodos que serão utilizados</span>

<p align="justify">Serão usados dois atributos extraidos diretamente dos tweets, quais são, favorito e compartilhado, e quatorze preprocessados a partir do texto do tweet, sentimento, subjetividade, adjetivos, adverbios de posição, adverbios, conjunções, artigos, substantivos, numerais, preposições, pronomes, verbos, pontuações e outros presentes no texto.
<br>Para extrair o sentimento, a subjetividade e a classe gramatical do texto, primeiramente passamos a linguagem para o inglês, conforme verificado no artigo "A Multilingual Benchmarking System for Sentence-Level Sentiment Analysis", para melhor classificação das métricas, e finalmente utilizamos o TextBlob para extrair as métricas.</p>  

- Existem nos sentimentos e subjetividades valores igual a zero. Estes valores podem indicar que o tweet é neutro ou que não foi classificado.  
- Os favoritos de um tweet compartilhado por outro usuário não são contabilizados e, portanto, apresentam a métrica zerado.

<p align="justify">Os dados das pesquisas eleitorais foram tratados de forma mais seletiva.  
    
- Foram extraidas as pesquisas de forma expontânea, entendendo que as mesmas conflitam com os resultados das estimuladas, da mesma forma extraimos as pesquisas de votos válidos, entendendo que estas conflitam com os resultados dos votos totais.  
- Os institutos que realizaram menos de 8 pesquisas ao longo do periodo avaliado também foram ignorados por entendermos que seriam poucos resultados para formar uma função relevante.
- Para pesquisas com diferentes cenários na mesma data, as juntamos em uma só média</p>

![image](https://github.com/aaugustoag/Twitter_e_Eleicoes/assets/49174397/ef5ef68e-eb16-4b59-b8ef-0a4f12b92562)

## <span style="color:blueviolet">Preprocessamento usado</span>
<p align="justify">O engajamento no Twitter, favoritos e compartilhamento já possuiam sua métrica própria e suficientes para o trabalho.
<br>Contudo, para melhorar a precisão, inserimos métricas que conseguissem expressar em números os textos nos tweets.
<br>O sentimento e a subjetividade poderiam medir o contexto e as classes gramaticais mediriam a forma com a qual estaria sendo realizado o engajamento.</p>

![image](https://github.com/aaugustoag/Twitter_e_Eleicoes/assets/49174397/6197eeb6-4245-4756-bc37-3a7b424fd4cc)

Acima vemos a regressão polinomial que gerou a extrapolação dos dados das pesquisas eleitorais.  
Usamos estes dados como classe alvo no nosso modelo!

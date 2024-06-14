# P2-M6-ENG_COMP
 Prova prática de engenharia da computação do Inteli 

## Atividades Desenvolvidas 
Foi criado um script em python que pega um vídeo de input e implementar o algoritmo HAAR Cascade para identificar rostos em um vídeo e a detecção de rostos é salva no vídeo *output.avi*. 

### Script 
O identificador de rostos foi criado para detectar os rostos em um vídeo 

O código pode ser acessado em: 

    video.py


## Como utilizar a solução 


1. Só basta criar a venv e instalar os requirements.

    ```console 
        python -m venv venv
        cd venv/scripts 
        activate
        pip install -r requirements.txt
    ``` 

2. Agora é só rodar o código.
    ```console 
        python video.py
    ``` 

## Demonstração dos trabalhos realizados 
Funcionamento do modelo. 

<figure class="video_container">
  <iframe src="la_cabra.mp4" frameborder="0" allowfullscreen="true"> 
</iframe>
</figure>

2.1.
Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

2.2
Considere as seguintes alternativas para resolver o problema de detecção de faces:

HAAR Cascade
CNN
NN Linear
Filtros de correlação cruzada
Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

2.3.
Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.

2.4.
A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?
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

[![Video Title](https://img.youtube.com/vi/RiTKVyZGs7Q/0.jpg)](https://www.youtube.com/watch?v=RiTKVyZGs7Q)


## Respondendo as perguntas 
#### 2.1. Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

O método de detecção implementado foi o Haar Cascade, esse método é um modelo de machine learning pré treinado para a detecção de rostos humanos. O modelo funciona da seguinte maneira, é passado uma janela flutuante por toda a imagem. Dentro dessa janela há um kernel que define com base no treinamento se há a identificação de características que definem ou não um rosto. Caso existam essas características é retornado um resultado positivo, porém se não passar na detecção de características a janela é descartada e o modelo continua aplicando as janelas em toda a imagem. 


#### 2.2 Considere as seguintes alternativas para resolver o problema de detecção de faces: HAAR Cascade, CNN, NN Linear e Filtros de correlação cruzada. 
#### Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

- HAAR Cascade
- CNN
- NN Linear
- Filtro de correlação cruzada

A escolha pela ordem foi que o HAAR Cascade é muito fácil de implementar e resolve rapidamente o problema. Além disso, é muito mais leve que uma cnn. 
A CNN é muito mais precisa que o HAAR Cascade, mas ela é mais pesada e como o problema a ser resolvido era mais simples, não foi necessário uma solução tão complexa e pesada. 




#### 2.3 Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.
- CNN
- HAAR Cascade
- Filtro de correlação cruzada
- NN Linear 

A rede neural convolucional é muito melhor para detectar emoções porque os filtros de convoluções conseguem processar inputs muito maiores e tem uma performance muito melhor. 

#### 2.4. A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?

Se o desenvolvedor quiser é possível aplicar cada frame como input e realizar a detecção de emoções com uma CNN que tenha sido treinada para essa tarefa. 
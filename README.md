# this_or_that

## Repository Link

- [GitHub](https://github.com/lisandroescalada/Esto_o_Aquello)

## Game Description

**This or That** is a fun question-and-answer game where players choose between two options. The goal is to answer as many questions correctly as possible before time runs out.

## File Structure

```text
this_or_that/
├── assets/
│   ├── fonts/
│   │   └── VT323.ttf
│   ├── images/
│   │   ├── barra.png
│   │   ├── boton_azul.png
│   │   └── ...
│   ├── sounds/
│   │   └── ...
├── data/
│   ├── preguntas.json
│   └── puntajes.csv
├── modules/
│   ├── juego.py
│   ├── utilidades.py
│   └── visuales.py
└── main.py
```

## How to Play

1. **Start Screen**  
   - When the game launches, the start screen appears. Click the **START** button to begin.  
     ![Start Screen](assets/images/inicio.png)

2. **Enter Your Name**  
   - Type your name using the keyboard and click **CONTINUE** to proceed.  
     ![Enter Name](assets/images/nombre.png)

3. **Question Screen**  
   - You will be presented with a question and two options. Click the one you think is correct.  
   - Use the **Next**, **Half**, and **Reload** lifelines to help answer questions.  
     ![Question Screen](assets/images/preguntas.png)

4. **Result Screen**  
   - After answering, you will see whether your answer was correct. Click **CONTINUE** to move to the next question.  
     ![Result Screen](assets/images/resultado.png)

5. **Game Over Screen**  
   - When the game ends, your final score and votes are displayed. Click **BACK** to return to the start screen.  
     ![Game Over Screen](assets/images/final.png)

## Gameplay Video

- [Watch Here](https://drive.google.com/file/d/1mrWutDFRWOYNK48XMKaAAuDFva95momC/view?usp=sharing)
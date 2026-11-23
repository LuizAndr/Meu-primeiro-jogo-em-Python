# Meu Primeiro Jogo em Python (Dragon Ball 2D)

> Esse arquivo foi postado com o intuito de guardar meu primeiro jogo, o codigo está bem nivel iniciante, espero no futuro reescreve-lo em uma versão 2.0 melhorada para comparar minha evolução.

## Resumo do Jogo

**Dragon Ball 2D** é um jogo 2D desenvolvido em Python utilizando a biblioteca padrão `turtle`. O jogo possui duas fases:
- **Fase 1:** O jogador precisa subir pelo cenário evitando encostar nos inimigos.
- **Fase 2:** O jogador enfrenta o chefe (**Frieza**), precisando desviar dos projéteis inimigos enquanto atira para derrotá-lo.

## Controles / Como Jogar

Com base no arquivo `Como jogar` e nos comandos configurados em `DB 2D.py`:

- **Iniciar o jogo:** Clique na tela após abrir a janela.
- **Movimentação:** Teclas `A`, `W`, `S`, `D` (no código principal: `A` para esquerda e `D` para direita).
- **Pular:** Tecla `Espaço`.
- **Atirar (Kamehameha):** Tecla `Y` *(disponível apenas na segunda fase)*.
- **Fechar o jogo:** Tecla `Q`.

> **Importante:** Lembre-se de deixar o **Caps Lock desligado** para que as teclas de comando funcionem corretamente.

## Contexto Acadêmico

Este jogo foi desenvolvido para a disciplina **Introdução à Informática para a Automação**, atendendo aos seguintes critérios do trabalho:
- Uso de dicionários ou objetos para salvar propriedades do jogador, obstáculos e inimigos;
- Uso de listas para armazenar os inimigos e obstáculos;
- 2 fases;
- 2 tipos de inimigos;
- Disparo de projétil pelo jogador ou inimigo;
- Tecla para iniciar e fechar o jogo;
- Barra de energia ou vida.

## Estrutura de Arquivos

- `DB 2D.py` — Código-fonte principal do jogo.
- `Como jogar` — Instruções básicas e controles do jogo.
- `Critérios` — Lista de requisitos da disciplina acadêmica.
- `frame1.gif` a `frame5.gif` — Frames de animação utilizados no jogo.
- `jogador_direita.gif`, `jogador_esquerda.gif` — Sprites do jogador.
- `picollo_direita.gif`, `picollo_esquerda.gif` — Sprites de inimigo.
- `frieza.gif` — Sprite do chefe (Fase 2).
- `mapa.gif`, `mapa2.gif` — Imagens de fundo das fases 1 e 2.
- `Luiz Gustavo de Andrade - Jogo.rar` — Arquivo compactado original do projeto.
- `.gitignore` — Regras padrão para ignorar arquivos temporários do Python e ambientes virtuais.
- `README.md` — Documentação do repositório.

## Dependências e Como Executar

Este projeto utiliza **apenas módulos da biblioteca padrão do Python** (`turtle`, `time`, `math` e `random`), portanto **não requer instalação de bibliotecas externas via `pip`**.

*(Observação para Linux: caso o `tkinter` não venha instalado por padrão com o Python, instale-o com `sudo apt-get install python3-tk`.)*

Execute os comandos abaixo a partir da raiz do repositório (necessário para que o jogo encontre os arquivos `.gif`):

```bash
git clone https://github.com/LuizAndr/Meu-primeiro-jogo-em-Python
cd Meu-primeiro-jogo-em-Python
python "DB 2D.py"
```

*(Em ambientes Linux/macOS onde `python` não aponte para o Python 3, utilize `python3 "DB 2D.py"`.)*
.0 melhorada para comparar minha evolução.

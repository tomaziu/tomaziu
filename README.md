<div align="center">

# 👋 Olá, eu sou o Thomaz

### Desenvolvedor Web | Estudante de Sistemas de Informação

<a href="https://github.com/tomaziu">
  <img src="https://img.shields.io/badge/GitHub-tomaziu-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>
<a href="https://linkedin.com/in/thomaz">
  <img src="https://img.shields.io/badge/LinkedIn-thomaz-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="mailto:tomaziu@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-tomaziu-F1403A?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
</a>

</div>

---

## 📈 Minhas Contribuições

<div align="center">

![Contributions](https://github-readme-activity-graph.vercel.app/graph?username=tomaziu&bg_color=0d1117&color=58a6ff&line=58a6ff&point=79c0ff&area=true&area_color=58a6ff&area_opacity=0.3)

</div>

---

## 🐍 Snake Game

<div align="center">

<svg width="320" height="320" viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes moveSnake {
        0%   { x: 20; y: 160; }
        10%  { x: 40; y: 160; }
        20%  { x: 60; y: 160; }
        30%  { x: 60; y: 140; }
        40%  { x: 60; y: 120; }
        50%  { x: 80; y: 120; }
        60%  { x: 100; y: 120; }
        70%  { x: 120; y: 120; }
        80%  { x: 140; y: 120; }
        90%  { x: 160; y: 120; }
        100% { x: 180; y: 120; }
      }
      @keyframes moveTail {
        0%   { x: 0;   y: 160; }
        10%  { x: 20;  y: 160; }
        20%  { x: 40;  y: 160; }
        30%  { x: 60;  y: 160; }
        40%  { x: 60;  y: 140; }
        50%  { x: 60;  y: 120; }
        60%  { x: 80;  y: 120; }
        70%  { x: 100; y: 120; }
        80%  { x: 120; y: 120; }
        90%  { x: 140; y: 120; }
        100% { x: 160; y: 120; }
      }
      @keyframes blink {
        0%, 100% { opacity: 1; }
        50%      { opacity: 0.3; }
      }
      @keyframes foodPulse {
        0%, 100% { r: 6; opacity: 1; }
        50%      { r: 8; opacity: 0.7; }
      }
      .snake-head { fill: #39d353; }
      .snake-body { fill: #26a641; }
      .food       { fill: #f85149; animation: foodPulse 0.8s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Background grid -->
  <rect width="320" height="320" rx="8" fill="#0d1117"/>
  <g stroke="#161b22" stroke-width="1">
    <line x1="0" y1="20" x2="320" y2="20"/><line x1="0" y1="40" x2="320" y2="40"/>
    <line x1="0" y1="60" x2="320" y2="60"/><line x1="0" y1="80" x2="320" y2="80"/>
    <line x1="0" y1="100" x2="320" y2="100"/><line x1="0" y1="120" x2="320" y2="120"/>
    <line x1="0" y1="140" x2="320" y2="140"/><line x1="0" y1="160" x2="320" y2="160"/>
    <line x1="0" y1="180" x2="320" y2="180"/><line x1="0" y1="200" x2="320" y2="200"/>
    <line x1="0" y1="220" x2="320" y2="220"/><line x1="0" y1="240" x2="320" y2="240"/>
    <line x1="0" y1="260" x2="320" y2="260"/><line x1="0" y1="280" x2="320" y2="280"/>
    <line x1="0" y1="300" x2="320" y2="300"/>
    <line x1="20" y1="0" x2="20" y2="320"/><line x1="40" y1="0" x2="40" y2="320"/>
    <line x1="60" y1="0" x2="60" y2="320"/><line x1="80" y1="0" x2="80" y2="320"/>
    <line x1="100" y1="0" x2="100" y2="320"/><line x1="120" y1="0" x2="120" y2="320"/>
    <line x1="140" y1="0" x2="140" y2="320"/><line x1="160" y1="0" x2="160" y2="320"/>
    <line x1="180" y1="0" x2="180" y2="320"/><line x1="200" y1="0" x2="200" y2="320"/>
    <line x1="220" y1="0" x2="220" y2="320"/><line x1="240" y1="0" x2="240" y2="320"/>
    <line x1="260" y1="0" x2="260" y2="320"/><line x1="280" y1="0" x2="280" y2="320"/>
    <line x1="300" y1="0" x2="300" y2="320"/>
  </g>

  <!-- Snake body segment 3 -->
  <rect x="0" y="160" width="20" height="20" rx="4" fill="#1a5c2b" style="animation: moveTail 4s linear infinite;"/>
  <!-- Snake body segment 2 -->
  <rect x="0" y="160" width="20" height="20" rx="4" fill="#1f7a33" style="animation: moveTail 4s linear infinite;"/>
  <!-- Snake body segment 1 -->
  <rect x="0" y="160" width="20" height="20" rx="4" fill="#26a641" style="animation: moveTail 4s linear infinite;"/>
  <!-- Snake head -->
  <rect x="20" y="160" width="20" height="20" rx="4" class="snake-head" style="animation: moveSnake 4s linear infinite;"/>
  <!-- Snake eyes -->
  <circle cx="28" cy="167" r="2" fill="#0d1117" style="animation: moveSnake 4s linear infinite;"/>
  <circle cx="34" cy="167" r="2" fill="#0d1117" style="animation: moveSnake 4s linear infinite;"/>

  <!-- Food -->
  <circle cx="200" cy="120" r="6" class="food"/>

  <!-- Score label -->
  <text x="160" y="30" text-anchor="middle" fill="#8b949e" font-family="monospace" font-size="12">🐍 SNAKE GAME</text>
</svg>

</div>


## 🚀 Sobre mim

```
🎓  Estudante de Sistemas de Informação na UNIGRANDE
💡  Curioso por tecnologia e resolver problemas com código
🚀  Focado em interfaces, automação e deploy
📈  Sempre buscando evoluir
```

---

## 💻 Tech Stack

<div align="center">

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

</div>



# quizrush-mvp
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>QuizRush Личный кабинет</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      background: #f0f0f0;
    }
    .header {
      font-size: 22px;
      margin-bottom: 10px;
    }
    .balance {
      background: #fff;
      padding: 10px;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .quiz-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .quiz {
      background: white;
      border-radius: 6px;
      padding: 10px;
      box-shadow: 0 0 4px rgba(0,0,0,0.1);
      cursor: pointer;
    }
    .quiz:hover {
      background: #f5f5f5;
    }
  </style>
</head>
<body>
  <div class="header">Привет, пользователь 👋</div>
  <div class="balance">Твои токены: <span id="balance">0</span> 🪙</div>

  <div class="header">Выбери квиз:</div>
  <div class="quiz-list">
    <div class="quiz" onclick="startQuiz('Мемы')">🔥 Мемы</div>
    <div class="quiz" onclick="startQuiz('Кино')">🎬 Кино</div>
    <div class="quiz" onclick="startQuiz('Финансы')">💰 Финансы</div>
  </div>

  <script>
    Telegram.WebApp.ready();

    let tokens = 0;

    function startQuiz(topic) {
      const answer = confirm(`Квиз «${topic}». Начать?`);
      if (answer) {
        alert("Квиз завершён! +10 токенов");
        tokens += 10;
        document.getElementById("balance").innerText = tokens;
      }
    }
  </script>
</body>
</html>

# Голосовой помощник Атом

---

Хакатон АТОМ. Кейс 1. Разработка back-end решения для голосового управления автомобилем.

---

Начало работы:

1. Клонируйте репозиторий на свою локальную машину 
`git clone https://github.com/niikmynick/atom_voice_assistant.git`
2. Установите зависимости из requirements.py с помощью команды 
`pip install -r requirements.txt`
3. Запустите приложение
`python main.py`

---

Стек:
- Python
- PicoVoice
- VOSK

Способ работы ассистента:

Ассистент реагирует на фразу-активатор "Привет, Атом"

После активации готов воспринимать как одну команду, так и последовательность команд от пользователя.

Для распознавания намерений пользователя используется расстояние Дамерау-Левенштейна.

---

Возможности развития:

- Переход от нечеткого поиска к методам искусственного интеллекта

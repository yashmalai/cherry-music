from src.recognizer import listen
from src.player import MusicPlayer
from src.commands import parse_command, Action

player = MusicPlayer()

print("Ассистент запущен. Говори команды...")

while True:
    try:
        text = listen()
        print(f"Распознано: {text}")
        
        cmd, secondary = parse_command(text)
        
        if cmd == Action.PLAY:
            response = player.play(secondary)
            print(response)
        elif cmd["action"] == "stop":
            player.stop()
            print("Остановлено")
        elif cmd["action"] == "next":
            response = player.next()
            print(response)
        elif cmd["action"] == "volume":
            player.volume(cmd["level"])
            print(f"Громкость: {cmd['level']}")
        elif cmd["action"] == "unpause":
            player.unpause()
            print("Продолжаю")
        elif cmd == Action.WRONG_COMAND:
            print("Неизвестная команда")
            
    except Exception as e:
        print("Ошибка:", e)
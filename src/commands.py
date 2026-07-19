import re
import enum

PLAY_WORDS = {"включи", "играй", "поставь", "запусти"}
STOP_WORDS = {"стоп", "пауза", "останови"}
NEXT_WORDS = {"дальше", "следующий", "следующую"}

class Action(enum.Enum):
    PLAY = 'play'
    STOP = 'stop'
    NEXT = 'next'
    VOLUME = 'volume'
    UNPAUSE = 'unpause'
    WRONG_COMAND = 'wrong'

def parse_command(text):
    text = text.lower()
    
    if any(w in text for w in PLAY_WORDS):
        match = re.search(r'(включи|играй|поставь|запусти)\s+(.+)', text)
        query = match.group(2) if match else None
        return Action.PLAY, query
    
    if any(w in text for w in STOP_WORDS):
        return Action.STOP
    
    if any(w in text for w in NEXT_WORDS):
        return Action.NEXT
    
    if "громче" in text or "тише" in text:
        level = 0.9 if "громче" in text else 0.4
        return Action.VOLUME, level
    
    if any(w in text for w in ["продолжай", "включи дальше", "продолжи"]):
        return Action.UNPAUSE
    
    return Action.WRONG_COMAND
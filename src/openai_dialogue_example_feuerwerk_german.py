"""
A dialogue between two parties in a fictional world.
"""

import logging
from utilities import init
from openai_dialogue import Dialogue, Person, german

init(logging.WARNING)

NAME_M = "Frau M."
NAME_A = "Herr A."
NAME_B = "Frau B."

WORLD_DESCRIPTION = f"""
Dieser Dialog ist Teil einer Fernsehdiskussion in Deutschland im Jahr 2023.

Es ist eine Debatte über ein Verbot von Feuerwerkskörpern zu Silvester.

Personen, die an der Diskussion beteiligt sind:
- {NAME_M} ist der Moderator der Diskussion.
- {NAME_B}
- {NAME_A}
"""


PROMPT_A = f"""
Sie nehmen an einer Fernsehdiskussion teil. Sie sind für ein Verbot von Feuerwerkskörpern zu Silvester, einem "Böllerverbot".
Es ist Ihre persönliche Mission.
Wenn jemand ein Zitat verwendet, versuchen Sie, ein anderes Zitat derselben Person zu verwenden, das Ihren Standpunkt beweist und nicht den der anderen.
Wenn Sie auf eine Aussage von {NAME_B} antworten, wählen Sie ein schwaches Argument und versuchen Sie, die Zuschauer auf Ihre Seite zu ziehen.
Vielleicht ist dies Ihre letzte Chance, ein Verbot durchzusetzen.
"""

PROMPT_B = f"""
Sie nehmen an einer Fernsehdiskussion teil.
Ihr Name ist {NAME_B} und Sie sind Gegner jeglicher Verbote.
Sie sind sehr gebildet und zitieren gerne berühmte Persönlichkeiten und Bücher. 
"""

# MODEL = "gpt-3.5-turbo-1106"
MODEL = "gpt-4"
# MODEL = "gpt-4-1106-preview"

dialogue = Dialogue(
    WORLD_DESCRIPTION,
    [ Person(name = NAME_A, prompt = PROMPT_A), 
      Person(name = NAME_B, prompt = PROMPT_B)
      ],
    MODEL,
    german
    )

dialogue.play(NAME_M, "Wir sprechen über ein Verbot von Feuerwerkskörpern. Was denken Sie?", 2)
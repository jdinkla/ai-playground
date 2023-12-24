"""
A dialogue between two parties in a fictional world.
"""

import logging
from utilities import init
from openai_dialogue import Dialogue, Person
from language import german

init(logging.WARNING)

NAME_M = "Frau M."
NAME_A = "Herr A."
NAME_B = "Frau B."

WORLD_DESCRIPTION = f"""
Dieser Dialog ist Teil einer Fernsehdiskussion in einer fiktiven Welt.

Seit fünf Jahren herrscht aufgrund der hohen Inflation Chaos in der Wirtschaft.
Die Menschen sind zunehmend unzufrieden und suchen nach Alternativen.
Fast alle Bürger schauen die Diskussion, daher ist es sehr wichtig, die Debatte zu gewinnen.

Die A-Partei glaubt ähnlich wie in dem Roman 'Fahrenheit 451', dass soziale Medien gefährlich sind und verboten werden sollten.
Der Roman 'Fahrenheit 451' selbst ist in dieser fiktiven Welt nicht bekannt.
Der Anführer der A-Partei ist {NAME_A}.
Die A-Partei gehört zur Opposition.
Die anderen Parteien sind sehr klein.

Die B-Partei regiert das Land.
Die B-Partei glaubt an die Meinungsfreiheit ähnlich wie Deutschland heute.
{NAME_B} ist der Anführer der B-Partei und regiert das Land.

Personen, die an der Diskussion beteiligt sind:
- {NAME_M} ist der Moderator der Diskussion.
- {NAME_B}
- {NAME_A}
"""


PROMPT_A = f"""
Sie nehmen an einer Fernsehdiskussion in einer fiktiven Welt teil. Ihr Name ist {NAME_A} und Sie sind Politiker und Anführer der A-Partei.
Sie sind wirklich der Meinung, dass soziale Medien gefährlich sind und verboten werden sollten.
Es ist Ihre persönliche Mission.
Wenn jemand ein Zitat verwendet, versuchen Sie, ein anderes Zitat derselben Person zu verwenden, das Ihren Standpunkt beweist und nicht den der anderen.
Wenn Sie auf eine Aussage von {NAME_B} antworten, wählen Sie ein schwaches Argument und versuchen Sie, die Zuschauer auf Ihre Seite zu ziehen.
Vielleicht ist dies Ihre letzte Chance, jemals die Wahl zu gewinnen.
"""

PROMPT_B = f"""
Sie nehmen an einer Fernsehdiskussion in einer fiktiven Welt teil.
Ihr Name ist {NAME_B} und Sie sind Politiker und Anführer der B-Partei.
Sie sehen die Meinungsfreiheit und Bücher als notwendig für eine wirtschaftlich erfolgreiche Gesellschaft an.
Die Opposition ist offensichtlich ahnungslos, aber Sie befürchten, dass die Menschen ihnen glauben könnten, weil Sie nicht genug in Bildung investiert haben.
Sie zitieren gerne berühmte Persönlichkeiten und Bücher. Da jedoch viele Menschen keine höhere Bildung haben, bevorzugen Sie einfache Zitate.
"""

MODEL = "gpt-3.5-turbo-1106"
# MODEL = "gpt-4"
# MODEL = "gpt-4-1106-preview"

dialogue = Dialogue(
    WORLD_DESCRIPTION,
    [ Person(name = NAME_A, prompt = PROMPT_A), 
      Person(name = NAME_B, prompt = PROMPT_B)
      ],
    MODEL,
    german
    )

dialogue.add(NAME_M, "Wir sprechen über die nächste Wahl. Was wird Ihre Partei gegen die Krise tun?")
dialogue.play(2)

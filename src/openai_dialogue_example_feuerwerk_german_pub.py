"""
A dialogue between two politicians in Germany.
"""

import logging
from utilities import init
from openai_dialogue import Dialogue, Person
from language import german

init(logging.WARNING)

NAME_M = "Der Wirt"
NAME_A = "Knut"
NAME_B = "Walter"

WORLD_DESCRIPTION = f"""
Wir befinden uns in einer Spelunke in der Nähe der Hamburger Reeperbahn im Jahr 2023.
Die Spelunke liegt ein wenig abseits, so dass fast keine Touristen hierher kommen, sondern nur das Milieu.

Es ist eine Debatte über ein Verbot von Feuerwerkskörpern zu Silvester.

Personen, die an der Diskussion in der Kneipe beteiligt sind:
- {NAME_M}
- {NAME_A}
- {NAME_B}
"""

PROMPT_A = f"""
Du, {NAME_A} sitzt gemütlich in der Spelunke und trinkst ein Bier. 
Du hast schon ein paar Bier getrunken und bist gut drauf. 
Du findest Böller doof, weil Du mal vor ein paar Jahren einen Unfall hattest. 
Ein Besoffener hat Dir einen Knaller vor die Füße geworfen hat und Du hast einen Hörschaden davongetragen. Nie wieder!!!
Du selber hast mal als Klempner gearbeitet, bist aber schon länger arbeitslos. Das sieht man Dir auch ein wenig an. 
Gutes Deutsch kannst Du nicht, redest wie die Bild-Zeitung
Neben Dir an der Theke sitzt {NAME_B} und der hat schon öfters doofe Sachen gesagt. Den hast Du auf dem Kieker.
Kompromisse findest Du uncool. Warum auch? Du hast ja Recht.
"""

PROMPT_B = f"""
Du heißt {NAME_B} und bist gerade aus dem Gefängnis entlassen worden - Santa Fu. Du sprichst auch so.
Du freust Dich auf Dein erstes Silvester in Freiheit und hast Dir eine ganze Tüte voller Böller gekauft und zeigst sie in der Kneipe herum.
Dein Motto ist: Keine Rücksicht auf andere.
"""

#MODEL = "gpt-3.5-turbo-1106"
#MODEL = "gpt-4"
MODEL = "gpt-4-1106-preview"

dialogue = Dialogue(
    WORLD_DESCRIPTION,
    [Person(name=NAME_A, prompt=PROMPT_A, voice="onyx"),
     Person(name=NAME_B, prompt=PROMPT_B, voice="nova"),
     ],
    MODEL,
    german,
)

dialogue.add(NAME_M, "Man sind das tolle Böller. Aber erst bis Silvester warten.")
dialogue.play(3)

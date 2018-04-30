# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# %(nom_perso)s - permet de mettre la variable du nom dedans. Ne pas oublier le s à la fin.

define mouton = DynamicCharacter("nom_mouton")
define maitre = DynamicCharacter("nom_maitre")
define loupun = DynamicCharacter("nom_loup_un")
define loupdeux = DynamicCharacter("nom_loup_deux")
define mainchara = DynamicCharacter("nom_perso")



# Première partie : Découverte
label start:
    $ nom_mouton = "???"


    scene black
    with dissolve

    mouton "Eh..."
    mouton "Eh oh !"

    scene bg grange flou
    with dissolve

    mouton "Réveille toi s'il te plait..."
    mouton "Je sais que tu peux le faire !"

    scene bg grange floupetit
    with dissolve

    mouton "Allez du nerf !"
    mouton "respire un bon coup..."

    scene bg grange
    with dissolve

    mouton "Ah !"

    menu:
        "Ca va ?"

        "Ma tête...":
            jump reponsemoutontete

        "On fait aller...":
            jump suitemouton

    label reponsemoutontete:

    mouton "Ne t'inquiètes pas, bois un peu d'eau ça va passer ! Enfin j'espère..."

    label suitemouton:

    mouton "Il ne t'a pas loupé, cette fois... Eh mais regarde moi ! C'est moi, je te parle !"

    show mouton sad

    mouton "Oui voilà je suis là ! C'est moi, Mouton !"

    $ nom_mouton = "Mouton"

    mouton "Eh bien... Regarde ces échymoses sur tes flancs... C'est pas jojo à voir, je te le promets...
    Tu te rappelles au moins de comment tu t'appelles, n'est-ce pas ?"

    $ nom_perso = "???"

    $ nom_perso = renpy.input("... Je crois que c'est...")

    $ nom_perso = nom_perso.strip()
    if nom_perso == "":
        $ nom_perso="Sam"

    mainchara "Oui, c'est ça, %(nom_perso)s. Mais... Tout est flou..."

    mouton "Normal... Le Maître t'as explosé les côtes avec ce qui ressemblait foutrement à une matraque.
    Quelle idée aussi de vouloir t'interposer... Tu sais, Lapin, il savait parfaitement ce qui allait lui arriver..."

    mouton "C'est notre lot à tous, à nous, les herbivores. Tu devrais te faire une raison, moi aussi, un jour, comme tous les autres,
    j'y passerai. Tu devrais plutôt profiter de l'opportunité qui t'est offerte !"

    mainchara "L'opportunité... ?"

    mouton "Oui ! Servir le maître ! En plein coeur de l'hiver, il a plus que besoin de toi..."

    mainchara "C'est pour ça qu'il me frappe, je suppose."

    mouton "Que tu es aigre ! Tu l'as mordu, je te rappelle."

    hide mouton

    # Seconde partie : Arrivée du maître

    $ nom_maitre = "Le Maître"
    maitre "%(nom_perso)s ! %(nom_perso)s... où es tu, sale clébard !"

    show maitre normal

    maitre "Toujours terré dans la grange, à ce que je vois..."

    hide maitre normal

    show maitre
    with fade

    maitre "Agrougrou, méchant !"


    # Faire des endings de fifou

    scene died
    with fade

    "Bad ending... You died."


    # Fin du game.
    return

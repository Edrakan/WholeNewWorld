# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mouton = DynamicCharacter("nom_mouton")
define maitre = DynamicCharacter("nom_maitre")
define loupun = DynamicCharacter("nom_loup_un")
define loupdeux = DynamicCharacter("nom_loup_deux")
define mainchara = DynamicCharacter("nom_perso")



# The game starts here.

label start:
    $ nom_mouton = "???"


    scene black
    with dissolve

    mouton "Bienvenue."

    scene bg ecrantitre
    with fade

    show mouton

    mouton "J'espère que tu n'as pas trop peur et que tu vas bien !"
    mouton "C'est moi, Mouton ! Je vais te montrer un peu comment ça fonctionne."

    $ nom_mouton = "Mouton"

    mouton "Ne bouge pas, tout va bien se passer. Tu te rappelles au moins de ton nom ?"

    $ nom_perso = renpy.input("Bien sûr ! Mon nom est... ")

    $ nom_perso = nom_perso.strip()
    if nom_perso == "":
        $ nom_perso="Sam"


    mainchara "Evidemment !"

    # This ends the game.
    return

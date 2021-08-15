wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50


while True:

    print("1)    Wizard")
    print("2)    Elf")
    print("3)    Human")
    character = int(input("Choose your character."))

    if character == 1:
        character = "Wizard"
        health = wizard_hp
        damage = wizard_damage
        break
    if character == 2:
        character = "Elf"
        health = elf_hp
        damage = elf_damage
        break
    if character == 3:
        character = "Human"
        health = human_hp
        damage = human_damage
        break
    else:
        print("Unknown character")

print("You have chosen the {}".format(character))
print("Health: {}".format(health))
print("Damage: {}".format(damage))

while True:
    dragon_hp = dragon_hp - damage
    print("The {} damaged the Dragon".format(character))
    print("The dragon's hit points are now {}.".format(dragon_hp))
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    health = health - dragon_damage
    print("The Dragon strikes back at the {}".format(character))
    print("The {}'s hitpoints are now: {}".format(character, health))
    if health <= 0:
        print("The {} has lost the battle".format(character))
        break

import graphics
print(" Welcome to the War Survival Game!")
print("You find yourself in the midst of a war zone...")
print(graphics.plain)
print("You need to make choices to survive in this war-torn land.")

# Choice 1: Scavenge for supplies

print("\nChapter name 1: Scavenge for supplies")
print("You come across a ruined building. Do you want to scavenge for supplies?")
print("1. Yes, scavenge for supplies.")
print("2. Move on without scavenging.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("You find some valuable supplies, including food and ammunition.")
else:
    print("You ignored an opportunity and moved on.")
# Choice 2: Ambush

print("\nChapter name 2: Ambush")
print("You spot an enemy patrol up ahead. Do you want to ambush them?")
print("1. Yes, ambush the patrol.")
print("2. Avoid the patrol and stay hidden.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("You attempted to ambush the patrol but were caught and killed by enemy forces.")
    print(graphics.game_over)
    exit()
else:
    print("You wisely avoided the patrol and continued your journey.")
# Choice 3: Seek shelter
print("\nChapter name 3: Seek shelter")
print("Night is falling, and you need shelter. Do you want to search for a safe place?")
print("1. Yes, search for shelter.")
print("2. Risk staying in the open.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("You found a hidden cave to spend the night safely.")
else:
    print("You decided to stay in the open, and enemy scouts discovered you. You are captured.")
    print(graphics.game_over)
    exit()

# Choice 4: Help a wounded soldier
print("\nChapter name 4: Help a wounded soldier")
print("You come across a wounded soldier. Do you want to help?")
print("1. Yes, help the wounded soldier.")
print("2. Leave the wounded soldier behind.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("You helped the wounded soldier, and together you find a safer path.")
else:
    print("You left the wounded soldier behind, and your path became more perilous.")

# Choice 5: Cross a dangerous bridge
print("\nChapter name 5: Cross a dangerous bridge")
print("You reach a rickety bridge over a deep ravine. Do you want to cross?")
print("1. Yes, cross the bridge carefully.")
print("2. Find an alternative route.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("As you cross, the bridge collapses, and you fall into the ravine.")
    print(graphics.game_over)
    exit()
else:
    print("You find an alternative route, avoiding the dangerous bridge.")

# Choice 6: Join a group of survivors
print("\nChapter name 6: Join a group of survivors")
print("You encounter a group of survivors who invite you to join them. Do you accept?")
print("1. Yes, join the group.")
print("2. Decline and continue on your own.")

choice = input("Enter your choice(1 or 2): ")
if choice == "1":
    print("You join the group, and together, you have a better chance of survival.")
else:
    print("You decided to continue on your own, and the path becomes increasingly perilous.")

# End of game
print("\nThe war rages on.")
print("Congratulations! You have survived the war and found a group to support each other.")
print(graphics.trophy)

hero_health = 100 # Starting health of the hero
hero_damage = 10 # Starting damage dealt by the hero
monster_health = 50 # Starting health of each monster
monster_damage = 5 # Starting damage dealt by each monster

for level in range(1, 11):
    print(f"Level {level}:")
    for monster in range(1, 101):
        hero_health -= monster_damage # Hero takes damage from monster
        monster_health -= hero_damage # Monster takes damage from hero

        # Check if either the hero or monster has reached 0 health
        if hero_health <= 0:
            print("Hero defeated!")
            break
        if monster_health <= 0:
            print(f"Monster {monster} defeated!")
            monster_health = 50 # Reset monster health for next monster
    if hero_health <= 0:
        break
    # Increase the hero's damage and health after each level
    hero_damage += (hero_damage*5)/100
    hero_health += (hero_health*10)/100

print("All levels complete!")
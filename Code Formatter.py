if event.type == pygame.KEYDOWN:
    elif event.key == pygame.K_n and player1.supported == True:
        if player1.gun == "rifle" and player1.ammo > 0 and rifleshoot == 0:
        pygame.mixer.music.load('Rifleshot.mp3')
        pygame.mixer.music.play()

if event.type == pygame.KEYUP:
    if player1.aiming == True and player1.ammo > 0:
        if player1.gun == "rifle":
            pygame.mixer.music.stop()

            # Code from other criteria
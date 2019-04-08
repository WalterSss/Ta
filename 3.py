shooting_sound = pygame.mixer.Sound(path.join(sound_folder,'pew.wav'))
missile_sound = pygame.mixer.Sound(path.join(sound_folder,'rocket.ogg'))

#加载敌机、火山石爆炸声音
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder,sound)))
#调低音量
pygame.mixer.music.set_volume(0.2)

#加载玩家爆炸声音
player_die_sound = pygame.mixer.Sound(path.join(sound_folder,'rumble1.ogg'))

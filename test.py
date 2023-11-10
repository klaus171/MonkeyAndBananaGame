import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Monkey Banana Game")

# 배경 이미지 로드 및 크기 조절
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (width, height))

# 원숭이 이미지 로드 및 크기 조절
monkey_img = pygame.image.load("monkey.png")
monkey_img = pygame.transform.scale(monkey_img, (200, 200))

# 바나나 이미지 로드 및 크기 조절
banana_img = pygame.image.load("banana.png")
banana_img = pygame.transform.scale(banana_img, (100, 100))

# 원숭이 위치
monkey_rect = monkey_img.get_rect()
monkey_rect.center = (width // 2, height - 50)

# 바나나 위치 초기화 함수
def initialize_banana():
    return random.randint(banana_img.get_width() // 2, width - banana_img.get_width() // 2), random.randint(0, height // 2)

# 바나나 초기화
num_bananas = 5
bananas = [pygame.Rect(initialize_banana(), (60, 60)) for _ in range(num_bananas)]
banana_speed = 5

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and monkey_rect.left > 0:
        monkey_rect.x -= 5
    if keys[pygame.K_RIGHT] and monkey_rect.right < width:
        monkey_rect.x += 5

    # 바나나 이동
    for banana_rect in bananas:
        banana_rect.y += banana_speed
        if banana_rect.y > height:
            banana_rect.topleft = initialize_banana()

        # 충돌 체크
        if monkey_rect.colliderect(banana_rect):
            print("게임 종료! 바나나와 충돌")
            pygame.quit()
            sys.exit()

    # 배경 그리기
    screen.blit(background_img, (0, 0))

    # 그리기
    screen.blit(monkey_img, monkey_rect)
    for banana_rect in bananas:
        screen.blit(banana_img, banana_rect)

    pygame.display.flip()

    # 초당 프레임 수 설정
    clock.tick(60)

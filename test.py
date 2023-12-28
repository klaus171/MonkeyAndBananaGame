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
monkey_img = pygame.transform.scale(monkey_img, (400, 400))

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

# 점수 초기화
score = 0

# 시스템 폰트 경로 설정 (운영체제에 따라 경로가 다를 수 있음)
font_path = pygame.font.match_font('arial')

# 시스템 폰트 로드
font = pygame.font.Font(font_path, 36)  # 36은 폰트 크기


# 제한 시간 설정 (초 단위)
time_limit = 60
start_time = pygame.time.get_ticks()

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

    # 현재 시간 계산 (밀리초 단위)
    current_time = pygame.time.get_ticks()

    # 경과 시간 계산 (초 단위)
    elapsed_time = (current_time - start_time) // 1000

    # 시간 초과 시 게임 종료
    if elapsed_time >= time_limit:
        print(f"게임 종료!Game Over! Score:: {score}")

        # 게임 종료 메시지 표시
        final_score_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
        screen.blit(final_score_text, (width // 2 - 150, height // 2 - 50))
        pygame.display.flip()

        # 잠시 대기 후 종료
        pygame.time.wait(5000)  # 3000 밀리초 (3초) 동안 대기
        pygame.quit()
        sys.exit()

    # 바나나 이동
    for banana_rect in bananas:
        banana_rect.y += banana_speed
        if banana_rect.y > height:
            banana_rect.topleft = initialize_banana()

        # 충돌 체크
        if monkey_rect.colliderect(banana_rect):
            score += 1
            banana_rect.topleft = initialize_banana()

    # 배경 그리기
    screen.blit(background_img, (0, 0))

    # 그리기
    screen.blit(monkey_img, monkey_rect)
    for banana_rect in bananas:
        screen.blit(banana_img, banana_rect)

    # 점수 및 시간 표시
    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    time_text = font.render(f"Time: {time_limit - elapsed_time}", True, (0, 0, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (width - 120, 10))

    pygame.display.flip()

    # 초당 프레임 수 설정
    clock.tick(60)

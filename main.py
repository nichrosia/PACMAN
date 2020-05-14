import pygame


def create_map(file):
    junctions = []
    rails = []
    with open(file) as blueprint:
        for line in blueprint:
            if line[0] == 'J':
                junction = []
                for item in line[1:].split(', '):
                    junction.append(int(item))
                junctions.append(junction)
            elif line[0] == 'R':
                rail = []
                for item in line[1:].split(', '):
                    rail.append(int(item))
                rails.append(rail)
    return junctions, rails


def main():
    junctions, rails = create_map('junctions_rails.txt')
    window = (1000, 750)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('PACMAN')
    screen.fill((255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for start, end in rails:
            pygame.draw.line(screen, (0, 0, 0), junctions[start], junctions[end], 5)
        for junction in junctions:
            pygame.draw.circle(screen, (255, 0, 0), junction, 20, 0)
        pygame.display.flip()


if __name__ == '__main__':
    main()

import pygame


TUNNEL_SIZE = 40


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


def get_wall_dots(junctions):
    walldots = []
    for junction in junctions:
        walldots.append([
            [junction[0] - TUNNEL_SIZE, junction[1] - TUNNEL_SIZE],
            [junction[0] + TUNNEL_SIZE, junction[1] - TUNNEL_SIZE],
            [junction[0] - TUNNEL_SIZE, junction[1] + TUNNEL_SIZE],
            [junction[0] + TUNNEL_SIZE, junction[1] + TUNNEL_SIZE],
        ])
    return walldots


def main():
    junctions, rails = create_map('junctions_rails.txt')
    window = (1000, 750)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('PACMAN')
    screen.fill((255, 255, 255))
    black = (0, 0, 0)
    wall_dots = get_wall_dots(junctions)
    rail_directions = []
    junctions_directions = {}
    iterator = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for start, end in rails:
            pygame.draw.line(screen, (0, 0, 255), junctions[start], junctions[end], 5)
        for junction in junctions:
            pygame.draw.circle(screen, (100, 100, 255), junction, 20, 0)
            junctions_directions[str(iterator)] = []
            iterator += 1
        iterator = 0
        for wall_dots_surrounding_junction in wall_dots:
            for walldot in wall_dots_surrounding_junction:
                pygame.draw.circle(screen, black, walldot, 2, 0)
        for rail in rails:
            if junctions[rail[0]][0] - junctions[rail[1]][0] == 0:
                rail_directions.append('VERTICAL')
                junctions_directions[str(rail[0])].append('DOWN')
                junctions_directions[str(rail[1])].append('UP')
            else:
                rail_directions.append('HORIZONTAL')
                junctions_directions[str(rail[0])].append('RIGHT')
                junctions_directions[str(rail[1])].append('LEFT')
        for rail, rail_direction in zip(rails, rail_directions):
            if rail_direction == 'HORIZONTAL':
                start, end = wall_dots[rail[0]][1], wall_dots[rail[1]][0]
                pygame.draw.line(screen, black, start, end, 5)
                start, end = wall_dots[rail[0]][3], wall_dots[rail[1]][2]
                pygame.draw.line(screen, black, start, end, 5)
            elif rail_direction == 'VERTICAL':
                start, end = wall_dots[rail[0]][2], wall_dots[rail[1]][0]
                pygame.draw.line(screen, black, start, end, 5)
                start, end = wall_dots[rail[0]][3], wall_dots[rail[1]][1]
                pygame.draw.line(screen, black, start, end, 5)
        for junction, iterator in zip(junctions, range(len(junctions))):
            if 'DOWN' not in junctions_directions[str(iterator)]:
                start, end = wall_dots[iterator][2], wall_dots[iterator][3]
                pygame.draw.line(screen, black, start, end, 5)
            if 'UP' not in junctions_directions[str(iterator)]:
                start, end = wall_dots[iterator][0], wall_dots[iterator][1]
                pygame.draw.line(screen, black, start, end, 5)
            if 'LEFT' not in junctions_directions[str(iterator)]:
                start, end = wall_dots[iterator][0], wall_dots[iterator][2]
                pygame.draw.line(screen, black, start, end, 5)
            if 'RIGHT' not in junctions_directions[str(iterator)]:
                start, end = wall_dots[iterator][1], wall_dots[iterator][3]
                pygame.draw.line(screen, black, start, end, 5)
        iterator = 0
        pygame.display.flip()


if __name__ == '__main__':
    main()

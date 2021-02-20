import pygame


class Board:
    def __init__(self, cell_size):
        self.width = 64
        self.height = 64
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell and cell < (self.width, self.height):
            self.on_click(cell)


class Ore:
    def __init__(self):
        self.color = pygame.Color(237, 160, 49)

    def get_color(self):
        return self.color


class Mountain:
    def __init__(self):
        self.color = pygame.Color(120, 120, 120)

    def get_color(self):
        return self.color


class Building:
    def __init__(self):
        self.color = pygame.Color(60, 60, 60)

    def get_color(self):
        return self.color


class Park:
    def __init__(self):
        self.color = pygame.Color(152, 255, 152)

    def get_color(self):
        return self.color


class Arch:
    def __init__(self):
        self.color = pygame.Color(80, 80, 80)

    def get_color(self):
        return self.color

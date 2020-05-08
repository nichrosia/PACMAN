import pygame


class Rail:
    def __init__(self):
        self.left_junction = None
        self.right_junction = None
        self.top_junction = None
        self.bottom_junction = None

    def attach_left(self, junction):
        orientation = self.get_orientation()
        if orientation == 'vertical':
            raise self._create_orientation_error(orientation, 'left')

        self.left_junction = junction

    def attach_right(self, junction):
        orientation = self.get_orientation()
        if orientation == 'vertical':
            raise self._create_orientation_error(orientation, 'right')

        self.right_junction = junction

    def attach_top(self, junction):
        orientation = self.get_orientation()
        if orientation == 'horizontal':
            raise self._create_orientation_error(orientation, 'top')

        self.top_junction = junction

    def attach_bottom(self, junction):
        orientation = self.get_orientation()
        if orientation == 'horizontal':
            raise self._create_orientation_error(orientation, 'bottom')

        self.bottom_junction = junction

    def get_orientation(self):
        if self.left_junction or self.right_junction:
            return 'horizontal'
        if self.top_junction or self.bottom_junction:
            return 'vertical'

        return 'unset'

    def _create_orientation_error(self, orientation, attachment_direction):
        return ValueError(f'Rail is already oriented {orientation}ly, Cannot attach on {attachment_direction}')


class Junction:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

        self.left_rail = None
        self.right_rail = None
        self.top_rail = None
        self.bottom_rail = None

    def attach_left(self, rail):
        self.left_rail = rail

    def attach_right(self, rail):
        self.right_rail = rail

    def attach_top(self, rail):
        self.top_rail = rail

    def attach_bottom(self, rail):
        self.bottom_rail = rail

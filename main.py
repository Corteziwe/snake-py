import pygame
from control import Control
from snake import Snake
from gui import Gui

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")

control = Control()
snake = Snake()
gui = Gui()
var_speed = 0


while(control.flag_game):
	control.control()
	window.fill(pygame.Color("Black"))
	snake.draw_snake(window)
	gui.draw_level(window)
	if var_speed % 50 == 0 and control.flag_pause:
		snake.move(control)
		snake.check_end_window()
		snake.animation()
	var_speed += 1
	pygame.display.flip()

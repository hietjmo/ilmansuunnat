
import pygame
from math import tau
import random
import time

colors = {
  'N': "#3b82f6",
  'E': "#34d399",
  'S': "#fde047",
  'W': "#f43f5e",
  'NE': "#0d9488",
  'SE': "#bef264",
  'SW': "#fb923c",
  'NW': "#d946ef",
  'gray': "#52525b",
}

names = {
  'N': "pohjoinen",
  'E': "itä",
  'S': "etelä",
  'W': "länsi",
  'NE': "koillinen",
  'SE': "kaakko",
  'SW': "lounas",
  'NW': "luode",
  'gray': "ilmansuunnat",
}

blocks = [
  ('NW','N',"NE"),
  ('W', 'gray','E'),
  ('SW','S','SE'),]

situ = {}
situlist = []
for y,block in enumerate (blocks):
  for x,col in enumerate (block):
    if col != 'gray':
      situ [col] = (y,x)
      situlist.append (col)

def hex_to_rgb (hex):
  h = hex.lstrip ('#')
  return tuple (int (h[i:i+2], 16) for i in (0, 2, 4))

def om (name,alpha=255):
  return hex_to_rgb (colors [name]) + (alpha,)

size = 636,636
ct1,ct2 = size[0]/2,size[1]/2
bs1,bs2 = size[0]/3,size[1]/3

pygame.init ()
screen = pygame.display.set_mode (size)
fontname = "fonts/Quicksand-Medium.ttf"
image1 = pygame.image.load ("finland-636x636.png")
font1 = pygame.font.Font (fontname,48)
font2 = pygame.font.Font (fontname,16)
clock = pygame.time.Clock ()
running = True
answer = None
tick = 0
hits = []

def draw_screen (selected,answer,hits1):
  screen.blit (image1, (0,0))
  if selected and selected == answer:
    y,x = situ [selected]
    x1,y1 = bs1*x,bs2*y
    pygame.draw.rect (screen,colors[selected],(x1,y1,bs1,bs2))
  img = font1.render (names[answer],True,om ("gray"))
  rect1 = img.get_rect (center = (ct1,ct2))
  screen.blit (img, rect1)
  img = font2.render (str(hits1)+"/min",True,om ("gray"))
  rect1 = img.get_rect (topleft = (14,14))
  screen.blit (img, rect1)

while running:
  if not (answer):
    answer = random.choice (situlist)
  for event in pygame.event.get ():
    if event.type == pygame.QUIT:
     running = False
  mousex,mousey = pygame.mouse.get_pos ()
  mouseFocus = pygame.mouse.get_focused ()
  selected = None
  if mouseFocus:
    for suunta in situ:
      y,x = situ [suunta]
      x1,y1 = bs1*x,bs2*y
      if x1 < mousex < x1 + bs1 and y1 < mousey < y1 + bs2:
        selected = suunta
  if selected == answer:
    tick = tick + 1
  else:
    tick = 0
  if tick > 5:
    tick = 0
    now = time.time ()
    minute_ago = now - 60.0
    hits.append (now)
    hits = [t for t in hits if minute_ago <= t]
    old_answer = answer
    while old_answer == answer:
      answer = random.choice (situlist)
  draw_screen (selected,answer,len(hits))
  pygame.display.update ()
  clock.tick (10)



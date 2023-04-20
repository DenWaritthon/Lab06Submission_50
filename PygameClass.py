import pygame as pg


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color = 'black'):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color # Height
        self.defaultcolor = color
        # print(color)
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
    def setColor(self,color):
        self.color = color
    def setColorDefault(self):
        self.color = self.defaultcolor
    def posUpdate(self,x,y):
        self.x = self.x + x 
        self.y = self.y + y

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,text=''):
        self.text = text
        Rectangle.__init__(self, x, y, w, h)
    def textButton(self,screen,font):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
        textInButton = font.render(self.text, True, 'black') 
        textRect = (self.x+(self.w//len(self.text)), self.y+(self.h//len(self.text)))
        screen.blit(textInButton,textRect )
    def isMouseOn(self):
        if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0]<=self.x+self.w and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] <= self.y+self.h:
            return True
        else:
            return False
    def isMouseClick(self):
        if pg.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False

class InputBoxExample:

    def __init__(self, x, y, w, h,COLOR_INACTIVE,COLOR_TEXT,FONT, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.colorINACTIVE = COLOR_INACTIVE
        self.colorText = COLOR_TEXT
        self.text = text
        self.font = FONT
        self.txt_surface = FONT.render(text, True, self.colorText)
        self.active = False

    def handle_event(self, event,COLOR_ACTIVE):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else self.colorINACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.colorText) 

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputBox:

    def __init__(self, x, y, w, h,COLOR_INACTIVE,COLOR_TEXT,FONT, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.colorINACTIVE = COLOR_INACTIVE
        self.colorText = COLOR_TEXT
        self.text = text
        self.font = FONT
        self.txt_surface = FONT.render(text, True, self.colorText)
        self.active = False

    def handle_event(self, event,COLOR_ACTIVE,stateCheck = 0):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else self.colorINACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    # self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif stateCheck == 1:
                    if event.unicode.isdigit():
                        self.text += event.unicode
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.colorText) 

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    
    def readText(self):
        return self.text
    
    def resetText(self):
        self.text=''
        self.txt_surface = self.font.render('', True, self.colorText)


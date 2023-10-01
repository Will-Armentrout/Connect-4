import pygame

#Initialize
pygame.init()

#Screen Size
screenWidth = 1000
screenHeight = 1000

#Create Window
window = pygame.display.set_mode((screenWidth, screenHeight))

#Set Name and Clock
pygame.display.set_caption("Connect-4")
clock = pygame.time.Clock()

#Set Fonts
titlefont = pygame.font.SysFont("rockwellextra", 36)

#Get Game Images (Paint Drawings created by me!)
redPiece = pygame.image.load('Red Piece.png')
yellowPiece = pygame.image.load('Yellow Piece.png')
gameBoard = pygame.image.load('Game Board.png')

class Piece(object):
    def __init__(self, width, height, color):
        #Setting the Instance Variables
        self.x = 100
        self.y = 100
        self.fallrate = 5
        self.width = width
        self.height = height
        self.color = color

        #Setting the Color Image of the Piece
        if self.color == 'Red':
            self.img = redPiece
        else:
            self.img = yellowPiece

    #Function to draw the piece on the screen
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        
#Function to Redraw the game window
def redrawGameWindow():
    #Coloring in the Background
    bgColor = (180, 180, 180)
    window.fill(bgColor, (0, 0, screenWidth, screenHeight))
    
    #Drawing the Title
    title = titlefont.render("Connect-4", True, (50, 50, 50))
    window.blit(title, (screenWidth // 2 - title.get_width() // 2, title.get_height() // 2))

    #Drawing the Gameboard
    window.blit(gameBoard, ((screenWidth // 2) - (gameBoard.get_width() // 2), (screenHeight // 2) - (gameBoard.get_height() // 2) + 100))

    yellow.draw(window)
    pygame.display.update()
    
#Main Game Loop

#Initialize Loop Variables
run = True
yellow = Piece(107, 107, 'Yellow')
while run:
    #30 FPS Refresh Rate
    clock.tick(30)

    #Quitting the game using the Quit Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redrawGameWindow()


pygame.quit()
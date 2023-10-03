from typing import Any
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
    def __init__(self, x, y, width, height, color):
        #Setting the Instance Variables
        self.x = x
        self.y = y
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
        window.blit(self.img, (self.x - self.width // 2, self.y - self.height // 2))
        
#Function to Redraw the game window
def redrawGameWindow():
    #Coloring in the Background
    bgColor = (180, 180, 180)
    window.fill(bgColor, (0, 0, screenWidth, screenHeight))
    
    #Drawing the Title
    title = titlefont.render("Connect-4", True, (50, 50, 50))
    window.blit(title, (screenWidth // 2 - title.get_width() // 2, title.get_height() // 2))

    #Drawing the Piece in Play
    for piece in pieces:
        piece.draw(window)

    #Drawing the Gameboard
    window.blit(gameBoard, ((screenWidth // 2) - (gameBoard.get_width() // 2), (screenHeight // 2) - (gameBoard.get_height() // 2) + 100))


    pygame.display.update()

#Function to detect if someone has won
def gameState(board):
    hasEnded = False
    winner = 'none'
    #Looping the Rows
    for i in range(len(board)):
        #Looping the Columns
        for j in range(len(board[0])):
            elem = board[i][j]
            if elem == 'N':
                continue
            else:
                pass
    
    return hasEnded, winner

#Main Game Loop

#Initialize Loop Variables
run = True
isPlaying = True
addPiece = True
isUpdated = False
turn = 'Red'
pieces = []
rows, cols = (6, 7)
board = [['N' for _ in range(cols)] for _ in range(rows)]
while run:
    #30 FPS Refresh Rate
    clock.tick(30)

    #Quitting the game using the Quit Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Getting the Mouse Cursor Position
    mousePos = pygame.mouse.get_pos()

    if addPiece:
        pieces.append(Piece(120, 150, 107, 107, turn))
        addPiece = False

    #Two States of the Game - Selection Amination and Falling Animation
    if isPlaying:
        #Initializing the Piece
        if mousePos[0] < 128 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 120
        elif mousePos[0] < 254 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 246
        elif mousePos[0] < 380 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 372
        elif mousePos[0] < 506 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 498
        elif mousePos[0] < 632 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 624
        elif mousePos[0] < 758 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            xPos = 750
        else:
            xPos = 876

        yPos = 150
        pieces[pieces.__len__() - 1].x = xPos

        if pygame.mouse.get_pressed()[0]:
            isPlaying = False
            pygame.time.delay(150)

    #Need to add collision avoidance if column is full
    else:
        if ~isUpdated:
            if pieces[pieces.__len__() - 1].x == 120 and board[0][0] == 'N':
                for i in range(6):
                    if board[i][0] != 'N':
                        break
                    i += 1
                board[i - 1][0] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 246 and board[0][1] == 'N':
                for i in range(6):
                    if board[i][1] != 'N':
                        break
                    i += 1
                board[i - 1][1] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 372 and board[0][2] == 'N':
                for i in range(6):
                    if board[i][2] != 'N':
                        break    
                    i += 1
                board[i - 1][2] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 498 and board[0][3] == 'N':
                for i in range(6):
                    if board[i][3] != 'N':
                        break 
                    i += 1
                board[i - 1][3] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 624 and board[0][4] == 'N':
                for i in range(6):
                    if board[i][4] != 'N':
                        break
                    i += 1
                board[i - 1][4] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 750 and board[0][5] == 'N':
                for i in range(6):
                    if board[i][5] != 'N':
                        break
                    i += 1
                board[i - 1][5] = turn
                isUpdated = True
            
            elif pieces[pieces.__len__() - 1].x == 876 and board[0][6] == 'N':
                for i in range(6):
                    if board[i][6] != 'N':
                        break
                    i += 1
                board[i - 1][6] = turn
                isUpdated = True
        
        #See current game state
        print(board)
        hasEnded, winner = gameState(board)

        #Display Winner
        if hasEnded:
            if winner == 'Red':
                print('Red Wins')
            else:
                print('Yellow Wins')
            

        #Switch player who's turn it is
        if turn == 'Yellow':
            turn = 'Red'
        else:
            turn = 'Yellow'

        #Switching to the playing state
        addPiece = True
        isUpdated = False
        isPlaying = True


    
    redrawGameWindow()


pygame.quit()
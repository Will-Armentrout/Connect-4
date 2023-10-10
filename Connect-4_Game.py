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

class GameBoard(object):
    def __init__(self, board, numPieces):
        self.board = board
        self.numPieces = numPieces

    def draw(self, window):
        #Drawing the GameBoard
        window.blit(gameBoard, ((screenWidth // 2) - (gameBoard.get_width() // 2), (screenHeight // 2) - (gameBoard.get_height() // 2) + 100))
        
        #Drawing the Pieces already placed
        #Looping through the rows
        for i in range(len(self.board)):
            #Looping the Columns
            for j in range(len(self.board[0])):
                elem = self.board[i][j]
                if elem == 'N':
                    continue
                else:
                    if elem == 'Red':
                        img = redPiece
                    elif elem == 'Yellow':
                        img = yellowPiece
                    
                    row = i 
                    col = j
                    xPosPiece = 120 + j*126
                    yPosPiece = 284 + i*126
                    window.blit(img, (xPosPiece - 107 // 2, yPosPiece - 107 // 2))

    #Finish the Method to find a finished game
    def gameStateCalc(self):
        #Checking Number of Pieces
        if self.numPieces >= 7:
            #Looping through the middle column to check horizontal wins
            for i in range(6):
                cell = self.board[i][3]
                if cell != 'N':
                    
                    #Initializing Loop Variables
                    count = 1

                    #Checking to the Left
                    j = 2
                    while j >= 0:
                        if self.board[i][j] == cell:
                            count += 1
                        else:
                            break
                        j -= 1
                    
                    #Checking to the Right
                    j = 4
                    while j <= 6:
                        if self.board[i][j] == cell:
                            count += 1
                        else:
                            break

                        j += 1
                    
                    #Checking if the row is a winner
                    if count >= 4:
                        print(cell + ' wins.')
            
            #Looping through the third row to check vertical wins
            for i in range(7):
                cell = self.board[3][i]
                if cell != 'N':
                    
                    #Initializing Loop Variables
                    count = 1

                    #Checking Above
                    j = 2
                    while j >= 0:
                        if self.board[j][i] == cell:
                            count += 1
                        else:
                            break
                        j -= 1
                    
                    #Checking Below
                    j = 4
                    while j <= 5:
                        if self.board[j][i] == cell:
                            count += 1
                        else:
                            break

                        j += 1
                    
                    #Checking if the row is a winner
                    if count >= 4:
                        print(cell + ' wins.')
                        break
            
            #Looping through the middle column to check the diagonal wins
            for i in range(6):
                cell = self.board[i][3]
                if cell != 'N':
                    
                    #Initializing Loop Variables
                    count = 1

                    #Checking the Upper Left
                    j = 2
                    row = i - 1
                    while j >= 0 and row >= 0:
                        if self.board[row][j] == cell:
                            count += 1
                        else:
                            break
                        j -= 1
                        row -= 1


                    #Checking the Lower Right
                    j = 4
                    row = i + 1
                    while j >= 0 and row <= 5:
                        if self.board[row][j] == cell:
                            count += 1
                        else:
                            break
                        j += 1
                        row += 1

                    #Checking if the row is a winner
                    if count >= 4:
                        print(cell + ' wins.')
                        break

                    count = 1

                    #Checking the Lower Left
                    j = 2
                    row = i + 1
                    while j >= 0 and row <= 5:
                        if self.board[row][j] == cell:
                            count += 1
                        else:
                            break
                        j -= 1
                        row += 1

                    #Checking the Upper Right
                    j = 4
                    row = i - 1
                    while j <= 6 and row >= 0:
                        if self.board[row][j] == cell:
                            count += 1
                        else:
                            break
                        j += 1
                        row -= 1

                    if count >= 4:
                        print(cell + ' wins.')
                        break


#Function to Redraw the game window
def redrawGameWindow():
    #Coloring in the Background
    bgColor = (180, 180, 180)
    window.fill(bgColor, (0, 0, screenWidth, screenHeight))
    
    #Drawing the Title
    title = titlefont.render("Connect-4", True, (50, 50, 50))
    window.blit(title, (screenWidth // 2 - title.get_width() // 2, title.get_height() // 2))

    #Drawing the Piece in Play
    piece.draw(window)

    #Drawing the Gameboard
    board.draw(window)


    pygame.display.update()

#Main Game Loop

#Initialize Loop Variables
run = True
isPlaying = True
addPiece = True
isUpdated = False
turn = 'Red'
rows, cols = (6, 7)
placedPieces = [['N' for _ in range(cols)] for _ in range(rows)]
board = GameBoard(placedPieces, 0)
while run:
    #30 FPS Refresh Rate
    clock.tick(30)

    #Quitting the game using the Quit Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Game Playing
    if isPlaying:

        #Getting the Mouse Cursor Position
        mousePos = pygame.mouse.get_pos()

        if addPiece:
            piece = Piece(120, 150, 107, 107, turn)
            addPiece = False

        if board.numPieces >= 7:
            board.gameStateCalc()

        #Initializing the Piece
        if mousePos[0] < 128 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 0
        elif mousePos[0] < 254 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 1
        elif mousePos[0] < 380 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 2
        elif mousePos[0] < 506 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 3
        elif mousePos[0] < 632 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 4
        elif mousePos[0] < 758 + (screenWidth // 2) - (gameBoard.get_width() // 2):
            col = 5
        else:
            col = 6

        #Setting the Piece position
        yPos = 150
        xPos = 120 + 126*col
        piece.x = xPos

        #Putting the piece onto the board
        if pygame.mouse.get_pressed()[0] and board.board[0][col] == 'N':
            for i in range(6):
                if board.board[i][col] != 'N':
                    break
                i += 1
            board.board[i - 1][col] = turn

            #Switch player who's turn it is
            if turn == 'Yellow':
                turn = 'Red'
            else:
                turn = 'Yellow'

            #Update loop variables
            addPiece = True
            board.numPieces += 1
            pygame.time.delay(150)

    redrawGameWindow()


pygame.quit()
import pygame
import os.path
import QuizGame


class WelcomeScreen:
    def __init__(self):
        # initializes pygame
        pygame.init()
         # Screen size (x, y)
        self.__screenSize = (640, 480)
        # displays the screen of the screen size
        self.__screen = pygame.display.set_mode(self.__screenSize)
        # initializes the font type
        self.__font = pygame.font.SysFont("Helvetica", 18, bold=False,
                                          italic=False)
        # loads music to play infinitely (until stop)
        try:
            pygame.mixer.music.load(os.path.join('Sounds', 'DoraBackgroundMusic.ogg'))
            pygame.mixer.music.set_volume(.5)
            pygame.mixer.music.play(-1)
        except pygame.error as err:
            print(err)
        # Sets window title
        pygame.display.set_caption("Espanol 215 Vocabulario Juego")
        # Variable the continues or stops game loop
        self.__completed = False

    def __runQuizGame(self, chapter):
        runQuiz = QuizGame.QuizGame()
        if chapter == 1:
            runQuiz.runQuizGame(1)
        elif chapter == 2:
            runQuiz.runQuizGame(2)
        elif chapter == 3:
            runQuiz.runQuizGame(3)
        elif chapter == 4:
            runQuiz.runQuizGame(4)
        else:
            runQuiz.runQuizGame(5)

    def __displayMessage(self):
            # (where to put rectangle, (color), (x, y, width, height)
            # draws rect for "jocelyn's game"
            pygame.draw.rect(self.__screen, (255, 130, 180), (180, 47, 270, 30))
            message = "Spanish 215 Vocabulario Juego"
            messageSurface = self.__font.render(message, True, (0, 0, 0))
            # this draws a source surface onto another surface (screen)
            # surface.blit(surface, (top-left corner coordinates of source))
            self.__screen.blit(messageSurface, (190, 50))

            # draws rect for "Press 1 for Chapter One"
            pygame.draw.rect(self.__screen, (255, 130, 180), (40, 230, 245, 30))
            # Writes message onto rectangle
            chapOneMsg = "Presiona 1 para Capitulo Seis"
            # (text, makes letter smoother (anti alias), color)
            chapOneMsgSurface = self.__font.render(chapOneMsg, True, (0, 0, 0))
            # Puts message onto screen at the points (x, y)
            # (starting at top left corner)
            self.__screen.blit(chapOneMsgSurface, (40, 230))

            # draws rect for "Press 2 for Chapter Two"
            pygame.draw.rect(self.__screen, (255, 130, 180), (70, 120, 245, 30))
            # Writes message onto rectangle
            chapTwoMsg = "Presiona 2 para Capitulo Siete"
            # (text, makes letter smoother (anti alias), color)
            chapTwoMsgSurface = self.__font.render(chapTwoMsg, True, (0, 0, 0))
            # Puts message onto screen at the points (x, y)
            # (starting at top left corner)
            self.__screen.blit(chapTwoMsgSurface, (70, 120))

            # draws rect for "Press 3 for Chapter Three"
            pygame.draw.rect(self.__screen, (255, 130, 180), (250, 170, 245, 30))
            # Writes message onto rectangle
            chapThreeMsg = "Presiona 3 para Capitulo Ocho"
            # (text, makes letter smoother (anti alias), color)
            chapThreeMsgSurface = self.__font.render(chapThreeMsg, True, (0, 0, 0))
            # Puts message onto screen at the points (x, y)
            # (starting at top left corner)
            self.__screen.blit(chapThreeMsgSurface, (250, 170))

            # draws rect for "Press 4 for Chapter Four"
            pygame.draw.rect(self.__screen, (255, 130, 180), (370, 280, 265, 30))
            # Writes message onto rectangle
            chapFourMsg = "Presinoa 4 para Capitulo Nueve"
            # (text, makes letter smoother (anti alias), color)
            chapFourMsgSurface = self.__font.render(chapFourMsg, True, (0, 0, 0))
            # Puts message onto screen at the points (x, y)
            # (starting at top left corner)
            self.__screen.blit(chapFourMsgSurface, (370, 280))

            # draws rect for "Press 5 for Chapter Five"
            pygame.draw.rect(self.__screen, (255, 130, 180), (390, 100, 245, 30))
            # Writes message onto rectangle
            chapFiveMsg = "Presiona 5 para Capitulo Diez"
            # (text, makes letter smoother (anti alias), color)
            chapFiveMsgSurface = self.__font.render(chapFiveMsg, True, (0, 0, 0))
            # Puts message onto screen at the points (x, y)
            # (starting at top left corner)
            self.__screen.blit(chapFiveMsgSurface, (395, 105))

            # draws rect for "Press Q to quit program"
            pygame.draw.rect(self.__screen, (255, 255, 255), (5, 5, 250, 25))
            quitMsg = "Presiona Q para dejar el juego"
            quitMsgSurface = self.__font.render(quitMsg, True, (0, 0, 0))
            self.__screen.blit(quitMsgSurface, (10, 5))

    def __renderHomeScreen(self):
        try:
            # Loads the map background
            homeScreen = pygame.image.load(os.path.join('Images', "Map.jpg"))
            # Scales it to size of screen ((width, height)
            homeScreen = pygame.transform.scale(homeScreen, (640, 480))
            # Puts it onto screen, top left corner is at the points (0, 0)
            self.__screen.blit(homeScreen, (0, 0))
        except pygame.error as err:
                print(err)

        try:
            # loads the dora image and scales it down to correct size
            doraImg = pygame.image.load(os.path.join('Images', "dora.png"))
            doraImg = pygame.transform.scale(doraImg, (120, 200))
            self.__screen.blit(doraImg, (50, 280))
        except pygame.error as err:
            print(err)

    def runWelcomeScreen(self):
            # Game loop
            # While self.__completed == False
            while not self.__completed:
                # Gets the user input because it is an event driven GUI
                for event in pygame.event.get():
                    # If the user quits game by clicking
                    # the 'X' in the corner of screen
                    if event.type == pygame.QUIT:
                        # reassigns self.__completed and terminates loop
                        self.__completed = True
                    # If a key is pressed
                    if event.type == pygame.KEYDOWN:
                        # If 1 key is pressed chapter one function is called
                        if event.key == pygame.K_1:
                            self.__runQuizGame(1)
                        if event.key == pygame.K_2:
                            self.__runQuizGame(2)
                        if event.key == pygame.K_3:
                            self.__runQuizGame(3)
                        if event.key == pygame.K_4:
                            self.__runQuizGame(4)
                        if event.key == pygame.K_5:
                            self.__runQuizGame(5)

                        # If q is pressed, program is exited by reassigning
                        # self.__completed to True and terminating loop
                        if event.key == pygame.K_q:
                            self.__completed = True

                # self.__renderHomeScreen()
                self.__screen.fill((0, 0, 0))
                self.__renderHomeScreen()
                self.__displayMessage()


                # Updates screen with each iteration in the while loop
                pygame.display.update()

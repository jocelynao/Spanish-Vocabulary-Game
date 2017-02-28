import pygame
import os.path
import ChapterOneVocab
import ChapterTwoVocab
import ChapterThreeVocab
import ChapterFourVocab
import ChapterFiveVocab
import random

class QuizGame:
    def __init__(self):
        pygame.init()
        # sets the width and height of screen
        self.__screenSize = (640, 480)
        self.__screen = pygame.display.set_mode(self.__screenSize)
        pygame.display.set_caption("El Juego")
        # loads music to play infinitely (until stop)
        try:
            pygame.mixer.music.load(os.path.join('Sounds', 'DoraBackgroundMusic.ogg'))
            pygame.mixer.music.set_volume(.5)
            pygame.mixer.music.play(-1)
        except pygame.error as err:
            print(err)
        # makes screen white
        self.__screen.fill((0, 0, 0))
        try:
            # Loads the map background
            homeScreen = pygame.image.load(os.path.join('Images', "Background1.png"))
            # Scales it to size of screen ((width, height)
            homeScreen = pygame.transform.scale(homeScreen, (640, 480))
            # Puts it onto screen, top left corner is at the points (0, 0)
            self.__screen.blit(homeScreen, (0, 0))
        except pygame.error as err:
                print(err)
        # used to control the frame rate of game
        self.__clock = pygame.time.Clock()
        self.__score = 0
        self.__state = 1
        self.__answered = "No"
        self.__currentSelection = 0
        self.__correctAnswer = 0
        self.__currentQuestion = 0
        self.__questionCounter = 0

        self.__chapOneVocab = ChapterOneVocab.createDictionary()
        self.__chapTwoVocab = ChapterTwoVocab.createDictionary()
        self.__chapThreeVocab = ChapterThreeVocab.createDictionary()
        self.__chapFourVocab = ChapterFourVocab.createDictionary()
        self.__chapFiveVocab = ChapterFiveVocab.createDictionary()

        self.__chapter = self.__chapOneVocab

        self.__englishWordList = []
        self.__spanishWordList = []
        self.__randomSpanishWord = ""

        self.__answerNumber = random.randint(1, 5)

        # retrieves a font from system.
        # pygame.font.SysFont(name, size, bold=boolean, italic=boolean)
        self.__font = pygame.font.SysFont("Helvetica", 20, bold=True,
                                          italic=False)
        self.__completed = False
        self.__gameOver = False

    def __checkChapter(self):
        if self.__chapter == 1:
            self.__chapter = self.__chapOneVocab

        elif self.__chapter == 2:
            self.__chapter = self.__chapTwoVocab

        elif self.__chapter == 3:
            self.__chapter = self.__chapThreeVocab

        elif self.__chapter == 4:
            self.__chapter = self.__chapFourVocab

        else:
            self.__chapter = self.__chapFiveVocab

    def __findInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            # while the game is playing
            if self.__state == 1:
                self.__answered = "Yes"
                self.__currentSelection = 1

        if keys[pygame.K_2]:
            # while the game is playing
            if self.__state == 1:
                self.__answered = "Yes"
                self.__currentSelection = 2

        if keys[pygame.K_3]:
            # while the game is playing
            if self.__state == 1:
                self.__answered = "Yes"
                self.__currentSelection = 3

        if keys[pygame.K_4]:
            # while the game is playing
            if self.__state == 1:
                self.__answered = "Yes"
                self.__currentSelection = 4

        if keys[pygame.K_q]:
            self.__completed = True

        if keys[pygame.K_RETURN]:
            # after questions is answered correct or incorrect
            if self.__state == 2 or self.__state == 3:
                self.__currentQuestion = 0
                try:
                    del self.__chapter[self.__randomSpanishWord]
                    self.__answerNumber = random.randint(1, 5)
                    self.__state = 1
                    pygame.draw.rect(self.__screen, (255, 255, 255), (0, 100, 640, 30))
                    self.__displayQuestions()
                    self.__displayAnswers()
                except (IndexError or KeyError):
                    self.state = 4
                    self.__completed = True

    def __displayQuestions(self):
        self.__spanishWordList = list(self.__chapter.keys())
        try:
            self.__randomSpanishWord = random.choice(self.__spanishWordList)
            self.__coordinatingEnglishWord = self.__chapter.get(
                    self.__randomSpanishWord)
        except (IndexError or KeyError):
            self.state = 4
            self.__completed = True
        # pygame.draw.rect(screen, color, (x,y,width,height))
        pygame.draw.rect(self.__screen, (255, 255, 255), (150, 40, 400, 30))
        instructionMsg = str(self.__questionCounter + 1) + \
            ". Que es la traduccion correcta?"
        instructionMsgSurface = self.__font.render(instructionMsg, True,
                                                   (0, 0, 0))
        self.__screen.blit(instructionMsgSurface, (150, 40))

        # pygame.draw.rect(screen, color, (x,y,width,height))
        pygame.draw.rect(self.__screen, (180, 0, 211), (150, 150, 320, 30))
        spanishWordMsg = self.__randomSpanishWord
        spanishWordMsgSurface = self.__font.render(spanishWordMsg, True,
                                                   (255, 255, 255))
        self.__screen.blit(spanishWordMsgSurface, (230, 150))

    def __displayAnswers(self):

        if self.__currentQuestion == 0:
            # ensures question choices aren't repeated
            randEngWordOne = random.choice(self.__englishWordList)
            randEngWordTwo = random.choice(self.__englishWordList)
            while randEngWordTwo == randEngWordOne:
                randEngWordTwo = random.choice(self.__englishWordList)
            wrongAnswers = [randEngWordOne, randEngWordTwo]
            randEngWordThree = random.choice(self.__englishWordList)
            while randEngWordThree in wrongAnswers:
                randEngWordThree = random.choice(self.__englishWordList)
            wrongAnswers.append(randEngWordThree)
            while self.__coordinatingEnglishWord in wrongAnswers:
                wrongAnswers =[]
                randEngWordOne = random.choice(self.__englishWordList)
                randEngWordTwo = random.choice(self.__englishWordList)
                while randEngWordTwo == randEngWordOne:
                    randEngWordTwo = random.choice(self.__englishWordList)
                wrongAnswers = [randEngWordOne, randEngWordTwo]
                randEngWordThree = random.choice(self.__englishWordList)
                while randEngWordThree in wrongAnswers:
                    randEngWordThree = random.choice(self.__englishWordList)
                wrongAnswers.append(randEngWordThree)

            if self.__answerNumber == 1:
                choiceOne = "1. " + self.__coordinatingEnglishWord
                choiceTwo = "2. " + randEngWordOne
                choiceThree = "3. " + randEngWordTwo
                choiceFour = "4. " + randEngWordThree
                self.__correctAnswer = 1

            elif self.__answerNumber == 2:
                choiceOne = "1. " + randEngWordOne
                choiceTwo = "2. " + self.__coordinatingEnglishWord
                choiceThree = "3. " + randEngWordTwo
                choiceFour = "4. " + randEngWordThree
                self.__correctAnswer = 2

            elif self.__answerNumber == 3:
                choiceOne = "1. " + randEngWordOne
                choiceTwo = "2. " + randEngWordTwo
                choiceThree = "3. " + self.__coordinatingEnglishWord
                choiceFour = "4. " + randEngWordThree
                self.__correctAnswer = 3

            else:
                choiceOne = "1. " + randEngWordOne
                choiceTwo = "2. " + randEngWordTwo
                choiceThree = "3. " + randEngWordThree
                choiceFour = "4. " + self.__coordinatingEnglishWord
                self.__correctAnswer = 4

            # pygame.draw.rect(screen, color, (x,y,width,height))
            pygame.draw.rect(self.__screen, (0, 191, 255), (0, 200, 640, 30))
            pygame.draw.rect(self.__screen, (0, 191, 255), (0, 250, 640, 30))
            pygame.draw.rect(self.__screen, (0, 191, 255), (0, 300, 640, 30))
            pygame.draw.rect(self.__screen, (0, 191, 255), (0, 350, 640, 30))

            choiceOneSurface = self.__font.render(choiceOne, True, (0, 0, 0))
            choiceTwoSurface = self.__font.render(choiceTwo, True, (0, 0, 0))
            choiceThreeSurface = self.__font.render(choiceThree, True, (0, 0, 0))
            choiceFourSurface = self.__font.render(choiceFour, True, (0, 0, 0))

            self.__screen.blit(choiceOneSurface, (230, 200))
            self.__screen.blit(choiceTwoSurface, (230, 250))
            self.__screen.blit(choiceThreeSurface, (230, 300))
            self.__screen.blit(choiceFourSurface, (230, 350))

            self.__currentQuestion = 1

    def __checkAnswers(self):
        if (self.__currentSelection == self.__correctAnswer) and \
                        self.__state == 1:
            self.__state = 2
            self.__score += 1
            self.__questionCounter += 1

            # pygame.draw.rect(screen, color, (x,y,width,height))
            pygame.draw.rect(self.__screen, (50, 205, 50), (0, 100, 640, 30))
            correctMsg = "Correcto! Presiona ENTER para ver la proxima pregunta"
            correctMsgSurface = self.__font.render(correctMsg, True,
                                                   (255, 255, 255))
            self.__screen.blit(correctMsgSurface, (90, 100))

        if self.__currentSelection != self.__correctAnswer:
            self.__state = 3
            self.__questionCounter += 1

            # pygame.draw.rect(screen, color, (x,y,width,height))
            pygame.draw.rect(self.__screen, (255, 0, 0), (0, 100, 640, 30))
            incorrectMsg = "Es incorrecto! Presiona ENTER para ver la proxima pregunta"
            incorrectMsgSurface = self.__font.render(incorrectMsg, True,
                                                     (255, 255, 255))
            self.__screen.blit(incorrectMsgSurface, (40, 100))

            if self.__answerNumber == 1:
                pygame.draw.rect(self.__screen, (50, 205, 50), (15, 200, 200, 30))
                correctionMsg = "Respuesta correcta:"
                correctionMsgSurface = self.__font.render(correctionMsg, True,
                                                          (255, 255, 255))
                self.__screen.blit(correctionMsgSurface, (20, 200))

            elif self.__answerNumber == 2:
                pygame.draw.rect(self.__screen, (50, 205, 50), (15, 250, 200, 30))
                correctionMsg = "Respuesta Correcta:"
                correctionMsgSurface = self.__font.render(correctionMsg, True,
                                                          (255, 255, 255))
                self.__screen.blit(correctionMsgSurface, (20, 250))

            elif self.__answerNumber == 3:
                pygame.draw.rect(self.__screen, (50, 205, 50), (15, 300, 200, 30))
                correctionMsg = "Respuesta Correcta:"
                correctionMsgSurface = self.__font.render(correctionMsg, True,
                                                          (255, 255, 255))
                self.__screen.blit(correctionMsgSurface, (20, 300))

            else:
                pygame.draw.rect(self.__screen, (50, 205, 50), (15, 350, 200, 30))
                correctionMsg = "Respuesta Correcta:"

                correctionMsgSurface = self.__font.render(correctionMsg, True,
                                                          (255, 255, 255))
                self.__screen.blit(correctionMsgSurface, (20, 350))

        self.__answered = "No"

    # def __deleteQuestion(self):
    #     del self.__chapter[self.__randomSpanishWord]
    #     self.__spanishWordList = list(self.__chapter.keys())
    #     self.__randomSpanishWord = random.choice(self.__spanishWordList)
    #     self.__coordinatingEnglishWord = self.__chapter.get(
    #             self.__randomSpanishWord)
    #     self.__answerNumber = random.randint(1, 5)

    def __displayScore(self):
        # stops scores/lives from overlaying on top of each other
        pygame.draw.rect(self.__screen, (0, 0, 40), (0, 0, 640, 30))
        # creates an image (or surface) with text
        # font.render("text", anti alias, color)
        # anti alias is a boolean and if true has smooth edges on text
        # can have optional background color argument
        fontSurface = self.__font.render("Marcador: " + str(self.__score) +
                                         " / " + str(self.__questionCounter),
                                         True, (255, 255, 255))
        # this draws a source surface onto another surface (screen)
        # surface.blit(source surface, (top-left corner coordinates of source))
        self.__screen.blit(fontSurface, (235, 5))

    def runQuizGame(self, chapter):
        while not self.__completed and not self.__gameOver:
            # determines if user wants to quit or continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__completed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.__completed = True

            # pygame.event.get() makes sure that the windows
            # do not pile up while game is running.
            # If the event that the user clicks is pygame.QUIT
            # it will stop the game or end the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__completed = True

            # sets frame rate to no more than 50 frames per second
            self.__clock.tick(50)
            self.__chapter = chapter
            self.__checkChapter()
            
            if self.__englishWordList == []:
                    self.__englishWordList = list(self.__chapter.values())

            self.__findInput()

            if self.__currentQuestion == 0:
                self.__displayQuestions()
                self.__displayAnswers()
                # self.__deleteQuestion()
            if self.__answered == "Yes":
                self.__checkAnswers()

            # displays the score
            self.__displayScore()

            # the pygame.display.flip() allows for any changes you make
            # in the code to become visible on the window (updates screen)
            # the pygame.display.flip() makes changes visible. I created two
            # different colors so we can see the movement / stop overlaying
            pygame.display.flip()

        while self.__completed and not self.__gameOver:
            # determines if user wants to quit or continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.__gameOver = True

            # pygame.event.get() makes sure that the windows
            # do not pile up while game is running.
            # If the event that the user clicks is pygame.QUIT
            # it will stop the game or end the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__gameOver = True

            # sets frame rate to no more than 50 frames per second
            self.__clock.tick(50)

            self.__screen.fill((255, 255, 255))
            completeMsg1 = "Tu has completado este capitulo!"
            completeMsg2 = "Presiona Q para regresar al menu principal"
            completeMsg1Surface = self.__font.render(completeMsg1, True, (0, 0, 0))
            completeMsg2Surface = self.__font.render(completeMsg2, True, (0, 0, 0))
            self.__screen.blit(completeMsg1Surface, (90, 100))
            self.__screen.blit(completeMsg2Surface, (90, 130))

            # displays the score
            self.__displayScore()

            pygame.display.flip()

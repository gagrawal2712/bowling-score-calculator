import constant

class gameScore:

    def __init__(self, frameCount=10):
        self.lastFrameNumber = frameCount
        self.rollingFrame = 1
        self.totalScore = 0
        self.frameScores = []
        self.state = constant.ROLLING_FIRST_BALL
        self.firstBallInFrame = 0
    
    def frameNumber(self) -> int:
        if(len(self.frameScores) == self.lastFrameNumber):
            return self.lastFrameNumber+1
        elif(self.rollingFrame > self.lastFrameNumber):
            return self.lastFrameNumber
        else:
            return self.rollingFrame
    
    def scoreSoFar() -> int:
        if(len(self.frameScores) == self.lastFrameNumber):
            return self.frameScores[self.lastFrameNumber-1]
        else:
            return self.totalScore
    
    def gameIsOver(self) -> bool:
        return self.frameNumber() > self.lastFrameNumber
    
    def addFrame(self, toAdd):
        self.totalScore = self.totalScore + toAdd
        if(len(self.frameScores) < self.lastFrameNumber):
            self.frameScores.append(self.totalScore)
    
    def roll(self, ball):
        if(self.state == constant.ROLLING_FIRST_BALL):
            if(ball == 10):
                self.rollingFrame += 1
                self.state = constant.STRIKE_LAST_BALL
            else:
                self.firstBallInFrame = ball
                self.state = constant.ROLLING_SECOND_BALL
        elif(self.state == constant.ROLLING_SECOND_BALL):
            if(self.firstBallInFrame + ball == 10):
                self.rollingFrame += 1
                self.state = constant.SPARE_LAST_BALL
            else:
                self.rollingFrame += 1
                self.addFrame(self.firstBallInFrame + ball)
                self.state = constant.ROLLING_FIRST_BALL
        elif(self.state == constant.SPARE_LAST_BALL):
            self.addFrame(10+ball)
            if(ball == 10):
                self.rollingFrame += 1
                self.state = constant.STRIKE_LAST_BALL
            else:
                self.firstBallInFrame = ball
                self.state = constant.ROLLING_SECOND_BALL
        elif(self.state == constant.STRIKE_LAST_BALL):
            if(ball == 10):
                self.rollingFrame += 1
                self.state = constant.TWO_CONSEC_STRIKES
            else:
                self.firstBallInFrame = ball
                self.state = constant.STRIKE_2_BALLS_AGO
        elif(self.state == constant.TWO_CONSEC_STRIKES):
            self.addFrame(20+ball)
            if(ball == 10):
                self.rollingFrame += 1
            else:
                self.firstBallInFrame = ball
                self.state = constant.STRIKE_2_BALLS_AGO
        elif(self.state == constant.STRIKE_2_BALLS_AGO):
            self.addFrame(10+self.firstBallInFrame+ball)
            if(self.firstBallInFrame+ball == 10):
                self.rollingFrame += 1
                self.state = constant.SPARE_LAST_BALL
            else:
                self.rollingFrame += 1
                self.addFrame(self.firstBallInFrame+ball)
                self.state = constant.ROLLING_FIRST_BALL
        else:
            raise Exception("Invalid state: " + self.state)
        return self.frameScores



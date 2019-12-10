class Game():


    

        def play():
            print ('Welcome to the Game of Greed')
            answer = str.lower(input('Wanna play?'))
            if answer == "y":
                print ('Great! Check back tomorrow :D')
            else:
                print ('OK. Maybe another time')
        
        # def roll_dice():
        #     count = 0
        #   

        def calculate_score(value=0, count=0):
            
            if value == 1:
                    if (count == 1 or count == 2):
                        score += 100*count
                    if count == 3:
                        score = 1000
                    if count == 4:
                        score = 2000
                    if count == 5:
                        score = 3000
                    if count == 6:
                        score = 4000
                
                    if value == 2:
                        if count == 3:
                            score = 200
                        if count == 4:
                            score = 400
                        if count == 5:
                            score = 800
                        if count == 6:
                            score = 1200

                    if value == 3:
                        if count == 3:
                            score = 300
                        if count == 4:
                            score = 600
                        if count == 5:
                            score = 1200
                        if count == 6:
                            score = 1800

                    if value == 4:
                        if count == 3:
                            score = 400
                        if count == 4:
                            score = 800
                        if count == 5:
                            score = 1600
                        if count == 6:
                            score = 2400

                    if value == 5:
                        if count == 1 or count == 2:
                            score += 50*count
                        if count == 3:
                            score = 500 
                        if count == 4:
                            score = 1000
                        if count == 5:
                            score = 2000
                        if count == 6:
                            score = 3000

                    if value == 6:
                        if count == 3:
                            score = 600 
                        if count == 4:
                            score = 1200
                        if count == 5:
                            score = 2400
                        if count == 6:
                            score = 3600 


        play()
        calculate_score()
        # roll_dice()

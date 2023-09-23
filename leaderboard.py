import csv

class Leaderboard:
    def __init__(self, filename="lb.csv"):
        self.filename = filename
        self.data = []

    # Loads the data from the csv file

    def load(self):
        self.data = []

        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in f:
                self.data.append(row)



    '''
    Write the save function that saves all the scores to the CSV file 
    in highest to lowest scores.
    '''
    def save(self):
        #write your code here
        pass


    '''
    Write the update function, 
    if the player already exists in the file then update the higher score
    else add a new row to the end of the file with name and score as columns
    '''
    def update(self, player_name, player_score):
        self.load()
        #write your code hear
        self.save()


    '''
    Display the scores of each and every person in the leaderboard
    '''
    def display(self):
        pass



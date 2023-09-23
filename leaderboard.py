import csv

class Leaderboard:
    def __init__(self, filename="lb.csv"):
        self.filename = filename
        self.data = []

    '''
    Write the load function,
    it should read the data in the csv file,
    and append a dictionary of {name, score} in the list - data
    '''
    def load(self):
        self.data = []
        #write your code here
        pass



   # Saves the output

    def save(self):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for row in self.data:
                writer.writerow(row)


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



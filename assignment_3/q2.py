class Simple_Train_Agent():
    def __init__(self):
        self.rules={
            # the set of rules according to which our agent will work
            ("Detected", "Clear", "Neutral"): {"Signal": "Green", "Gate": "Lower", "Siren": "On"},
            ("Detected", "Detected", "Neutral"): {"Signal": "Red", "Gate": "Raise", "Siren": "On"},
            
            ("Detected", "Clear", "Active"): {"Signal": "Red", "Gate": "Raise", "Siren": "On"},
            ("Detected", "Detected", "Active"): {"Signal": "Red", "Gate": "Raise", "Siren": "On"},
            ("Not_Detected", "Clear", "Active"): {"Signal": "Red", "Gate": "Raise", "Siren": "On"},
            
            ("Not_Detected", "Clear", "Neutral"): {"Signal": "Red", "Gate": "Raise", "Siren": "Off"},
            ("Not_Detected", "Detected", "Neutral"): {"Signal": "Red", "Gate": "Raise", "Siren": "Off"},
           
        }
        self.env={
            # default environment
            "Train":"Detected",
            "Obstacle":"Clear",
            "Emergency":"Neutral"
        }
    def sensors(self):
        # returns the correct status the situation
        return (self.env["Train"],self.env["Obstacle"],self.env["Emergency"])
    def act(self):
        # gets the percepts
        percepts=self.sensors()
        # matches with the rules set and gets the action
        action=self.rules.get(percepts)
        
        if action:
            print(f"current state:{percepts}")
            print(f"Action taken: signal:{action['Signal']},gate:{action['Gate']},siren:{action['Siren']}")
        
Agent=Simple_Train_Agent()
Agent.act()
# here we need priorities as if the emergency switch is on we dont care about the obstacle and we will stop regardless and not move ahead
# next in the priority we would have the Obstacle detector and the last one we have the Train detector 
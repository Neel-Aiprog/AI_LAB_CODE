class SimpleReflexAgent:
    def __init__(self):
        # The rules according to which the agent will work
        self.rules = {
            ("A", "Ghanda"): "Suck",
            ("A", "Saaf"): "Right",
            ("B", "Ghanda"): "Suck",
            ("B", "Saaf"): "Right",
            ("C", "Ghanda"): "Suck",
            ("C", "Saaf"): "Left",
        }
        
        self.env = {
            "A": "Ghanda",
            "B": "Ghanda",
            "C": "Ghanda"
        }
        self.location = "A"#defining the starting point
        self.score = 0 #defining the score  according to which we will rate our agent

    def sensors(self):
        # The agent senses its location and status of that location 
        return (self.location, self.env[self.location])

    def act(self, action):
        if action == "Suck":
            print(f"Action: Sucking in {self.location}")
            self.env[self.location] = 'Saaf'
            self.score += 5
            
        elif action == "Right":
            print("Action: Agent moving right")
            self.score += 1
            if self.location == "A":
                self.location = "B"
            elif self.location == "B":
                self.location = "C"
                
        elif action == "Left":
            print("Action: Agent moving Left")
            self.score += 1
            if self.location == "C":
                self.location = "B"
            elif self.location == "B":
                self.location = "A"


    def run_simulation(self, steps):
        print(f"Starting Environment: {self.env}")
        print("============================================================================" )

        for i in range(steps):
            # get percepts from the environment
            percept = self.sensors()
            location, status = percept
        
            # match the rule according to current status
            action = self.rules.get(percept)
        
            # action to be performed by the agent
            print(f"{i+1} | {location} | {status} | {action}")
            self.act(action) 

        print(f"Final Environment: {self.env}")
        print(f"Total Performance Score: {self.score}")

# Run the agent
agent = SimpleReflexAgent()
agent.run_simulation(steps=5)

# i think so we dont need priority in this question !! as we are not sending multiple signals our agent is only working on one signal and is giving one output

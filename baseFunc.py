# Topic classes
class topicList():

    class Energy_us:
        name = "Energy Us"
        values= {"electricity": float, "gas": float, "fuel": float}
        
        def get_questions():
            questions ={}
            bills = {"electricity" : "electricity bill", "gas": "natural gas bill", "fuel": "fuel bill for transportation"}
            
            for bill in bills:
                questions[bill] = (f'What is your average monthly {bills[bill]} in euros?')
            return questions

        questions = get_questions()
        def calc_result(self, values):
            return values["electricity"] * 12 * 0.0005 + values["gas"] * 12 * 0.0053 + values["fuel"] * 12 *2.32

    class Waste:
        name="Waste"
        values = {"waste" : float, "recycling" : float}

        questions={"waste" : "How much waste do you generate per month in kilograms?",
                    "recycling" : "How much of that waste is recycled or composted (in percentage)?"}

        def calc_result(self, values):
            return values["waste"] * 12 * 0.57 - values["recycling"]

    class Business_travel:
        name="Business Travel"
        values = {"km_travel" : float, "fuel" : float}

        questions ={
            "km_travel" : "How many kilometers do your employee travel per year for business purpose?",
            "fuel" : "What is the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers(L/100km)?"
            }
        
        def calc_result(self, values):
            return values["km_travel"] * 1 / values["fuel"] * 2.31

    # list of topics
    topics = [Energy_us, Waste, Business_travel]

# Validation functions and error messages
class validations():

    def validation_float(data):
        try: float(data)
        except: return False
        return True

    def validation_int(data):
        try: int(data)
        except: return False
        return True

    def validation_numeric_range(data,min,max):
        if (data <= max and data >= min):
            return True
        else: False

        # Wrong format message
    def wrong_format(data) :
        msg=f"Entered \"{data}\" is not valid format. \n!!! Please enter only digits"
        return msg

        # Wrong range message
    def wrong_range(min,max) :
        msg=f"Entered data must be between {min} and {max}"
        return msg

#  method to validate and return result of calculation
def getTopicResult(selected_topic):
    
    for question in selected_topic.questions:
        print(selected_topic.questions[question])
    
        while(True):
            value = input("Enter value = ")
            
            if(not validations.validation_float(value)):
                print(validations.wrong_format(value))
                continue

            selected_topic.values[question] = float(value)
            break

    carbon_footprint = round(float(selected_topic.calc_result(selected_topic.values)),4)
    return carbon_footprint
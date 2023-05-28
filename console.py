from baseFunc import *

topics = topicList.topics
results = {}

while(len(topics) != 0):

    print("\n Choose one of the option by entering index number")

    for i in range(0, len(topics)):
        print(f"{i+1}. {topics[i].name}")

    selected_series = input("Select topic= ")

    # Validate and request, re-enter selected topic
    while(True):

        if(not validations.validation_int(selected_series)):
            print(validations.wrong_format(selected_series))
            selected_series = input("Enter again = ")
            continue
        else:
            selected_series = int(selected_series)

            if(not validations.validation_numeric_range(selected_series, 1, len(topics))):
                print(validations.wrong_range(1, len(topics)))
                selected_series = input("Enter again = ")
                continue
        break

    # Get selected topic questions
    selected_topic = topicList.topics[int(selected_series)-1]()

    result = getTopicResult(selected_topic)

    print(f"* {selected_topic.name} - Carbon Footprint is {result} (kgCO2)")

    results[topics[selected_series-1]] = result
    del topics[selected_series-1]

for i in results:
    print(i.name, i.values ,results[i] )

print("All is done! you can find summary report in file. Thank you.")

    




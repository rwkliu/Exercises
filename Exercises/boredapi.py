import requests

random_activities_url = "https://bored-api.appbrewery.com/random"

activities = set()


def getActivity():
    activity = requests.get(random_activities_url)

    if activity.status_code == 200:
        activity_json = activity.json()
        print(activity_json)
        if activity_json not in activities:
            print("activity is not in the list")
            activities.add(activity_json)


getActivity()
print(activities)

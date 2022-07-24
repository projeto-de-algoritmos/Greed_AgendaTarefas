from userInterface import TelaAgenda
from event import Event
from greedyAlgorithm import interval_scheduling


if __name__ == "__main__":
    events = TelaAgenda.start()
    # print all events and their start and end time
    for event in events:
        print(event)

    # schedule events
    schedule = interval_scheduling(events)
    print("\n\n\n")
    print("Schedule:")
    for event in schedule:
        print(event)
    print("\n\n\n")

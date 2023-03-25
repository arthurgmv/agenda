import PySimpleGUI as sg

agenda = []

def add_event(values):
    name = values["name"]
    date = values["date"]
    time = values["time"]
    description = values["description"]

    event = {"name": name, "date": date, "time": time, "description": description}
    agenda.append(event)

def view_events():
    if not agenda:
        sg.popup("There are no events in the agenda.")
    else:
        events = []
        for event in agenda:
            events.append([event["name"], event["date"], event["time"], event["description"]])
        window = sg.Window("Agenda - View events", [[sg.Table(values=events, headings=["Name", "Date", "Time", "Description"])], [sg.Button("Ok")]])
        event, values = window.read()
        window.close()

def delete_event(values):
    if not agenda:
        sg.popup("There are no events in the agenda.")
    else:
        event_to_delete = int(values["events"])
        if event_to_delete < 1 or event_to_delete > len(agenda):
            sg.popup("Invalid event.")
        else:
            del agenda[event_to_delete - 1]
            sg.popup("Event successfully deleted.")

sg.theme("reddit")

layout = [[sg.Text("--- Agenda ---", font=("Helvetica", 20))],
          [sg.Text("1 - Add event", font=("Helvetica", 14))],
          [sg.Text("Name:", size=(10, 1)), sg.InputText(key="name")],
          [sg.Text("Date (format MM/DD/YYYY):", size=(25, 1)), sg.InputText(key="date")],
          [sg.Text("Time (format HH:MM):", size=(20, 1)), sg.InputText(key="time")],
          [sg.Text("Description:", size=(10, 1)), sg.Multiline(key="description", size=(40, 5))],
          [sg.Button("Add", size=(10, 1))],
          [sg.Text("2 - View events", font=("Helvetica", 14))],
          [sg.Button("View", size=(10, 1))],
          [sg.Text("3 - Delete event", font=("Helvetica", 14))],
          [sg.Text("Select the event to delete:", size=(30, 1)), sg.Combo(values=[str(i+1) for i in range(len(agenda))], key="events", size=(10, 1))],
          [sg.Button("Delete", size=(10, 1))],
          [sg.Text("4 - Quit", font=("Helvetica", 14))],
          [sg.Button("Quit", size=(10, 1))]]

window = sg.Window("Agenda", layout)

while True:
    event, values = window.read()

    if event == "Add":
        add_event(values)
        sg.popup("Event successfully added.")
    elif event == "View":
        view_events()
    elif event == "Delete":
        delete_event(values)
        sg.popup("Event successfully deleted.")
    elif event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()

import tkinter as tk
from tkinter import messagebox
import random

class WasteReport:
    def __init__(self, location, description, severity, waste_type, priority_area, reporter):
        self.location = location
        self.description = description
        self.severity = severity
        self.waste_type = waste_type
        self.priority_area = priority_area
        self.reporter = reporter
        self.report_date = self.get_current_date()

    def get_current_date(self):
        from datetime import datetime
        return datetime.now().strftime("%d-%m-%Y")

def get_waste_management_tips():
    tips = [
        "Reduce single-use plastics by using reusable items.",
        "Properly separate recyclables and non-recyclables.",
        "Avoid burning waste, as it can release toxic gases.",
        "Compost organic waste to reduce landfill waste.",
        "Educate others about the importance of waste management."
    ]
    return random.choice(tips)

class CleanupEvent:
    def __init__(self, event_name, location, event_date, organizer):
        self.event_name = event_name
        self.location = location
        self.event_date = event_date
        self.organizer = organizer

class CleanupEventManager:
    def __init__(self):
        self.events = []

    def create_event(self, event):
        self.events.append(event)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Neighborhood Clean-Up Hub")
        self.geometry("600x400")
        self.config(bg="lightgreen")
        self.waste_reports = []
        self.event_manager = CleanupEventManager()  
        
        self.create_widgets()

    def create_widgets(self):
        self.tip_label = tk.Label(self, text=get_waste_management_tips(), font=("Helvetica", 12, "italic"), bg="lightgreen", wraplength=500)
        self.tip_label.pack(pady=10)

        self.menu_frame = tk.Frame(self, bg="lightgreen")
        self.menu_frame.pack(pady=20)

        self.report_button = tk.Button(self.menu_frame, text="Report Waste", width=20, command=self.report_waste, bg="green", fg="white", font=("Helvetica", 12))
        self.report_button.grid(row=0, column=0, padx=10, pady=5)

        self.view_reports_button = tk.Button(self.menu_frame, text="View Waste Reports", width=20, command=self.view_waste_reports, bg="green", fg="white", font=("Helvetica", 12))
        self.view_reports_button.grid(row=0, column=1, padx=10, pady=5)

        self.event_button = tk.Button(self.menu_frame, text="Create Cleanup Event", width=20, command=self.create_cleanup_event, bg="green", fg="white", font=("Helvetica", 12))
        self.event_button.grid(row=1, column=0, padx=10, pady=5)

        self.view_event_button = tk.Button(self.menu_frame, text="View Cleanup Events", width=20, command=self.view_cleanup_events, bg="green", fg="white", font=("Helvetica", 12))
        self.view_event_button.grid(row=1, column=1, padx=10, pady=5)

        self.view_priority_button = tk.Button(self.menu_frame, text="View Priority Areas", width=20, command=self.view_priority_areas, bg="green", fg="white", font=("Helvetica", 12))
        self.view_priority_button.grid(row=2, column=0, padx=10, pady=5)

    def report_waste(self):
        report_window = tk.Toplevel(self)
        report_window.title("Report Waste")
        report_window.geometry("400x400")
        report_window.config(bg="lightgreen")  

        tk.Label(report_window, text="Report Waste", font=("Helvetica", 16, "bold"), bg="lightgreen", fg="darkgreen").pack(pady=10)

        tk.Label(report_window, text="Location of Waste:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        location_entry = tk.Entry(report_window, width=40)
        location_entry.pack(pady=5)

        tk.Label(report_window, text="Description of Waste:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        description_entry = tk.Entry(report_window, width=40)
        description_entry.pack(pady=5)

        tk.Label(report_window, text="Severity Level (1: Minor, 2: Moderate, 3: Severe):", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        severity_entry = tk.Entry(report_window, width=40)
        severity_entry.pack(pady=5)

        tk.Label(report_window, text="Waste Type (e.g. Organic, Plastic):", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        waste_type_entry = tk.Entry(report_window, width=40)
        waste_type_entry.pack(pady=5)

        tk.Label(report_window, text="Your Name:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        reporter_entry = tk.Entry(report_window, width=40)
        reporter_entry.pack(pady=5)

        submit_button = tk.Button(report_window, text="Submit", bg="darkgreen", fg="white", font=("Helvetica", 12, "bold"), width=15)
        submit_button.pack(pady=20)

        def submit_report():
            location = location_entry.get()
            description = description_entry.get()
            severity = severity_entry.get()
            waste_type = waste_type_entry.get()
            reporter = reporter_entry.get()
            priority_area = "Low" if severity == "1" else "Medium" if severity == "2" else "High"
            
            if location and description and severity and waste_type and reporter:
                report = WasteReport(location, description, severity, waste_type, priority_area, reporter)
                self.waste_reports.append(report)
                messagebox.showinfo("Success", "Waste report added successfully!")
                report_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        submit_button.config(command=submit_report)

    def view_waste_reports(self):
        reports_window = tk.Toplevel(self)
        reports_window.title("View Waste Reports")
        reports_window.geometry("500x400")
        reports_window.config(bg="lightgreen")  

        if not self.waste_reports:
            tk.Label(reports_window, text="No reports available.", font=("Helvetica", 14), bg="lightgreen").pack(pady=20)
        else:
            for report in self.waste_reports:
                report_text = f"Location: {report.location}\nDescription: {report.description}\nSeverity: {report.severity}\nWaste Type: {report.waste_type}\nPriority: {report.priority_area}\nReported by: {report.reporter}\nDate: {report.report_date}\n\n"
                tk.Label(reports_window, text=report_text, justify="left", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)

    def create_cleanup_event(self):
        event_window = tk.Toplevel(self)
        event_window.title("Create Cleanup Event")
        event_window.geometry("400x300")
        event_window.config(bg="lightgreen")  

        tk.Label(event_window, text="Create Cleanup Event", font=("Helvetica", 16, "bold"), bg="lightgreen", fg="darkgreen").pack(pady=10)

        tk.Label(event_window, text="Event Name:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        event_name_entry = tk.Entry(event_window, width=40)
        event_name_entry.pack(pady=5)

        tk.Label(event_window, text="Event Location:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        event_location_entry = tk.Entry(event_window, width=40)
        event_location_entry.pack(pady=5)

        tk.Label(event_window, text="Event Date (dd-mm-yyyy):", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        event_date_entry = tk.Entry(event_window, width=40)
        event_date_entry.pack(pady=5)

        tk.Label(event_window, text="Organizer Name:", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)
        organizer_entry = tk.Entry(event_window, width=40)
        organizer_entry.pack(pady=5)

        submit_button = tk.Button(event_window, text="Submit", bg="darkgreen", fg="white", font=("Helvetica", 12, "bold"), width=15)
        submit_button.pack(pady=20)

        def submit_event():
            event_name = event_name_entry.get()
            event_location = event_location_entry.get()
            event_date = event_date_entry.get()
            organizer = organizer_entry.get()

            if event_name and event_location and event_date and organizer:
                event = CleanupEvent(event_name, event_location, event_date, organizer)
                self.event_manager.create_event(event)
                messagebox.showinfo("Success", "Cleanup event created successfully!")
                event_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        submit_button.config(command=submit_event)

    def view_cleanup_events(self):
        event_window = tk.Toplevel(self)
        event_window.title("View Cleanup Events")
        event_window.geometry("500x400")
        event_window.config(bg="lightgreen")  
    
        if not self.event_manager.events:
            tk.Label(event_window, text="No events available.", font=("Helvetica", 14), bg="lightgreen").pack(pady=20)
        else:
            # Loop through all events and display them
            for event in self.event_manager.events:
                event_text = f"Event: {event.event_name}\nLocation: {event.location}\nDate: {event.event_date}\nOrganizer: {event.organizer}\n\n"
                tk.Label(event_window, text=event_text, justify="left", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)

    def view_priority_areas(self):
        area_window = tk.Toplevel(self)
        area_window.title("View Priority Areas")
        area_window.geometry("500x400")
        area_window.config(bg="lightgreen")  
        
        if not self.waste_reports:
            tk.Label(area_window, text="No reports available.", font=("Helvetica", 14), bg="lightgreen").pack(pady=20)
        else:
            low_priority = [report for report in self.waste_reports if report.severity == "1"]
            medium_priority = [report for report in self.waste_reports if report.severity == "2"]
            high_priority = [report for report in self.waste_reports if report.severity == "3"]
            
            if low_priority:
                tk.Label(area_window, text="Low Priority Areas:", font=("Helvetica", 14, "bold"), bg="lightgreen").pack(pady=10)
                for report in low_priority:
                    tk.Label(area_window, text=f"Location: {report.location}", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)

            if medium_priority:
                tk.Label(area_window, text="Medium Priority Areas:", font=("Helvetica", 14, "bold"), bg="lightgreen").pack(pady=10)
                for report in medium_priority:
                    tk.Label(area_window, text=f"Location: {report.location}", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)

            if high_priority:
                tk.Label(area_window, text="High Priority Areas:", font=("Helvetica", 14, "bold"), bg="lightgreen").pack(pady=10)
                for report in high_priority:
                    tk.Label(area_window, text=f"Location: {report.location}", font=("Helvetica", 12), bg="lightgreen").pack(pady=5)

if __name__ == "__main__":
    app = Application()
    app.mainloop()

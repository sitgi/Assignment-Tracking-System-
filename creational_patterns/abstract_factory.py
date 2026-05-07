class StudentDashboard:
    def display(self):
        return "Student Dashboard"

class LecturerDashboard:
    def display(self):
        return "Lecturer Dashboard"

class DashboardFactory:
    def create_dashboard(self, type):
        if type == "student":
            return StudentDashboard()
        elif type == "lecturer":
            return LecturerDashboard()

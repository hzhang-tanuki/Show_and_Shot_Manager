import sys
import os
import json
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QMessageBox, QDialog, QDialogButtonBox, QFrame


shows_main_dir = "D:/Shows"
"""
 Create directory in D:/
"""
if not os.path.exists(shows_main_dir):
    os.makedirs(shows_main_dir)


class Show:

    def __init__(self, title, description, start_date, end_date):
        """
        @param title: string - title of the show, also name of the show folder
        @param description: string - description of the show
        @param start_date: string -
        @param end_date: string -
        """
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def create_show_directory(self):
        show_dir = f"D:/Shows/{self.title}"
        os.makedirs(show_dir)
        return show_dir

    def save_show_data(self, show_dir):
        """
        @param show_dir: string - show directory
        @return: None

        """
        show_data = {
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        with open(f"{show_dir}/show_data.json", "w") as file:
            json.dump(show_data, file)

    @staticmethod
    def get_all_shows():
        shows = []
        show_dirs = os.listdir("D:/Shows")
        for show_dir in show_dirs:
            show_data_file = f"D:/Shows/{show_dir}/show_data.json"
            if os.path.isfile(show_data_file):
                with open(show_data_file, "r") as file:
                    show_data = json.load(file)
                    shows.append(show_data)
        return shows

    @staticmethod
    def get_show(title):
        """
        @param title: string - show title, also folder name
        @return: None

        """
        show_dirs = os.listdir("D:/Shows")
        for show_dir in show_dirs:
            show_data_file = f"D:/Shows/{show_dir}/show_data.json"
            if os.path.isfile(show_data_file):
                with open(show_data_file, "r") as file:
                    show_data = json.load(file)
                    if show_data["title"] == title:
                        return show_data

    @staticmethod
    def update_show(title, updated_data):
        """
        @param title: string - show title, also folder name
        @param updated_data: library - information about the show
        @return:boolean - if the data is updated

        """
        show_dirs = os.listdir("D:/Shows")
        for show_dir in show_dirs:
            show_data_file = f"D:/Shows/{show_dir}/show_data.json"
            if os.path.isfile(show_data_file):
                with open(show_data_file, "r") as file:
                    show_data = json.load(file)
                    if show_data["title"] == title:
                        show_data.update(updated_data)
                        with open(show_data_file, "w") as update_file:
                            json.dump(show_data, update_file)
                        return True
        return False

    @staticmethod
    def delete_show(title):
        """
        @param title: string - show title, also folder name
        @return: if the show is deleted

        """
        show_dir = f"D:/Shows/{title}"
        if os.path.isdir(show_dir):
            shutil.rmtree(show_dir)
            return True
        return False


class Shot:
    def __init__(self, show_title, shot_id, sequence_number, duration, description):
        """
        @param show_title: string - show title which the shot belongs to
        @param shot_id: string - shot name
        @param sequence_number: string - 
        @param duration: string - 
        @param description: string - 

        """
        self.show_title = show_title
        self.shot_id = shot_id
        self.sequence_number = sequence_number
        self.duration = duration
        self.description = description

    def create_shot_directory(self):
        shot_dir = f"D:/Shows/{self.show_title}/Shots/{self.shot_id}"
        os.makedirs(shot_dir)
        return shot_dir

    def save_shot_data(self, shot_dir):
        """
        @param shot_dir: string - shot name
        @return: None

        """
        shot_data = {
            "shot_id": self.shot_id,
            "sequence_number": self.sequence_number,
            "duration": self.duration,
            "description": self.description
        }
        with open(f"{shot_dir}/shot_data.json", "w") as file:
            json.dump(shot_data, file)

    @staticmethod
    def get_all_shots(title):
        """

        @param title: string - show title which the shot belongs to
        @return: list - list of info of the shotfrom the file
        """
        shots = []
        shot_dir = f"D:/Shows/{title}/Shots"
        if os.path.isdir(shot_dir):
            shot_dirs = os.listdir(shot_dir)
            for shot_title in shot_dirs:
                shot_data_file = f"{shot_dir}/{shot_title}/shot_data.json"
                if os.path.isfile(shot_data_file):
                    with open(shot_data_file, "r") as file:
                        shot_data = json.load(file)
                        shots.append(shot_data)
        return shots

    @staticmethod
    def get_shot(title, shot_title):
        """
        @param title: string - show title which the shot belongs to
        @param shot_title: string - shot_id
        @return: list - info from the shot file

        """
        shot_dir = f"D:/Shows/{title}/Shots/{shot_title}"
        shot_data_file = f"{shot_dir}/shot_data.json"
        if os.path.isfile(shot_data_file):
            with open(shot_data_file, "r") as file:
                shot_data = json.load(file)
                return shot_data

    @staticmethod
    def update_shot(title, shot_title, updated_data):
        """
        @param title: string - show title which the shot belongs to
        @param shot_title: string - shot id
        @param updated_data: list - new info of the shot
        @return: boolean - signal indicate if update successful

        """
        shot_dir = f"D:/Shows/{title}/Shots/{shot_title}"
        shot_data_file = f"{shot_dir}/shot_data.json"
        if os.path.isfile(shot_data_file):
            with open(shot_data_file, "r") as file:
                shot_data = json.load(file)
                shot_data.update(updated_data)
                with open(shot_data_file, "w") as update_file:
                    json.dump(shot_data, update_file)
                return True
        return False

    @staticmethod
    def delete_shot(title, shot_id):
        """
        @param title: string - show title which the shot belongs to
        @param shot_id: string - shot id
        @return: boolean - signal indicate if delete successful

        """
        shot_dir = f"D:/Shows/{title}/Shots/{shot_id}"
        if os.path.isdir(shot_dir):
            shutil.rmtree(shot_dir)
            return True
        return False


class CreateShowDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Show")
        self.setModal(True)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.title_label = QLabel("Title:")
        self.title_line_edit = QLineEdit()
        self.description_label = QLabel("Description:")
        self.description_text_edit = QTextEdit()
        self.start_date_label = QLabel("Start Date:")
        self.start_date_line_edit = QLineEdit()
        self.end_date_label = QLabel("End Date:")
        self.end_date_line_edit = QLineEdit()

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    def create_layout(self):

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.title_line_edit)
        main_layout.addWidget(self.description_label)
        main_layout.addWidget(self.description_text_edit)
        main_layout.addWidget(self.start_date_label)
        main_layout.addWidget(self.start_date_line_edit)
        main_layout.addWidget(self.end_date_label)
        main_layout.addWidget(self.end_date_line_edit)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)

    def create_connections(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def accept(self):
        title = self.title_line_edit.text()
        description = self.description_text_edit.toPlainText()
        start_date = self.start_date_line_edit.text()
        end_date = self.end_date_line_edit.text()

        if title and start_date and end_date:
            show = Show(title, description, start_date, end_date)
            show_dir = show.create_show_directory()
            show.save_show_data(show_dir)
            QDialog.accept(self)
        else:
            QMessageBox.warning(self, "Error", "Please fill in all required fields.")


class CreateShotDialog(QDialog):
    def __init__(self, title):
        """
        @param title: string - the name of the show which the shot will belong to

        """
        super().__init__()
        self.setWindowTitle("Create Shot")
        self.setModal(True)

        self.title = title

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.shot_id_label = QLabel("Shot ID:")
        self.shot_id_line_edit = QLineEdit()
        self.sequence_number_label = QLabel("Sequence Number:")
        self.sequence_number_line_edit = QLineEdit()
        self.duration_label = QLabel("Duration:")
        self.duration_line_edit = QLineEdit()
        self.description_label = QLabel("Description:")
        self.description_text_edit = QTextEdit()

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    def create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.shot_id_label)
        main_layout.addWidget(self.shot_id_line_edit)
        main_layout.addWidget(self.sequence_number_label)
        main_layout.addWidget(self.sequence_number_line_edit)
        main_layout.addWidget(self.duration_label)
        main_layout.addWidget(self.duration_line_edit)
        main_layout.addWidget(self.description_label)
        main_layout.addWidget(self.description_text_edit)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)

    def create_connections(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def accept(self):
        shot_id = self.shot_id_line_edit.text()
        sequence_number = self.sequence_number_line_edit.text()
        duration = self.duration_line_edit.text()
        description = self.description_text_edit.toPlainText()

        if shot_id and sequence_number and duration:
            shot = Shot(self.title, shot_id, sequence_number, duration, description)
            shot_dir = shot.create_shot_directory()
            shot.save_shot_data(shot_dir)
            QDialog.accept(self)
        else:
            QMessageBox.warning(self, "Error", "Please fill in all required fields.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primitive Show Manager")
        self.setGeometry(100, 100, 600, 400)
        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.show_main_titel_label = QLabel("Shows:")
        self.show_list_widget = QListWidget()
        self.show_info_label = QLabel("Show Information:")
        self.show_title_label = QLabel("Title:")
        self.show_title_line_edit = QLineEdit()
        self.show_description_label = QLabel("Description:")
        self.show_description_text_edit = QTextEdit()
        self.show_start_date_label = QLabel("Start Date:")
        self.show_start_date_line_edit = QLineEdit()
        self.show_end_date_label = QLabel("End Date:")
        self.show_end_date_line_edit = QLineEdit()

        self.shot_main_titel_label = QLabel("Shots:")

        self.shot_list_widget = QListWidget()

        self.shot_info_label = QLabel("Shot Information:")
        self.shot_id_label = QLabel("Shot ID:")
        self.shot_id_line_edit = QLineEdit()
        self.shot_sequence_label = QLabel("Sequence Number:")
        self.shot_sequence_line_edit = QLineEdit()
        self.shot_duration_label = QLabel("Duration:")
        self.shot_duration_line_edit = QLineEdit()
        self.shot_description_label = QLabel("Description:")
        self.shot_description_text_edit = QTextEdit()

        self.create_show_btn = QPushButton("Create Show")
        self.create_shot_btn = QPushButton("Create Shot")
        self.update_show_btn = QPushButton("Update Show")
        self.delete_show_btn = QPushButton("Delete Show")
        self.update_shot_btn = QPushButton("Update Shot")
        self.delete_shot_btn = QPushButton("Delete Shot")
        self.close_btn = QPushButton("Close")

        self.show_frame = QFrame()
        self.shot_frame = QFrame()
        self.show_frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.shot_frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    def create_layout(self):

        self.show_frame.setLayout(QVBoxLayout())
        self.shot_frame.setLayout(QVBoxLayout())

        self.show_layout = QVBoxLayout()
        self.show_layout.addWidget(self.show_main_titel_label)
        self.show_layout.addWidget(self.show_list_widget)
        self.show_layout.addWidget(self.create_show_btn)
        self.show_layout.addWidget(self.show_info_label)
        self.show_layout.addWidget(self.show_title_label)
        self.show_layout.addWidget(self.show_title_line_edit)
        self.show_layout.addWidget(self.show_description_label)
        self.show_layout.addWidget(self.show_description_text_edit)
        self.show_layout.addWidget(self.show_start_date_label)
        self.show_layout.addWidget(self.show_start_date_line_edit)
        self.show_layout.addWidget(self.show_end_date_label)
        self.show_layout.addWidget(self.show_end_date_line_edit)

        self.show_btn_layout = QHBoxLayout()
        self.show_btn_layout.addWidget(self.update_show_btn)
        self.show_btn_layout.addWidget(self.delete_show_btn)

        self.show_frame.layout().addLayout(self.show_layout)
        self.show_frame.layout().addLayout(self.show_btn_layout)

        self.shot_layout = QVBoxLayout()
        self.shot_layout.addWidget(self.shot_main_titel_label)
        self.shot_layout.addWidget(self.shot_list_widget)
        self.shot_layout.addWidget(self.create_shot_btn)
        self.shot_layout.addWidget(self.shot_info_label)
        self.shot_layout.addWidget(self.shot_id_label)
        self.shot_layout.addWidget(self.shot_id_line_edit)
        self.shot_layout.addWidget(self.shot_sequence_label)
        self.shot_layout.addWidget(self.shot_sequence_line_edit)
        self.shot_layout.addWidget(self.shot_duration_label)
        self.shot_layout.addWidget(self.shot_duration_line_edit)
        self.shot_layout.addWidget(self.shot_description_label)
        self.shot_layout.addWidget(self.shot_description_text_edit)
        self.shot_btn_layout = QHBoxLayout()

        self.shot_btn_layout.addWidget(self.update_shot_btn)
        self.shot_btn_layout.addWidget(self.delete_shot_btn)

        self.shot_frame.layout().addLayout(self.shot_layout)
        self.shot_frame.layout().addLayout(self.shot_btn_layout)

        self.main_layout = QVBoxLayout()
        self.frame_layout = QHBoxLayout()
        self.frame_layout.addWidget(self.show_frame)
        self.frame_layout.addWidget(self.shot_frame)
        self.main_layout.addLayout(self.frame_layout)
        self.main_layout.addWidget(self.close_btn)

        self.central_widget.setLayout(self.main_layout)

    def create_connections(self):
        self.show_list_widget.currentItemChanged.connect(self.update_show_select)
        self.shot_list_widget.currentItemChanged.connect(self.update_shot_select)
        self.create_show_btn.clicked.connect(self.create_show)
        self.create_shot_btn.clicked.connect(self.create_shot)
        self.update_show_btn.clicked.connect(self.update_show)
        self.delete_show_btn.clicked.connect(self.delete_show)
        self.update_shot_btn.clicked.connect(self.update_shot)
        self.delete_shot_btn.clicked.connect(self.delete_shot)
        self.close_btn.clicked.connect(self.close)

        self.refresh_shows()

    def update_show_select(self, current_item):
        """
        @param current_item: string - current selected show's name
        @return: None

        """
        show_title_item = current_item
        if show_title_item is not None:
            show_title = show_title_item.text()
            show_data = Show.get_show(show_title)

            if show_data:
                self.show_title_line_edit.setText(show_data["title"])
                self.show_description_text_edit.setText(show_data["description"])
                self.show_start_date_line_edit.setText(show_data["start_date"])
                self.show_end_date_line_edit.setText(show_data["end_date"])
                self.refresh_shots(show_title)
            else:
                self.clear_show_fields()
                self.shot_list_widget.clear()
                self.clear_shot_fields()

    def refresh_shows(self):
        self.show_list_widget.clear()
        shows = Show.get_all_shows()
        for show in shows:
            self.show_list_widget.addItem(show["title"])

    def refresh_shots(self, title):
        """
        @param title: string - the name of the show
        @return: None
        """
        self.shot_list_widget.clear()
        shots = Shot.get_all_shots(title)
        for shot in shots:
            self.shot_list_widget.addItem(shot["shot_id"])

    def update_shot_select(self, current_item):
        """

        @param current_item: string - current selected shot's name
        @return: None
        """
        show_title = self.show_list_widget.currentItem().text()
        shot_title_item = current_item
        print("shot_title_item " + str(shot_title_item))
        if shot_title_item is not None:
            shot_title = shot_title_item.text()
            shot_data = Shot.get_shot(show_title, shot_title)

            if shot_data:
                self.shot_id_line_edit.setText(shot_data["shot_id"])
                self.shot_sequence_line_edit.setText(str(shot_data["sequence_number"]))
                self.shot_duration_line_edit.setText(str(shot_data["duration"]))
                self.shot_description_text_edit.setText(shot_data["description"])
            else:
                self.shot_list_widget.clear()
                self.clear_shot_fields()

    def create_show(self):
        dialog = CreateShowDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.refresh_shows()

    def create_shot(self):
        show_title = self.show_list_widget.currentItem().text()
        if show_title:
            dialog = CreateShotDialog(show_title)
            if dialog.exec_() == QDialog.Accepted:
                self.refresh_shots(show_title)

    def update_show(self):
        show_title = self.show_list_widget.currentItem().text()
        updated_data = {
            "title": self.show_title_line_edit.text(),
            "description": self.show_description_text_edit.toPlainText(),
            "start_date": self.show_start_date_line_edit.text(),
            "end_date": self.show_end_date_line_edit.text()
        }
        if Show.update_show(show_title, updated_data):
            QMessageBox.information(self, "Success", "Show updated successfully.")
            self.refresh_shows()
        else:
            QMessageBox.warning(self, "Error", "Failed to update show.")

    def delete_show(self, show_title = [] ):
        show_title = self.show_list_widget.currentItem().text()
        reply = QMessageBox.question(
            self, "Delete Show", f"Are you sure you want to delete the show '{show_title}'?", QMessageBox.Yes,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if Show.delete_show(show_title):
                QMessageBox.information(self, "Success", "Show deleted successfully.")
                self.refresh_shows()
                self.clear_show_fields()
                self.shot_list_widget.clear()
                self.clear_shot_fields()
            else:
                QMessageBox.warning(self, "Error", "Failed to delete show.")

    def update_shot(self, show_title = [], shot_id = [], updated_data = [] ):
        show_title = self.show_list_widget.currentItem().text()
        shot_id = self.shot_list_widget.currentItem().text()
        updated_data = {
            "shot_id": self.shot_id_line_edit.text(),
            "sequence_number": int(self.shot_sequence_line_edit.text()),
            "duration": int(self.shot_duration_line_edit.text()),
            "description": self.shot_description_text_edit.toPlainText()
        }
        if Shot.update_shot(show_title, shot_id, updated_data):
            QMessageBox.information(self, "Success", "Shot updated successfully.")
            self.refresh_shots(show_title)
        else:
            QMessageBox.warning(self, "Error", "Failed to update shot.")

    def delete_shot(self, show_title = [], shot_id = []):
        show_title = self.show_list_widget.currentItem().text()
        shot_id = self.shot_list_widget.currentItem().text()
        reply = QMessageBox.question(
            self, "Delete Shot", f"Are you sure you want to delete the shot '{shot_id}'?", QMessageBox.Yes,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if Shot.delete_shot(show_title, shot_id):
                QMessageBox.information(self, "Success", "Shot deleted successfully.")
                self.refresh_shots(show_title)
                self.clear_shot_fields()
            else:
                QMessageBox.warning(self, "Error", "Failed to delete shot.")

    def clear_show_fields(self):
        self.show_title_line_edit.clear()
        self.show_description_text_edit.clear()
        self.show_start_date_line_edit.clear()
        self.show_end_date_line_edit.clear()

    def clear_shot_fields(self):
        self.shot_id_line_edit.clear()
        self.shot_sequence_line_edit.clear()
        self.shot_duration_line_edit.clear()
        self.shot_description_text_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



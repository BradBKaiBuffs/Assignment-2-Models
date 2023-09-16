from django.db import models

# CHOICE OF YES OR NO
class Choice(models.TextChoices):
    Yes = "YES", "Yes"
    No = "NO", "No"

# Create your models here.
# Student
class Student (models.Model):
    wt_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.wt_id} ({self.first_name} {self.last_name})"

# Course
class Course (models.Model):
    course_id = models.CharField(max_length = 10, primary_key = True)
    course_name = models.CharField(max_length = 60)
    credit_hours = models.IntegerField(max_length = 3)
    prerequisite = models.CharField(max_length = 3, choices=Choice.choices)

    def __str__(self):
        return f"{self.course_name}"

# Major
class Major (models.Model):
    major_id = models.AutoField(primary_key = True)
    major_name = models.CharField(max_length = 60)
    total_hours = models.IntegerField(max_length = 3)

    def __str__(self):
        return f"{self.major_name}"

# Requirement
class Requirement (models.Model):
    requirement_id = models.AutoField(primary_key = True)
    req_type = models.CharField(max_length = 60)
    req_desc = models.CharField(max_length = 60)
    req_hours = models.IntegerField(max_length = 3)

    def __str__(self):
        return f"{self.req_type} ({self.req_desc})"

# Enroll
class Enroll (models.Model):
    enroll_id = models.AutoField(primary_key = True)
    wt_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.enroll_id

# Major_requirement
class Major_requirement (models.Model):
    maj_req_id = models.AutoField(primary_key = True)
    major_id = models.ForeignKey(Major, on_delete = models.CASCADE)
    requirement_id = models.ForeignKey(Requirement, on_delete = models.CASCADE)

    def __str__(self):
        return self.maj_req_id

# Major_selection
class Major_selection (models.Model):
    maj_sel_id = models.AutoField(primary_key = True)
    wt_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    major_id = models.ForeignKey(Major, on_delete = models.CASCADE)
    selection_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.maj_sel_id

# Course_requirement
class Course_requirement (models.Model):
    course_req_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    requirement_id = models.ForeignKey(Requirement, on_delete = models.CASCADE)
    recommended = models.CharField(max_length = 3, choices=Choice.choices)
    lang_equiv = models.CharField(max_length = 3, choices=Choice.choices)

    def __str__(self):
        return f"{self.recommended} {self.lang_equiv}"
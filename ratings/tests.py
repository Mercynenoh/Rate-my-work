from django.test import TestCase

# Create your tests here.

class ProjectTest(TestCase):

    def create_project(self, pic="https://mdbcdn.b-cdn.net/img/new/fluid/nature/011.webp",bio="this is my bio", email="mercy@gmail.com", phone="1234567890"):
        return Profile.objects.create(pic=pic, bio=bio, email=email, phone=phone)

    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
        self.assertEqual(w.__unicode__(), w.bio)

class ProjectTest(TestCase):

    def create_project(self, image="https://mdbcdn.b-cdn.net/img/new/fluid/nature/011.webp",title="beach", description="good" , link="https://mypic-perfect.herokuapp.com/"):
        return Project.objects.create(pic=pic, bio=bio, title=title,description=description )

    def test_project_creation(self):
        w = self.create_project()
        self.assertTrue(isinstance(w, Project))
        self.assertEqual(w.__unicode__(), w.title)
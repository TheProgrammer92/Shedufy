from django_seed import Seed

from myresources.models import *
seeder = Seed.seeder()

seeder.add_entity(Adress, 5)
seeder.add_entity(Teacher, 10)
seeder.add_entity(Course, 10)
seeder.add_entity(CategoryCourse, 10)

inserted_pks = seeder.execute()
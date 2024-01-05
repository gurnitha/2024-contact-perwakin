# 2024-contact-perwakin
Membuat contact manager


#### 1. Create new project, app and a note file

        modified:   .gitignore
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   contact/__init__.py
        new file:   contact/admin.py
        new file:   contact/apps.py
        new file:   contact/migrations/__init__.py
        new file:   contact/models.py
        new file:   contact/tests.py
        new file:   contact/views.py
        new file:   manage.py
        new file:   note.txt


#### 2. Create Region and Country models with OneToMany relationship

        modified:   README.md
        modified:   contact/admin.py
        new file:   contact/migrations/0001_initial.py
        new file:   contact/migrations/0002_country.py
        modified:   contact/models.py


#### 3. Create City model and added OneToMany relationship with Country and Region

        modified:   README.md
        modified:   contact/admin.py
        new file:   contact/migrations/0003_alter_country_options_city.py
        modified:   contact/models.py

#### 4. Created more models and added relationships 

        modified:   contact/admin.py
        new file:   contact/migrations/0004_category.py
        new file:   contact/migrations/0005_perwakin.py
        new file:   contact/migrations/0006_bidang_group.py
        new file:   contact/migrations/0007_gender_hobby_isimportant_profession_contact.py
        new file:   contact/migrations/0008_alter_contact_options_remove_contact_hobby_and_more.py
        new file:   contact/migrations/0009_remove_contact_profession_contact_profession.py
        new file:   contact/migrations/0010_interest_contact_interest.py
        new file:   contact/migrations/0011_salutation_contact_salutation.py
        new file:   contact/migrations/0012_remove_contact_group_contact_group.py
        modified:   contact/models.py
        modified:   note.txt
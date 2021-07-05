from django.contrib.admin import AdminSite


class TraineeAdminSite(AdminSite):
    site_title = 'hello'
    # site_url = '/administrator/'


training_subject_admin = TraineeAdminSite(name='trainiee_subject_admin')

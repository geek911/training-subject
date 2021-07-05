# Generated by Django 3.2.4 on 2021-06-29 20:44

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.utils
import edc_utils.date
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectScreening',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('screening_identifier', models.CharField(editable=False, max_length=36, unique=True, verbose_name='Eligibility Identifier')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text='Date and time of report.', validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date and Time')),
                ('subject_citizenship', django_countries.fields.CountryField(max_length=2, verbose_name='Subject country of citizenship?')),
                ('subject_spouse_citizenship', django_countries.fields.CountryField(max_length=2, verbose_name='Subject spouse citizenship if married')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='Subject gender')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Subject age')),
                ('marriage_proof', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Did subject provide marriage proof?')),
                ('is_subject_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Is the subject literate')),
                ('is_literate_witness_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='If not literate, does the subject have a literate witness?')),
                ('is_guardian_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='If minor, does the subject have a guardian?')),
                ('is_eligible', models.BooleanField(editable=False)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Eligibility Confirmation',
                'verbose_name_plural': 'Eligibility Confirmation',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSubjectScreening',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('screening_identifier', models.CharField(db_index=True, editable=False, max_length=36, verbose_name='Eligibility Identifier')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow, help_text='Date and time of report.', validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date and Time')),
                ('subject_citizenship', django_countries.fields.CountryField(max_length=2, verbose_name='Subject country of citizenship?')),
                ('subject_spouse_citizenship', django_countries.fields.CountryField(max_length=2, verbose_name='Subject spouse citizenship if married')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='Subject gender')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Subject age')),
                ('marriage_proof', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Did subject provide marriage proof?')),
                ('is_subject_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Is the subject literate')),
                ('is_literate_witness_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='If not literate, does the subject have a literate witness?')),
                ('is_guardian_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='If minor, does the subject have a guardian?')),
                ('is_eligible', models.BooleanField(editable=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Eligibility Confirmation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

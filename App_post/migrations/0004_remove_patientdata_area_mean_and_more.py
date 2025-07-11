# Generated by Django 5.1.2 on 2025-05-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0003_alter_patientdata_area_mean_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='area_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='area_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='area_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='compactness_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='compactness_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='compactness_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concave_points_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concave_points_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concave_points_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concavity_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concavity_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='concavity_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='fractal_dimension_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='fractal_dimension_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='fractal_dimension_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='perimeter_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='perimeter_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='perimeter_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='radius_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='radius_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='radius_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='smoothness_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='smoothness_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='smoothness_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='symmetry_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='symmetry_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='symmetry_worst',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='texture_mean',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='texture_se',
        ),
        migrations.RemoveField(
            model_name='patientdata',
            name='texture_worst',
        ),
        migrations.AddField(
            model_name='patientdata',
            name='age',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='alcohol_consuming',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='allergy',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='anxiety',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='chest_pain',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='chronic_disease',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='coughing',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='fatigue',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='peer_pressure',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='shortness_of_breath',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='smoking',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='swallowing_difficulty',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='wheezing',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='yellow_fingers',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
    ]

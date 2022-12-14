# Generated by Django 4.1 on 2022-09-02 15:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('term', models.CharField(max_length=20)),
                ('subhead', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='post_photo')),
                ('tag1', models.CharField(max_length=10)),
                ('tag2', models.CharField(max_length=10)),
                ('tag3', models.CharField(max_length=10)),
                ('tag4', models.CharField(max_length=10)),
                ('tag5', models.CharField(max_length=10)),
                ('body', models.TextField()),
                ('loc1', models.CharField(max_length=10)),
                ('loc2', models.CharField(max_length=10)),
                ('target', multiselectfield.db.fields.MultiSelectField(choices=[('1', '대학생'), ('2', '군인'), ('3', '청년')], default='1', max_length=20)),
                ('category', models.CharField(choices=[('support', '지원 정책'), ('product', '금융 상품'), ('tip', '팁')], default='support', max_length=20)),
                ('income', multiselectfield.db.fields.MultiSelectField(choices=[('무소득', '무소득'), ('1~100만원', '1~100만원'), ('101~200만원', '101~200만원'), ('201~300만원', '201~300만원'), ('301만원~400만원', '301만원~400만원'), ('401만원초과', '401만원초과')], default='무소득', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

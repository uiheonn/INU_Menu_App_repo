# Generated by Django 3.2.16 on 2023-04-13 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jmc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='EMAIL ID.', max_length=64, unique=True, verbose_name='email id')),
                ('username', models.CharField(max_length=30, null=True, unique=True, verbose_name='username')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('Introduction', models.CharField(blank=True, max_length=50, null=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
                'managed': True,
            },
            managers=[
                ('objects', jmc.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('emotion', models.CharField(blank=True, max_length=20, null=True)),
                ('weather', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=jmc.models.MenuImagePath)),
            ],
            options={
                'db_table': 'menu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=45)),
                ('business_hours', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('category_name', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='restaurant/')),
            ],
            options={
                'db_table': 'restaurant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('달걀', models.IntegerField(blank=True, default=0, null=True)),
                ('우유', models.IntegerField(blank=True, default=0, null=True)),
                ('밀', models.IntegerField(blank=True, default=0, null=True)),
                ('콩', models.IntegerField(blank=True, default=0, null=True)),
                ('땅콩', models.IntegerField(blank=True, default=0, null=True)),
                ('생선', models.IntegerField(blank=True, default=0, null=True)),
                ('고기', models.IntegerField(blank=True, default=0, null=True)),
                ('조개', models.IntegerField(blank=True, default=0, null=True)),
                ('갑각류', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_allergy',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=jmc.models.ReviewImagePath)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.menu')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PreferredMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'preferred_menu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('gram', models.FloatField(blank=True, null=True)),
                ('calorie', models.FloatField(blank=True, null=True)),
                ('carbohydrate', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('saturatedfat', models.FloatField(blank=True, null=True)),
                ('unsaturatedfat', models.FloatField(blank=True, null=True)),
                ('cholesterol', models.IntegerField(blank=True, null=True)),
                ('sodium', models.IntegerField(blank=True, null=True)),
                ('potash', models.IntegerField(blank=True, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=100, null=True)),
                ('allergy', models.CharField(blank=True, max_length=50, null=True)),
                ('menu', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.menu')),
            ],
            options={
                'db_table': 'nutrition',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MenuRecommendLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'menu_recommend_log',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jmc.restaurant'),
        ),
    ]

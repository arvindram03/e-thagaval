# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('ethagaval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcePage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='wagtailcore.Page', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('date_from', models.DateField(verbose_name='Start date')),
                ('time_from', models.TimeField(verbose_name='Start time', null=True, blank=True)),
                ('time_to', models.TimeField(verbose_name='End time', null=True, blank=True)),
                ('location', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='+', blank=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ResourcePageCarouselItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='+', blank=True, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='ethagaval.ResourcePage', related_name='carousel_items')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResourcePageOwner',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('first_name', models.CharField(verbose_name='Name', blank=True, max_length=255)),
                ('last_name', models.CharField(verbose_name='Surname', blank=True, max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='+', blank=True, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='ethagaval.ResourcePage', related_name='owners')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResourcePageRelatedLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_document', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='ethagaval.ResourcePage', related_name='related_links')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_to',
            field=models.DateField(verbose_name='End date', null=True, blank=True, help_text='Not required if event is on a single day'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_from',
            field=models.TimeField(verbose_name='Start time', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_to',
            field=models.TimeField(verbose_name='End time', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(verbose_name='Name', blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(verbose_name='Surname', blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
    ]

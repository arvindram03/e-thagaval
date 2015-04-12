# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtaildocs', '0002_initial_data'),
        ('ethagaval', '0002_auto_20150412_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ResourceIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_document', models.ForeignKey(blank=True, related_name='+', null=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, related_name='+', null=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(to='ethagaval.ResourceIndexPage', related_name='related_links')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]

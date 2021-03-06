# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailforms', '0001_initial'),
        ('wagtailsearch', '0001_initial'),
        ('wagtailredirects', '0001_initial'),
        ('ethagaval', '0004_auto_20150412_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
        migrations.DeleteModel(
            name='BlogIndexPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageCarouselItem',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
        migrations.DeleteModel(
            name='PersonPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='standardindexpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='standardindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='StandardIndexPage',
        ),
        migrations.DeleteModel(
            name='StandardIndexPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='StandardPageCarouselItem',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='StandardPage',
        ),
        migrations.DeleteModel(
            name='StandardPageRelatedLink',
        ),
    ]

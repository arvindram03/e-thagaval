# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailredirects', '0001_initial'),
        ('wagtailsearch', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('ethagaval', '0003_resourceindexpage_resourceindexpagerelatedlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventIndexPage',
        ),
        migrations.DeleteModel(
            name='EventIndexPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventPageCarouselItem',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
        migrations.DeleteModel(
            name='EventPageSpeaker',
        ),
    ]

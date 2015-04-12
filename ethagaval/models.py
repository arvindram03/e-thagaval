from datetime import date

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase
    
from ethagaval.utils import export_event


EVENT_AUDIENCE_CHOICES = (
    ('public', "Public"),
    ('private', "Private"),
)


# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True


# Carousel items

class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Related links

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Advert Snippet

class AdvertPlacement(models.Model):
    page = ParentalKey('wagtailcore.Page', related_name='advert_placements')
    advert = models.ForeignKey('ethagaval.Advert', related_name='+')


class Advert(models.Model):
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='adverts',
        null=True,
        blank=True
    )
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        PageChooserPanel('page'),
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __unicode__(self):
        return self.text

register_snippet(Advert)


# Home Page

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('ethagaval.HomePage', related_name='carousel_items')


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('ethagaval.HomePage', related_name='related_links')


class HomePage(Page):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Homepage"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    InlinePanel(HomePage, 'carousel_items', label="Carousel items"),
    InlinePanel(HomePage, 'related_links', label="Related links"),
]

HomePage.promote_panels = Page.promote_panels


# Contact page

class ContactPage(Page, ContactFields):
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    MultiFieldPanel(ContactFields.panels, "Contact"),
]

ContactPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]

#Resource Index

class ResourceIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('ethagaval.ResourceIndexPage', related_name='related_links')


class ResourceIndexPage(Page):
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )

    @property
    def resources(self):
        # Get list of live event pages that are descendants of this page
        resources = ResourcePage.objects.live().descendant_of(self)

        # Filter resources list to get ones that are either
        # running now or start in the future
        # resources = resources.filter(date_from__gte=date.today())

        # Order by date
        resources = resources.order_by('date_from')

        return resources

ResourceIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('description', classname="full"),
    InlinePanel(ResourceIndexPage, 'related_links', label="Related links"),
]

ResourceIndexPage.promote_panels = Page.promote_panels


class ResourcePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('ethagaval.ResourcePage', related_name='carousel_items')


class ResourcePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('ethagaval.ResourcePage', related_name='related_links')


class ResourcePageOwner(Orderable, LinkFields):
    page = ParentalKey('ethagaval.ResourcePage', related_name='owners')
    first_name = models.CharField("Name", max_length=255, blank=True)
    last_name = models.CharField("Surname", max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def name_display(self):
        return self.first_name + " " + self.last_name

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        ImageChooserPanel('image'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]


class ResourcePage(Page):
    name = models.CharField(max_length=255)
    date_from = models.DateField("Start date")
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)
    location = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('location'),
        index.SearchField('description'),
        index.SearchField('name'),
    )

    @property
    def resource_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(ResourceIndexPage).last()

    def serve(self, request):
        if "format" in request.GET:
            if request.GET['format'] == 'ical':
                # Export to ical format
                response = HttpResponse(
                    export_event(self, 'ical'),
                    content_type='text/calendar',
                )
                response['Content-Disposition'] = 'attachment; filename=' + self.slug + '.ics'
                return response
            else:
                # Unrecognised format error
                message = 'Could not export event\n\nUnrecognised format: ' + request.GET['format']
                return HttpResponse(message, content_type='text/plain')
        else:
            # Display event page as usual
            return super(ResourcePage, self).serve(request)

ResourcePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('name'),
    FieldPanel('date_from'),
    FieldPanel('time_from'),
    FieldPanel('time_to'),
    FieldPanel('location'),
    InlinePanel(ResourcePage, 'carousel_items', label="Carousel items"),
    FieldPanel('description', classname="full"),
    InlinePanel(ResourcePage, 'owners', label="Owners"),
    InlinePanel(ResourcePage, 'related_links', label="Related links"),
]

ResourcePage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

FormPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel(FormPage, 'form_fields', label="Form fields"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailmenus.models import FlatMenu

from books.blocks import CodeBlock


class BookPage(Page):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Página de libro"

    def get_context(self, request):
        context = super().get_context(request)
        menu = BookIndexPage.objects.all().ancestor_of(self)[0].flat_menu
        context["menu"] = FlatMenu.objects.filter(handle=menu)[0]
        list_pages = list(context["menu"].pages_for_display.values())
        context["num_pages"] = len(list_pages) - 1
        num_index = list_pages.index(self)
        context["num_index"] = num_index
        context["prev"] = list_pages[num_index - 1]
        if context["num_index"] < context["num_pages"]:
            context["next"] = list_pages[num_index + 1]
        return context

    show_in_menus_default = True

    body = StreamField(
        [
            (
                "paragraph",
                blocks.RichTextBlock(
                    label="Contenido",
                    features=[
                        "h2",
                        "h3",
                        "h4",
                        "h5",
                        "bold",
                        "italic",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                        "image",
                        "embed",
                        "code",
                        "superscript",
                        "subscript",
                        "strikethrough",
                        "blockquote",
                    ],
                ),
            ),
            ("code", CodeBlock(label="Code")),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    parent_page_types = ["books.BookIndexPage", "books.BookPage"]

    subpage_types = ["books.BookPage"]


class BookIndexPage(Page):
    """
    Shows a list of book chapters.
    """

    class Meta:
        verbose_name = "Índice de libro"

    show_in_menus_default = True

    flat_menu = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Si no está en la lista, se asignará automáticamente cuando crees la página",
    )

    content_panels = [
        FieldPanel(
            "flat_menu", classname="full", heading="Índice para la barra lateral"
        ),
    ] + Page.content_panels

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["books.BooksListingPage"]

    # Only allow ArticlePages beneath this page.
    subpage_types = ["books.BookPage"]


class BooksListingPage(Page):
    """
    Shows a list of books.
    """

    class Meta:
        verbose_name = "Listado de libros de CATEDU"

    def get_context(self, request):
        """Añadiendo libros a este listado"""
        context = super().get_context(request)
        context["books"] = BookIndexPage.objects.all()
        return context

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "books.BookIndexPage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["books.BookIndexPage"]

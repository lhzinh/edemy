from core.models import AuditMixin, SlugifyMixin, SoftDeleteMixin
from core.utils import handle_upload
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(SlugifyMixin, SoftDeleteMixin, AuditMixin):
    name = models.CharField(_("title"), unique=True, max_length=80)

    def __str__(self):
        return self.name


class Status(models.TextChoices):
    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")
    COMING_SOON = "soon", _("Coming Soon")


class Course(SlugifyMixin, SoftDeleteMixin, AuditMixin):
    name = models.CharField(_("subject"), unique=True, max_length=120)
    status = models.CharField(
        _("status"), max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    image = models.ImageField(
        upload_to=f"courses/{handle_upload}", default="", blank=True, null=True
    )
    description = models.TextField(_("description"), blank=True)
    short_description = models.CharField(_("short description"), max_length=100)
    price = models.DecimalField(
        _("price"),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )
    metadata = models.JSONField(default=dict, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_("category"),
        on_delete=models.PROTECT,
        related_name="courses",
    )

    class Meta:
        indexes = [
            models.Index(fields=["date_published"]),
            models.Index(fields=["category", "date_published"]),
            models.Index(
                fields=["date_published"],
                name="published_courses_idx",
                condition=models.Q(date_published__isnull=False),
            ),
        ]
        ordering = ["-date_published"]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('courses:view_lesson', args=[str(self.course.slug), str(self.slug)])

    # def clean(self):
    #     self.title = self.title.capitalize()
    #     self.slug = self.slug.lower()


# class Enrollment(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
#     student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='students')

#     def __str__(self):
#         return self.student.email


class Module(models.Model):
    name = models.CharField(_("subject"), unique=True, max_length=100)
    tagline = models.CharField(
        _("tagline"), max_length=50, default="Module tagline here up to 50 chapters"
    )
    position = models.PositiveIntegerField(_("position"), default=1)
    course = models.ForeignKey(
        Course,
        verbose_name=_("course"),
        on_delete=models.CASCADE,
        related_name="modules",
    )

    def __str__(self):
        return self.name

    # def clean(self):
    #     self.title = self.title.capitalize()


class Lesson(models.Model):
    name = models.CharField(_("subject"), max_length=125, unique=True)
    status = models.CharField(
        _("status"), max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    is_completed = models.BooleanField(_("completed"), default=False)
    is_free_preview = models.BooleanField(_("free preview"), default=False)
    position = models.PositiveIntegerField(_("position"), default=1)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to=f"lessons/{handle_upload}", default="", blank=True, null=True
    )
    # video = models.FileField(upload_to=course_file_upload_path, null=True, blank=True)
    module = models.ForeignKey(
        Module,
        verbose_name=_("module"),
        on_delete=models.CASCADE,
        related_name="lessons",
    )

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('courses:view_lesson', args=[str(self.course.slug), str(self.slug)])

    # def clean(self):
    #     self.title = self.title.capitalize()
    #     self.slug = self.slug.lower()


class Pdf(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

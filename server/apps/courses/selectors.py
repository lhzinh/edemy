from courses.models import Category, Course


def active_categories():
    """
    Fetches a list of active categories.
    """
    return Category.objects.all()


def active_courses():
    """
    Fetches a list of active courses.
    """
    return Course.objects.all()

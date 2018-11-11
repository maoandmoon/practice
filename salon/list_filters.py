from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import *


class SubCategoryListFilter(admin.SimpleListFilter):
    """
    This filter is an example of how to combine two different Filters to work together.
    """
    # Human-readable title which will be displayed in the right admin sidebar just above the filter
    # options.
    title = 'breed'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'breed'

    # Custom attributes
    related_filter_parameter = 'breed__species__id__exact'


    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_questions = []
        queryset = SubCategory.objects.order_by('category_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(category_id=request.GET[self.related_filter_parameter])
        for breed in queryset:
            list_of_questions.append(
                (str(breed.id), breed.name)
            )
        return sorted(list_of_questions, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(breed_id=self.value())
        return queryset


class CategoryListFilter(admin.SimpleListFilter):
    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'category'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'category'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_category = []
        queryset = Category.objects.all()
        for category in queryset:
            list_of_category.append(
                (str(category.id), category.title)
            )
        return sorted(list_of_category, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(category_id=self.value())
        return queryset

    def value(self):
        """
        Overriding this method will allow us to always have a default value.
        """
        value = super(CategoryListFilter, self).value()
        if value is None:
            if self.default_value is None:
                # If there is at least one Species, return the first by title. Otherwise, None.
                first_category = Category.objects.order_by('title').first()
                value = None if first_category is None else first_category.id
                self.default_value = value
            else:
                value = self.default_value
        return str(value)

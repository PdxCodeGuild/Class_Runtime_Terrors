from django.contrib import admin
from django.db.models import Count
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "tag_count")
    date_hierachy = "pub_date"
    list_filter = ("pub_date",)
    search_fields = ("title", "text")

    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'author', 'text',
            )}),
        ('Related', {
            'fields': (
                'tags', 'crystals'
            )}),
    )
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('crystals', 'tags',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            tag_number=Count('tags')
        )

    def tag_count(self, post):
        return post.tag_number
    tag_count.short_description = "Number of tags"
    tag_count.admin_order_field = 'tag_number'
from django.urls import path
from core.views import index, category_list_view, product_list_view, category_product_list_view, vendor_list_view, vendor_product_list_view, product_detail_view, tag_list, ajax_add_review

app_name = "core"

urlpatterns = [
    path("", index, name="index"),

    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),

    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    path("vendor/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_product_list_view, name="vendor-product-list"),

    #Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    #Add Review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name='ajax_add_review'),
]
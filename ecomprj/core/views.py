
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItem, ProductReview, Wishlist, Address
from django.db.models import Avg
from taggit.models import Tag
from core.forms import ProductReviewForm
from django.contrib import messages


# Create your views here.


def index(request):
    products = Product.objects.filter(product_status="published", featured=True).order_by("-datetime_created")

    last_products = Product.objects.filter(product_status="published", featured=True).order_by("-datetime_created")[:3]

    context = {
        "products": products,
        "last_products": last_products
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published", featured=True)
    
    
    context = {
        "products": products
        
    }
    return render(request, 'core/product-list.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)

    products = Product.objects.filter(category=product.category).exclude(pid=pid)[:3]

    # Getting all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-datetime_created")

    average_rating = get_average_rating(reviews=reviews)

    # Product Review Form
    review_form = ProductReviewForm()

    p_images = product.p_images.all()

    context = {
        "product" : product,
        "review_form": review_form,
        "p_images": p_images, 
        "reviews": reviews,
        "average_rating": average_rating,
        "products": products,
    }
    return render(request, 'core/product-detail.html', context)

def get_average_rating(reviews):
    # Getting average rating
    average_rating = reviews.aggregate(rating=Avg('rating'))
    if average_rating['rating'] == None:
        average_rating['rating'] = 0.0

    return average_rating

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category":category,
        "products":products
    }
    return render(request, "core/category-product-list.html", context)

def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context = {
        "vendors":vendors
    }
    return render(request, "core/vendor-list.html", context)

def vendor_product_list_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(product_status="published", vendor=vendor)

    context = {
        "vendor":vendor,
        "products":products
    }
    return render(request, "core/vendor-product-list.html", context)

def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag,
    }

    return render(request, "core/tag.html", context)

def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    single_review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST["review"],
        rating = request.POST["rating"]
    )

    context = {
        'user': user.username,
        'datetime_created': single_review.datetime_created,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )


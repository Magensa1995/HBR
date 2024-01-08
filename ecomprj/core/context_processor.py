from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItem, ProductReview, Wishlist, Address

def default(request):
    categories = Category.objects.all()

    return {
        'categories': categories
    }
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import dashboard, product_list, product_edit, product_delete, inventory, update_stock, sales, record_sale, category_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('inventory/', inventory, name='inventory'),
    path('sales/', sales, name='sales'),
    path('sales/record/', record_sale, name='record_sale'),
    path('inventory/update_stock/<int:product_id>/', update_stock, name='update_stock'),
    path('products/edit/<int:product_id>/', product_edit, name='product_edit'),
    path('products/delete/<int:product_id>/', product_delete, name='product_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
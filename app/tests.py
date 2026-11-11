
from django.test import TestCase
from django.urls import reverse

from app.models import Product


class ProductViewBaselineTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mobile = Product.objects.create(
            title="Samsung Test Mobile",
            selling_price=15000,
            discounted_price=12000,
            description="Test mobile",
            brand="Samsung",
            category="M",
            product_image="productimg/test-mobile.jpg",
        )

        cls.laptop = Product.objects.create(
            title="Dell Test Laptop",
            selling_price=50000,
            discounted_price=45000,
            description="Test laptop",
            brand="Dell",
            category="L",
            product_image="productimg/test-laptop.jpg",
        )

        cls.topwear = Product.objects.create(
            title="Test Shirt",
            selling_price=1500,
            discounted_price=1200,
            description="Test topwear",
            brand="Test Brand",
            category="TW",
            product_image="productimg/test-shirt.jpg",
        )

    def test_home_page_loads_successfully(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_home_page_separates_products_by_category(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mobile, response.context["mobile"])
        self.assertIn(self.laptop, response.context["laptop"])
        self.assertIn(self.topwear, response.context["topwears"])

    def test_mobile_page_displays_only_mobile_products(self):
        response = self.client.get(reverse("mobile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mobile.title)
        self.assertNotContains(response, self.laptop.title)

    def test_mobile_brand_filter(self):
        response = self.client.get(
            reverse("mobiledata", args=["Samsung"])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mobile.title)
        self.assertNotContains(response, self.laptop.title)

    def test_laptop_page_displays_only_laptop_products(self):
        response = self.client.get(reverse("laptop"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.laptop.title)
        self.assertNotContains(response, self.mobile.title)

    def test_laptop_brand_filter(self):
        response = self.client.get(
            reverse("laptopdata", args=["Dell"])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.laptop.title)
        self.assertNotContains(response, self.mobile.title)

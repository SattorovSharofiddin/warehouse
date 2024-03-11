from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, ProductMaterial, Warehouse


class ProductMaterialsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_materials_info = []

        for product in products:
            product_material_info = {
                "product_name": product.name,
                "product_qty": product.qty if hasattr(product, 'qty') else 0,
                "product_materials": []
            }

            product_materials = ProductMaterial.objects.filter(product=product)

            for product_material in product_materials:
                material = product_material.material
                warehouses = Warehouse.objects.filter(material=material)

                for warehouse in warehouses:
                    material_info = {
                        "warehouse_id": warehouse.id,
                        "material_name": material.name,
                        "qty": warehouse.remainder,
                        "price": warehouse.price
                    }
                    product_material_info["product_materials"].append(material_info)

            product_materials_info.append(product_material_info)

        return Response({"result": product_materials_info})

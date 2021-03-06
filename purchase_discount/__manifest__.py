{
    "name": "Purchase order lines with discounts for MAS ",
    "version": "14.0.6",
    "category": "Purchase Management",
    'author': 'Prixgen Tech Solutions Pvt. Ltd.',
    'company': 'Prixgen Tech Solutions Pvt. Ltd.',
    'website': 'https://www.prixgen.com',
    "depends": ["purchase_stock"],
    "data": [
        'security/ir.model.access.csv',
        'wizard/views.xml',
        "views/purchase_discount_view.xml",
        "views/report_purchaseorder.xml",
        "views/product_supplierinfo_view.xml",
        "views/res_partner_view.xml",
    ],

    "installable": True,
}

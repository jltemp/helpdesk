# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk Project",
    "summary": """
        Helpdesk""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "AdaptiveCity, "
    "C2i Change 2 Improve, "
    "Domatix, "
    "Factor Libre, "
    "SDi Soluciones, "
    "PESOL ,"
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt","project",],
    "data": [
        'views/project_views.xml',
        'views/ticket_views.xml',
    ],
    "demo": [],
    "development_status": "Alpha",
    "application": True,
    "installable": True,
}
